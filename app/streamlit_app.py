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
    
    # Header with Blat branding
    col1, col2 = st.columns([1, 8])
    with col1:
        logo_path = resource_path("assets/blat_logo.png")
        try:
            if os.path.exists(logo_path):
                st.image(logo_path, width=80)
            else:
                st.write("🅱️")  # Simple fallback
        except Exception as e:
            st.write("🅱️")  # Simple fallback
    
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
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔴 Cerrar Aplicación", 
                    help="Cierra completamente la aplicación",
                    key="shutdown_btn",
                    use_container_width=True,
                    type="secondary"):
            st.success("Cerrando aplicación...")
            import time
            time.sleep(2)
            # Force exit the entire Python process including launcher
            import signal
            os.kill(os.getpid(), signal.SIGTERM)


if __name__ == "__main__":
    main()
