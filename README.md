# Cálculo del Límite Elástico (Yield Strength)

Este proyecto calcula el límite elástico de un material utilizando datos de entrada y genera gráficos como salida.

## Estructura del Proyecto

El proyecto sigue la siguiente estructura de directorios y archivos:

```
yield-strength-calculus/
├── data/                  # Carpeta para almacenar los datos de entrada
│   ├── example_data.xlsx  # Ejemplo de archivo de datos
├── output/                # Carpeta donde se guardan los resultados (gráficos generados)
│   └── plot.png           # Gráfico generado por el programa
├── src/                   # Código fuente del proyecto
│   ├── config.py          # Configuración del proyecto
│   └── data_manager.py    # Módulo para manejar los datos
├── main.py                # Archivo principal para ejecutar el proyecto
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación del proyecto
```

## Datos de entrada

Añade los archivos con tus datos en la carpeta `data/`. La carpeta `data/` debe contener archivos en formato `.xlsx` con los datos necesarios para el cálculo, asegúrate de manejar el siguiente formato en tus archivios `.xlsx`.

| strain | stress |
|--------|--------|
| 0.0000 | 0.0    |
| 0.0010 | 50.0   |
| 0.0020 | 100.0  |
| 0.0030 | 150.0  |
| 0.0040 | 200.0  |
| 0.0050 | 250.0  |

Guarda este archivo en la carpeta `data/` como `example_data.xlsx` para probar el proyecto.

## Requisitos

- Python 3.13 o superior.
- Las dependencias listadas en `requirements.txt`.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Mauriciocr207/yield-strength
   cd yield-strength-calculus
   ```

2. Crea un entorno virtual:
   ```bash
   python -m venv env
   ```

3. Activa el entorno virtual en Windows:
   ```bash
   .\env\Scripts\activate
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Run
```bash
python main.py
``` 

## `output/`
Una vez corras el programa podrás ver el resultado en las imagenes generadas en la carpeta `output/`. Se generará una imagen por cada archivo en la carpeta `data/`.