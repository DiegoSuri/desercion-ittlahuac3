import numpy as np
import pandas as pd

def construir_dataset(seed: int = 42, n: int = 400) -> pd.DataFrame:
    """Genera y limpia el conjunto de datos de deserción escolar del ITTláhuac III."""
    np.random.seed(seed)
    carreras = [
        'Ing. en Ciencia de Datos',
        'Ing. en Sistemas Comp.',
        'Ing. en Gestión Emp.',
        'Ing. Industrial'
    ]

    df_raw = pd.DataFrame({
        'id_estudiante': np.arange(1001, 1001 + n),
        'carrera': np.random.choice(carreras, n, p=[0.30, 0.30, 0.20, 0.20]),
        'semestre': np.random.randint(1, 9, n),
        'promedio_general': np.round(np.random.normal(81, 9, n), 1),
        'materias_reprobadas': np.random.poisson(1.4, n),
        'asistencia_pct': np.round(np.random.normal(84, 11, n), 1),
        'traslado_min': np.random.randint(15, 130, n),
        'beca_transporte_sectei': np.random.choice(['Si', 'No'], n, p=[0.45, 0.55]),
        'trabaja': np.random.choice(['Si', 'No'], n, p=[0.40, 0.60])
    })

    riesgo = (
        (df_raw['materias_reprobadas'] >= 3).astype(int) * 2 +
        (df_raw['promedio_general'] < 75).astype(int) * 2 +
        (df_raw['asistencia_pct'] < 75).astype(int) +
        ((df_raw['traslado_min'] > 80) & (df_raw['beca_transporte_sectei'] == 'No')).astype(int) +
        (df_raw['trabaja'] == 'Si').astype(int)
    )
    df_raw['desercion'] = (riesgo >= 3).astype(int)

    df = df_raw.drop_duplicates().copy()
    df['promedio_general'] = np.clip(df['promedio_general'], 0, 100)
    df['asistencia_pct'] = np.clip(df['asistencia_pct'], 0, 100)
    return df

if __name__ == "__main__":
    dataset = construir_dataset()
    dataset.to_csv("desercion_ittlahuac3.csv", index=False)
    print("Dataset generado exitosamente:", dataset.shape)
