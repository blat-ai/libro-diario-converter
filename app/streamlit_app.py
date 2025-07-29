import streamlit as st
from pathlib import Path
import io
import os
import sys
from app.consolidator import ExcelConsolidator


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller bundle."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    # Handle favicon with fallback
    favicon_path = resource_path("assets/blat_favicon.png")
    try:
        if os.path.exists(favicon_path):
            page_icon = favicon_path
        else:
            page_icon = "🅱️"  # Fallback emoji
    except:
        page_icon = "🅱️"  # Fallback emoji
    
    st.set_page_config(
        page_title="Consolidador de Excel Formato A3", 
        page_icon=page_icon, 
        layout="wide"
    )
    
    # Custom CSS for black theme with blue interactive elements
    st.markdown("""
    <style>
    /* Main app background */
    .stApp {
        background-color: rgb(22, 22, 24);
        color: white;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: rgb(22, 22, 24);
    }
    
    /* Main content area */
    .main .block-container {
        background-color: rgb(22, 22, 24);
        color: white;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    
    /* Text and markdown */
    .stMarkdown, .stMarkdown p, .stText {
        color: white !important;
    }
    
    /* Buttons - Blue theme */
    .stButton > button {
        background-color: rgb(0, 153, 255) !important;
        color: white !important;
        border: 1px solid rgb(0, 153, 255) !important;
        border-radius: 8px;
    }
    
    .stButton > button:hover {
        background-color: rgb(0, 133, 235) !important;
        border: 1px solid rgb(0, 133, 235) !important;
    }
    
    .stButton > button:active {
        background-color: rgb(0, 113, 215) !important;
    }
    
    /* Download button */
    .stDownloadButton > button {
        background-color: rgb(0, 153, 255) !important;
        color: white !important;
        border: 1px solid rgb(0, 153, 255) !important;
    }
    
    .stDownloadButton > button:hover {
        background-color: rgb(0, 133, 235) !important;
    }
    
    /* File uploader */
    .stFileUploader > div > div {
        background-color: rgb(40, 40, 42) !important;
        border: 2px dashed rgb(0, 153, 255) !important;
        color: white !important;
    }
    
    /* Success/Info/Error messages */
    .stSuccess {
        background-color: rgba(0, 153, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgb(0, 153, 255) !important;
    }
    
    .stInfo {
        background-color: rgba(0, 153, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgb(0, 153, 255) !important;
    }
    
    .stError {
        background-color: rgba(255, 0, 0, 0.1) !important;
        color: white !important;
        border: 1px solid rgb(255, 100, 100) !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: rgb(40, 40, 42) !important;
        color: white !important;
        border: 1px solid rgb(60, 60, 62) !important;
    }
    
    .streamlit-expanderContent {
        background-color: rgb(30, 30, 32) !important;
        color: white !important;
        border: 1px solid rgb(60, 60, 62) !important;
    }
    
    /* Dataframe */
    .stDataFrame {
        background-color: rgb(30, 30, 32) !important;
        color: white !important;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background-color: rgb(0, 153, 255) !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: rgb(0, 153, 255) !important;
    }
    
    /* Columns and containers */
    .element-container {
        background-color: transparent !important;
    }
    
    /* Horizontal rule */
    hr {
        border-color: rgb(60, 60, 62) !important;
    }
    
    /* Input fields if any */
    .stTextInput > div > div > input {
        background-color: rgb(40, 40, 42) !important;
        color: white !important;
        border: 1px solid rgb(60, 60, 62) !important;
    }
    
    /* Select boxes if any */
    .stSelectbox > div > div > select {
        background-color: rgb(40, 40, 42) !important;
        color: white !important;
        border: 1px solid rgb(60, 60, 62) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header with Blat branding
    col1, col2 = st.columns([1, 8])
    with col1:
        logo_path = resource_path("assets/blat_logo.png")
        try:
            if os.path.exists(logo_path):
                st.image(logo_path, width=80)
            else:
                st.markdown("""
                <div style="
                    width: 80px; 
                    height: 80px; 
                    background-color: #0099ff; 
                    border-radius: 8px; 
                    display: flex; 
                    align-items: center; 
                    justify-content: center; 
                    font-size: 32px; 
                    font-weight: bold; 
                    color: white;
                ">🅱️</div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown("""
            <div style="
                width: 80px; 
                height: 80px; 
                background-color: #0099ff; 
                border-radius: 8px; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                font-size: 32px; 
                font-weight: bold; 
                color: white;
            ">🅱️</div>
            """, unsafe_allow_html=True)
    
    st.title("Consolidador de Excel Formato A3")
    st.markdown("**Esta aplicación solo acepta libro diario con formato A3 que tiene las cuentas contables separadas en sheets por cada mes.**")
    
    st.markdown("---")

    consolidator = ExcelConsolidator()

    # Instructions section (collapsible)
    with st.expander("📋 Instrucciones", expanded=False):
        st.markdown("""
        **Requisitos del archivo:**
        - Solo acepta archivos Excel con formato A3
        - El libro diario debe tener las cuentas contables separadas en sheets por cada mes
        
        **Pasos para procesar:**
        1. **Sube** tu archivo Excel usando el cargador de archivos de abajo
        2. La aplicación procesará todas las hojas y buscará las columnas 'Fecha' y 'Asiento'
        3. Las entradas válidas de todas las hojas se consolidarán en una hoja 'MASTER'
        4. **Descarga** el archivo procesado con los datos consolidados
        
        **Nota**: Las hojas originales se conservan, y se añade una nueva hoja 'MASTER' al principio.
        """)

    # File upload section
    st.subheader("📁 Selección de Archivo")

    uploaded_file = st.file_uploader(
        "Selecciona un archivo Excel (formato A3)",
        type=["xlsx", "xls"],
        help="Selecciona el archivo Excel con formato A3 que contiene el libro diario con cuentas contables separadas por mes",
    )

    if uploaded_file is not None:
        st.success(f"Archivo subido: **{uploaded_file.name}**")

        # Generate output filename
        input_path = Path(uploaded_file.name)
        output_filename = f"{input_path.stem}_consolidated{input_path.suffix}"

        st.info(f"El archivo de salida será: **{output_filename}**")

        # Process button
        if st.button("🚀 Procesar Archivo", type="primary"):
            with st.spinner("Procesando archivo Excel..."):
                try:
                    # Read file bytes
                    file_bytes = uploaded_file.read()

                    # Process the file
                    output_workbook, master_df = consolidator.process_excel_file(
                        file_bytes, uploaded_file.name, progress_callback=st.write
                    )

                    if output_workbook:
                        # Show preview of master data
                        if master_df is not None:
                            st.subheader("Vista Previa de Datos Maestros")
                            st.dataframe(master_df.head(10))
                        # Save to bytes for download
                        output_buffer = io.BytesIO()
                        output_workbook.save(output_buffer)
                        output_buffer.seek(0)

                        st.success("✅ ¡Procesamiento completado exitosamente!")

                        # Download button
                        st.download_button(
                            label="💾 Descargar Archivo Consolidado",
                            data=output_buffer.getvalue(),
                            file_name=output_filename,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        )

                except Exception as e:
                    st.error(f"❌ Ha ocurrido un error: {str(e)}")
    else:
        st.info("👆 Por favor sube un archivo Excel para comenzar")

    # Add footer section with close button
    st.markdown("---")
    
    # Professional close button styling with Edge compatibility
    st.markdown("""
    <style>
    .shutdown-container {
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;
        -ms-flex-pack: center;
        -webkit-justify-content: center;
        justify-content: center;
        -ms-flex-align: center;
        -webkit-align-items: center;
        align-items: center;
        margin: 2rem 0;
    }
    .shutdown-message {
        text-align: center;
        color: #666 !important;
        font-size: 1.1rem;
        margin: 1rem 0;
    }
    .loading-spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid #f3f3f3;
        border-top: 3px solid #ff4757;
        border-radius: 50%;
        -webkit-animation: spin 1s linear infinite;
        -moz-animation: spin 1s linear infinite;
        -ms-animation: spin 1s linear infinite;
        animation: spin 1s linear infinite;
        margin-right: 10px;
        vertical-align: middle;
    }
    @-webkit-keyframes spin {
        0% { -webkit-transform: rotate(0deg); }
        100% { -webkit-transform: rotate(360deg); }
    }
    @-moz-keyframes spin {
        0% { -moz-transform: rotate(0deg); }
        100% { -moz-transform: rotate(360deg); }
    }
    @-ms-keyframes spin {
        0% { -ms-transform: rotate(0deg); }
        100% { -ms-transform: rotate(360deg); }
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Enhanced button styling for Edge compatibility */
    .stButton > button[data-testid="baseButton-secondary"] {
        background-color: #dc3545 !important;
        color: white !important;
        border: 2px solid #dc3545 !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        -webkit-transition: all 0.3s ease !important;
        -moz-transition: all 0.3s ease !important;
        -ms-transition: all 0.3s ease !important;
    }
    
    .stButton > button[data-testid="baseButton-secondary"]:hover {
        background-color: #c82333 !important;
        border-color: #bd2130 !important;
        transform: translateY(-2px) !important;
        -webkit-transform: translateY(-2px) !important;
        -moz-transform: translateY(-2px) !important;
        -ms-transform: translateY(-2px) !important;
        box-shadow: 0 4px 8px rgba(220, 53, 69, 0.3) !important;
    }
    
    .stButton > button[data-testid="baseButton-secondary"]:active {
        background-color: #bd2130 !important;
        transform: translateY(0px) !important;
        -webkit-transform: translateY(0px) !important;
        -moz-transform: translateY(0px) !important;
        -ms-transform: translateY(0px) !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔴 Cerrar Aplicación", 
                    help="Cierra completamente la aplicación",
                    key="shutdown_btn",
                    use_container_width=True,
                    type="secondary"):
            st.markdown('''
            <div class="shutdown-message">
                <div class="loading-spinner"></div>
                Cerrando aplicación...
            </div>
            ''', unsafe_allow_html=True)
            import time
            time.sleep(2)
            # Force exit the entire Python process including launcher
            import signal
            os.kill(os.getpid(), signal.SIGTERM)


if __name__ == "__main__":
    main()
