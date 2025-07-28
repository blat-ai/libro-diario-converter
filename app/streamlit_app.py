import streamlit as st
from pathlib import Path
import io
from app.consolidator import ExcelConsolidator


def main():
    st.set_page_config(
        page_title="Consolidador de Excel Formato A3", page_icon="📊", layout="wide"
    )

    st.title("📊 Consolidador de Excel Formato A3")
    st.markdown("---")

    consolidator = ExcelConsolidator()

    # Instructions section (collapsible)
    with st.expander("📋 Instrucciones", expanded=False):
        st.markdown("""
        1. **Sube** tu archivo Excel usando el cargador de archivos de abajo
        2. La aplicación procesará todas las hojas y buscará las columnas 'Fecha' y 'Asiento'
        3. Las entradas válidas de todas las hojas se consolidarán en una hoja 'MASTER'
        4. **Descarga** el archivo procesado con los datos consolidados
        
        **Nota**: Las hojas originales se conservan, y se añade una nueva hoja 'MASTER' al principio.
        """)

    # File upload section
    st.subheader("📁 Selección de Archivo")

    uploaded_file = st.file_uploader(
        "Selecciona un archivo Excel",
        type=["xlsx", "xls"],
        help="Selecciona el archivo Excel que quieres consolidar",
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


if __name__ == "__main__":
    main()
