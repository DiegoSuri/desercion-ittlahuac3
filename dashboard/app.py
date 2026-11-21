import os
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier

st.set_page_config(
    page_title="Dashboard Deserción - ITTláhuac III",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Monitor Analítico de Deserción Escolar — ITTláhuac III (TecNM)")
st.markdown("Tablero ejecutivo para detección temprana de riesgo académico y socioeconómico (Equipo 6).")

ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(ruta_actual, "desercion_ittlahuac3.csv")
df = pd.read_csv(ruta_csv)

st.sidebar.header("Filtros de Exploración")
carrera_sel = st.sidebar.multiselect(
    "Selecciona Carrera:",
    options=sorted(df['carrera'].unique()),
    default=sorted(df['carrera'].unique())
)
semestre_sel = st.sidebar.slider("Rango de Semestre:", 1, 8, (1, 8))

df_filt = df[
    (df['carrera'].isin(carrera_sel)) &
    (df['semestre'].between(semestre_sel[0], semestre_sel[1]))
]

if df_filt.empty:
    st.warning("Selecciona al menos una carrera en el panel izquierdo para visualizar los datos.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
tasa_desercion = df_filt['desercion'].mean() * 100
col1.metric("Total Estudiantes", f"{len(df_filt)}")
col2.metric("Tasa de Riesgo / Deserción", f"{tasa_desercion:.1f}%")
col3.metric("Promedio General", f"{df_filt['promedio_general'].mean():.1f}")
col4.metric("Asistencia Media", f"{df_filt['asistencia_pct'].mean():.1f}%")

st.divider()

tab1, tab2, tab3 = st.tabs([
    "📊 Vista 1: Panorama Académico",
    "🚌 Vista 2: Factores Socioeconómicos",
    "🤖 Vista 3: Simulador Predictivo"
])

with tab1:
    c1, c2 = st.columns(2)
    df_plot1 = df_filt.copy()
    df_plot1['Estatus'] = df_plot1['desercion'].map({0: 'Permanece (0)', 1: 'Deserta (1)'})

    fig1 = px.histogram(
        df_plot1, x="materias_reprobadas", color="Estatus", barmode="group",
        color_discrete_map={'Permanece (0)': '#2b5c8f', 'Deserta (1)': '#d95f02'},
        title="Materias Reprobadas vs. Estatus de Deserción",
        labels={'materias_reprobadas': 'Materias Reprobadas', 'count': 'Estudiantes'}
    )
    c1.plotly_chart(fig1, use_container_width=True)

    fig2 = px.box(
        df_plot1, x="carrera", y="promedio_general", color="Estatus",
        color_discrete_map={'Permanece (0)': '#2b5c8f', 'Deserta (1)': '#d95f02'},
        title="Distribución de Promedio General por Carrera",
        labels={'carrera': 'Carrera', 'promedio_general': 'Promedio General (0-100)'}
    )
    c2.plotly_chart(fig2, use_container_width=True)

with tab2:
    c3, c4 = st.columns(2)
    df_plot2 = df_filt.copy()
    df_plot2['Estatus'] = df_plot2['desercion'].map({0: 'Permanece (0)', 1: 'Deserta (1)'})

    fig3 = px.scatter(
        df_plot2, x="traslado_min", y="asistencia_pct", color="Estatus",
        color_discrete_map={'Permanece (0)': '#2b5c8f', 'Deserta (1)': '#d95f02'},
        title="Tiempo de Traslado (min) vs. Asistencia (%)",
        labels={'traslado_min': 'Tiempo de Traslado (minutos)', 'asistencia_pct': 'Asistencia (%)'}
    )
    c3.plotly_chart(fig3, use_container_width=True)

    df_beca = df_plot2.groupby(['beca_transporte_sectei', 'Estatus']).size().reset_index(name='Estudiantes')
    fig4 = px.bar(
        df_beca, x="beca_transporte_sectei", y="Estudiantes", color="Estatus", barmode="group",
        color_discrete_map={'Permanece (0)': '#2b5c8f', 'Deserta (1)': '#d95f02'},
        title="Impacto de la Beca de Transporte SECT
