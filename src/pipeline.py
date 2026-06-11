from data.chunks.save_chunks import save_chunks
from src.chunking.chunker import fixed_chunk, recursive_chunk, semantic_chunk
from src.ingestion.ingest import ingest_documents
from src.processing.text_cleaner import clean_text


def run_pipeline(data_dir : str, strategy : str = "fixed"):
    # 1- load files and clean them
    documents = ingest_documents(data_dir)
    all_chunks = []

    for d in documents:

        # 2- split each documents into chunks
        if strategy == "fixed":
            chunks = fixed_chunk(d['content'])
        elif strategy == "recursive":
            chunks = recursive_chunk(d['content'])
        elif strategy == "semantic":
            chunks = semantic_chunk(d['content'])
        else:
            raise ValueError(f"Unknown chunking strategy: {strategy}")


        # 3- add metadata to each chunk
        for i,chunk in enumerate(chunks):
            chunk = clean_text(chunk)
            all_chunks.append({
                "file_name": d['file_name'],
                "file_type": d['file_type'],
                "chunk_id":i,
                "chunk_length": len(chunk),
                "content": chunk
            })
        save_chunks(all_chunks)
    return all_chunks

