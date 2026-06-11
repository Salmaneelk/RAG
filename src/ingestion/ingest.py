from pathlib import Path

from src.loaders.pdf_loader import load_pdf_file
from src.loaders.text_loader import load_text_file


def ingest_documents(data_dir :str):
    documents = []
    for file in Path(data_dir).iterdir():
        if not file.is_file():
            continue
        match file.suffix.lower():

            case ".txt":
                text = load_text_file(file)

            # case ".md":
            #     text = load_markdown_file(file)
            #
            # case ".html":
            #     text = load_html_file(file)

            case ".pdf":
                text = load_pdf_file(file)

            case _:
                print(f"Skipping unsupported file: {file.name}")
                continue

        documents.append(
            {
                "file_name": file.name,
                "file_type": file.suffix,
                "content": text,
            }
        )

        return documents

