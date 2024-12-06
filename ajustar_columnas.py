import pandas as pd

# Ruta al archivo de actualización de pagos
file_path = "gestion_pagos/pagos/data/ACTUALIZACION_DE_PAGOS.xlsx"

# Cargar el archivo Excel
df_pagos = pd.read_excel(file_path)

# Mostrar las columnas del DataFrame
print("Columnas actuales del archivo de actualización de pagos:")
print(df_pagos.columns.tolist())

# Columnas esperadas
expected_columns = ['sociedad', 'material', 'item', 'nuevo_precio_2024', 'desvio_en_porcentaje', 'area']

# Verificar y ajustar columnas
for col in expected_columns:
    if col not in df_pagos.columns:
        print(f"Columna '{col}' no encontrada. Creando columna con valores predeterminados.")
        if col == 'desvio_en_porcentaje':
            df_pagos[col] = 0
        else:
            df_pagos[col] = ''

# Guardar el archivo ajustado
df_pagos.to_excel(file_path, index=False)
print(f"Archivo ajustado guardado en {file_path}")
