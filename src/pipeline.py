from src.chunking.chunker import fixed_chunk
from src.ingestion.ingest import ingest_documents


def run_pipeline(data_dir : str):
    # 1- load files and clean them
    documents = ingest_documents(data_dir)
    all_chunks = []

    for d in documents:

        # 2- split each documents into chunks
        chunks = fixed_chunk(d['content'], chunk_size=500, overlap=100)

        # 3- add metadata to each chunk
        for i,chunk in enumerate(chunks):
            all_chunks.append({
                "file_name": d['file_name'],
                "file_type": d['file_type'],
                "chunk_id":i,
                "chunk_length": len(chunk),
                "content": chunk
            })
        return all_chunks