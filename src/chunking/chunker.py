# first type : fixed size chunking

def fixed_chunk(text: str, chunk_size: int = 500, overlap: int = 100) :
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = start + chunk_size
        chunk_text = text[start:end]
        chunks.append(chunk_text)
        start = end - overlap
    return chunks