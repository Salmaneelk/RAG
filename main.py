"""RAG pipeline entry point."""
from pathlib import Path

from src.chunking.chunker import fixed_chunk
from src.ingestion.ingest import ingest_documents
from src.loaders.text_loader import load_text_file
from src.loaders.pdf_loader import load_pdf_file
from src.pipeline import run_pipeline


def main() -> None:
    documents = ingest_documents("data/raw")

    for document in documents:
        # print(f"File name: {document['file_name']}")
        # print(f"File type: {document['file_type']}")
        # print(f"length :{len(document['content'])}")
        # print('-' * 40)
        print(document['content'][:200])
        text = document['content'][:1000]  # from a loaded document
        chunks = fixed_chunk(text, chunk_size=200, overlap=50)
        for i, c in enumerate(chunks):
            print(f"Chunk {i + 1}: {len(c)} characters")


if __name__ == "__main__":
    chunks = run_pipeline("data/raw")
    print(f"total Chunks: {len(chunks)}")
    print(chunks[0])
