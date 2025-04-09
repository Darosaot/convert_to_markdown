import streamlit as st
import os
import io
import pandas as pd
import tempfile
import subprocess
from pathlib import Path

def main():
    # Set page config
    st.set_page_config(
        page_title="MarkItDown Converter",
        page_icon="📝",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Sidebar
    st.sidebar.title("MarkItDown Converter")
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/25/25462.png", width=100)
    st.sidebar.markdown("---")
    
    # About section in sidebar
    with st.sidebar.expander("About this app", expanded=True):
        st.markdown("""
        This application uses Microsoft's MarkItDown to convert various file formats to Markdown.
        
        Supported formats:
        - PDF (.pdf)
        - PowerPoint (.pptx, .ppt)
        - Word (.docx, .doc)
        - Excel (.xlsx, .xls)
        - Images (EXIF metadata and OCR)
        - Audio (EXIF metadata and speech transcription)
        - HTML (.html, .htm)
        - Text-based formats (CSV, JSON, XML)
        - And more!
        
        Built with Streamlit and powered by Microsoft MarkItDown.
        """)
        
        st.markdown("""
        ### Troubleshooting
        
        If you encounter errors, you might need to install the appropriate dependencies:
        
        ```bash
        pip install 'markitdown[all]'
        ```
        
        For specific file formats, you can install targeted dependencies:
        
        ```bash
        pip install 'markitdown[pdf,docx,pptx]'
        ```
        """)
    
    # Main app area
    st.title("MarkItDown Converter")
    st.markdown("Upload a file to convert it to Markdown format")
    
    # File uploader - all supported formats
    uploaded_file = st.file_uploader("Choose a file", 
                                     type=["pdf", "docx", "doc", "pptx", "ppt", "xlsx", "xls",
                                           "csv", "txt", "json", "xml", "html", "htm",
                                           "jpg", "jpeg", "png", "gif", "wav", "mp3", "epub"])

    # Advanced options
    with st.expander("Advanced Options"):
        use_cli = st.checkbox("Use MarkItDown CLI (recommended for complex documents)", value=True)
        enable_plugins = st.checkbox("Enable plugins", value=False)
        advanced_args = st.text_input("Additional CLI arguments (optional)", 
                                      help="Example: --use-plugins --no-images")
    
    # Process file
    if uploaded_file is not None:
        with st.spinner('Converting your file to Markdown...'):
            # Show file details
            file_details = {
                "Filename": uploaded_file.name,
                "File size": f"{uploaded_file.size / 1024:.2f} KB",
                "File type": uploaded_file.type
            }
            
            st.write("File Details:")
            for key, value in file_details.items():
                st.write(f"- {key}: {value}")
            
            try:
                # Create a temporary file to save the uploaded content
                with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name
                
                # Convert using CLI if selected
                if use_cli:
                    # Build the command
                    cmd = ["markitdown", tmp_file_path]
                    
                    # Add any additional arguments
                    if enable_plugins:
                        cmd.append("--use-plugins")
                    
                    if advanced_args:
                        cmd.extend(advanced_args.split())
                    
                    # Run the command and capture output
                    try:
                        st.text(f"Running command: {' '.join(cmd)}")
                        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                        markdown_content = result.stdout
                    except subprocess.CalledProcessError as e:
                        st.error(f"Command failed with error code {e.returncode}")
                        st.code(e.stderr)
                        markdown_content = f"# Conversion Error\n\nCommand failed with error code {e.returncode}.\n\n```\n{e.stderr}\n```"
                else:
                    # Use Python API if CLI not selected
                    try:
                        from markitdown import MarkItDown
                        
                        # Initialize MarkItDown with options
                        md = MarkItDown(enable_plugins=enable_plugins)
                        
                        # Convert the file
                        with open(tmp_file_path, 'rb') as f:
                            result = md.convert_stream(f, filename=uploaded_file.name)
                        
                        markdown_content = result.text_content
                    except ImportError:
                        st.error("MarkItDown Python library is not properly installed.")
                        markdown_content = "# Import Error\n\nFailed to import MarkItDown. Please install it with:\n\n```\npip install 'markitdown[all]'\n```"
                
                # Remove the temporary file
                os.unlink(tmp_file_path)
                
                # Display the result
                st.subheader("Markdown Output")
                
                # Create tabs for different views
                tab1, tab2 = st.tabs(["Rendered", "Raw Markdown"])
                
                with tab1:
                    st.markdown(markdown_content)
                
                with tab2:
                    st.code(markdown_content, language="markdown")
                
                # Download button for the markdown file
                st.download_button(
                    label="Download Markdown",
                    data=markdown_content,
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}.md",
                    mime="text/markdown",
                )
                
                # If it's a data file, offer a preview
                if uploaded_file.name.endswith(('.xlsx', '.xls', '.csv')):
                    try:
                        st.subheader("Data Preview")
                        if uploaded_file.name.endswith(('.xlsx', '.xls')):
                            df = pd.read_excel(uploaded_file)
                        else:  # CSV
                            df = pd.read_csv(uploaded_file)
                        
                        st.dataframe(df.head(10))
                    except Exception as e:
                        st.warning(f"Could not generate data preview: {str(e)}")
            
            except Exception as e:
                st.error(f"Error during conversion: {str(e)}")
                st.warning("Make sure the file format is supported and the file is not corrupted.")
    
    # Info about CLI
    st.markdown("---")
    with st.expander("Using MarkItDown CLI directly"):
        st.markdown("""
        You can also use MarkItDown directly from the command line:
        
        ```bash
        # Basic usage
        markitdown path-to-file.pdf > document.md
        
        # Specify output file
        markitdown path-to-file.pdf -o document.md
        
        # Enable plugins
        markitdown --use-plugins path-to-file.pdf
        
        # List installed plugins
        markitdown --list-plugins
        ```
        
        For more information, visit the [MarkItDown GitHub repository](https://github.com/microsoft/markitdown).
        """)
    
    # Footer
    st.markdown("---")
    st.caption("© 2025 MarkItDown Converter | Powered by Microsoft MarkItDown")

if __name__ == "__main__":
    main()