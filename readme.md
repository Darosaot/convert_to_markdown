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


## About MarkItDown

MarkItDown is a lightweight Python utility developed by Microsoft for converting various files to Markdown for use with LLMs and related text analysis pipelines. It preserves important document structure (headings, lists, tables, links, etc.) while maintaining a format that's optimized for LLM consumption.

For more information, visit the [MarkItDown GitHub repository](https://github.com/microsoft/markitdown).
