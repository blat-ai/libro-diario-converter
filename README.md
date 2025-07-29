# Consolidador de Excel Formato A3

Esta aplicación consolida archivos Excel en formato A3 extrayendo todas las filas con datos de "Fecha" y "Asiento" y combinándolas en una hoja maestra.

## Índice

- [Usuario](#usuario)
  - [¿Qué hace la herramienta?](#qué-hace-la-herramienta)
  - [Instalación en Windows Desktop](#instalación-en-windows-desktop)
- [Desenvolupador](#desenvolupador)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Configuración de desarrollo en Ubuntu](#configuración-de-desarrollo-en-ubuntu)
  - [Generar ejecutable para Windows desde Ubuntu](#generar-ejecutable-para-windows-desde-ubuntu)
  - [Ejecutar tests](#ejecutar-tests)
  - [Desarrollo con Docker](#desarrollo-con-docker)
  - [Tecnologías utilizadas](#tecnologías-utilizadas)
  - [Cómo funciona](#cómo-funciona)

## Usuario

### ¿Qué hace la herramienta?

La herramienta procesa libros diarios en formato A3 que tienen las cuentas contables separadas en hojas por cada mes. Consolida todos los datos contables en una sola hoja "MASTER" para facilitar el análisis y procesamiento.

**Características principales:**
- Interfaz web fácil de usar con Streamlit
- Procesa todas las hojas del archivo Excel automáticamente
- Preserva las hojas originales en el archivo de salida
- Crea una hoja "MASTER" con todos los datos consolidados
- Añade seguimiento del origen de cada fila (qué hoja)

### Instalación en Windows Desktop

1. **Descargar el ejecutable:**
   - Descarga el archivo `.exe` de la aplicación desde los releases del proyecto
   - Guarda el archivo en una carpeta de tu elección

2. **Ejecutar la aplicación:**
   - Haz doble clic en el archivo `.exe`
   - Se abrirá automáticamente tu navegador web con la interfaz de la aplicación
   - Si no se abre automáticamente, ve a `http://localhost:8501`

3. **Usar la herramienta:**
   - En la App verás qué formato tiene que tener el documento
   - Selecciona tu archivo Excel
   - Haz clic en "Procesar Archivo"
   - Descarga el archivo consolidado

4. **Cerrar la aplicación:**
   - Usa el botón "Cerrar Aplicación" en la interfaz web
   - O cierra la ventana del navegador y la terminal

## Desenvolupador

### Estructura del proyecto

```
libro-diario-converter/
├── app/
│   ├── consolidator.py      # Lógica principal de consolidación
│   ├── streamlit_app.py     # Interfaz web con Streamlit
│   └── __init__.py
├── tests/
│   ├── unit/                # Tests unitarios
│   ├── integration/         # Tests de integración
│   └── data/                # Datos de prueba
├── build/                   # Archivos de construcción PyInstaller
├── dist/                    # Ejecutables generados
├── launcher.py              # Lanzador para el ejecutable
├── streamlit_app.spec       # Configuración PyInstaller
├── requirements.txt         # Dependencias Python
├── run_dashboard.sh         # Script para ejecutar en desarrollo
└── Dockerfile               # Containerización
```

### Configuración de desarrollo en Ubuntu

1. **Prerrequisitos del sistema:**
```bash
# Actualizar el sistema
sudo apt update && sudo apt upgrade -y

# Instalar Python y herramientas de desarrollo
sudo apt install python3 python3-pip python3-venv git -y

# Verificar instalación
python3 --version
pip3 --version
```

2. **Clonar el repositorio:**
```bash
git clone <repository-url>
cd libro-diario-converter
```

3. **Crear y activar entorno virtual:**
```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

5. **Ejecutar en modo desarrollo:**
```bash
# Ejecutar la aplicación
python launcher.py
```

### Generar ejecutable para Windows desde Ubuntu

```bash
# Instalar PyInstaller si no está incluido
pip install pyinstaller

# Generar ejecutable Windows
pyinstaller streamlit_app.spec

# El ejecutable se generará en dist/streamlit_app.exe
```

### Ejecutar tests

```bash
# Tests unitarios
python -m pytest tests/unit/ -v

# Tests de integración
python -m pytest tests/integration/ -v

# Todos los tests con cobertura
python -m pytest tests/ --cov=app --cov-report=html
```

### Desarrollo con Docker

```bash
# Construir imagen
docker build -t libro-diario-converter .

# Ejecutar contenedor
docker run -p 8501:8501 libro-diario-converter
```

### Tecnologías utilizadas

- **Python 3.7+**
- **Streamlit** - Interfaz web
- **pandas** - Procesamiento de datos
- **openpyxl** - Manipulación de archivos Excel
- **PyInstaller** - Generación de ejecutables
- **pytest** - Framework de testing

### Cómo funciona

1. La aplicación lee cada hoja del archivo Excel de entrada
2. Identifica la fila de encabezado que contiene las columnas "Fecha" y "Asiento"
3. Extrae todas las filas que tienen valores en ambas columnas
4. Combina todas las filas válidas de todas las hojas en una hoja maestra
5. Crea un archivo de salida con:
   - Todas las hojas originales (preservadas tal como están)
   - Una nueva hoja "MASTER" con los datos consolidados
   - Seguimiento del origen de cada fila consolidada