# 🎓 Predicción y Análisis de la Deserción Escolar — ITTláhuac III (TecNM)

**Asignatura:** Ingeniería en Ciencia de Datos  
**Fase:** Fase 3 — Ejecución, Modelado y Visualización  
**Metodología:** CRISP-DM  
**Equipo 6:**
* **Solano Blancas Diego Suriel** (`L261120068@Tlahuac3.tecnm.mx`) — *Líder / Programador*
* **Alberto Luis Flores Hernandez** (`C261120058@Tlahuac3.tecnm.mx`) — *Data Science*

---

## 📋 Descripción del Proyecto
Este proyecto implementa un pipeline completo de Ciencia de Datos para analizar los factores académicos y socioeconómicos asociados a la deserción escolar en el **Instituto Tecnológico de Tláhuac III (TecNM)** y predecir tempranamente el riesgo de abandono estudiantil mediante aprendizaje automático supervisado.

## 📂 Estructura del Repositorio
* `/data`: Conjunto de datos limpio (`desercion_ittlahuac3.csv`) con 400 registros estudiantiles procesados.
* `/notebooks`: Cuaderno Jupyter/Colab (`Fase3_Desercion_ITTL3.ipynb`) con limpieza de datos (Scrub), Análisis Exploratorio (EDA) y entrenamiento del modelo.
* `/src`: Scripts auxiliares en Python (`generar_datos.py`) para reproducibilidad y preparación de datos.
* `/dashboard`: Aplicación web interactiva construida en **Streamlit** (`app.py`) y dependencias (`requirements.txt`).

## ⚙️ Tecnologías y Modelo Utilizado
* **Lenguaje:** Python 3.10+
* **Manipulación y EDA:** `pandas`, `numpy`, `matplotlib`, `seaborn`
* **Modelado:** `scikit-learn` (`DecisionTreeClassifier`, `max_depth=4`, `random_state=42`) — *Accuracy: 91.25% | F1-Score: 83.72%*
* **Visualización Ejecutiva:** `Streamlit` y `Plotly`

## 🚀 Cómo ejecutar el Dashboard localmente
```bash
cd dashboard
pip install -r requirements.txt
streamlit run app.py
