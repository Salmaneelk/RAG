from pathlib import Path
def load_pdf_file(file_path : Path) -> str:
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text