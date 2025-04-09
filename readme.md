# MarkItDown Converter

A Streamlit application that converts various file formats to Markdown using Microsoft's MarkItDown library.

## Features

This application supports all the file formats that Microsoft's MarkItDown supports:

- PDF (.pdf)
- PowerPoint (.pptx, .ppt)
- Word (.docx, .doc)
- Excel (.xlsx, .xls)
- Images (EXIF metadata and OCR)
- Audio (EXIF metadata and speech transcription)
- HTML (.html, .htm)
- Text-based formats (CSV, JSON, XML)
- ZIP files (iterates over contents)
- YouTube URLs
- EPubs
- And more!

## Installation

### Easy Installation (Windows)

1. Run the `install.bat` script by double-clicking it
2. Follow the on-screen instructions

### Easy Installation (Mac/Linux)

1. Make the script executable: `chmod +x install.sh`
2. Run the script: `./install.sh`
3. Follow the on-screen instructions

### Manual Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install --upgrade pip
   pip install 'markitdown[all]'
   pip install streamlit pandas openpyxl
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Streamlit app:
   ```bash
   streamlit run full-markdown-converter.py
   ```
3. Open your web browser to the provided URL (typically http://localhost:8501)

## Troubleshooting

### DLL Issues on Windows

If you encounter DLL loading errors like:
```
ImportError: DLL load failed while importing onnxruntime_pybind11_state
```

Try these solutions:

1. **Install Visual C++ Redistributable**: Download and install the latest [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)

2. **Try a different Python version**: MarkItDown may work better with Python 3.8 or 3.9
   ```bash
   # Create a new environment with Python 3.9
   python3.9 -m venv venv_py39
   venv_py39\Scripts\activate
   # Then follow installation steps
   ```

3. **Use Conda**: Conda manages binary dependencies better than pip
   ```bash
   conda create -n markitdown python=3.9
   conda activate markitdown
   pip install 'markitdown[all]'
   pip install streamlit pandas openpyxl
   ```

### Missing Specific Format Support

If you have trouble with specific file formats, you can install their dependencies explicitly:

```bash
# For Word documents
pip install 'markitdown[docx]'

# For PDFs
pip install 'markitdown[pdf]'

# For PowerPoint
pip install 'markitdown[pptx]'

# For all formats
pip install 'markitdown[all]'
```

### Command-Line Usage

You can also use MarkItDown directly from the command line:

```bash
# Basic usage
markitdown path-to-file.pdf > document.md

# Specify output file
markitdown path-to-file.pdf -o document.md

# Enable plugins
markitdown --use-plugins path-to-file.pdf
```

## About MarkItDown

MarkItDown is a lightweight Python utility developed by Microsoft for converting various files to Markdown for use with LLMs and related text analysis pipelines. It preserves important document structure (headings, lists, tables, links, etc.) while maintaining a format that's optimized for LLM consumption.

For more information, visit the [MarkItDown GitHub repository](https://github.com/microsoft/markitdown).
