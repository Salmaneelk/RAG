#3 tpyes of chunking
import re

from sklearn.feature_extraction.text import TfidfVectorizer


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

#second type : recursive
def recursive_chunk(text: str, chunk_size: int = 500, overlap: int = 100) :
    """
    Split text by headings (lines starting with # or ALL CAPS),
    then recursively split large sections until under chunk_size.
    """
    lines = text.split("\n")
    sections = []
    current= ""
    for line in lines:
        if line.strip().startswith("#") or line.isupper():
            if current :
                sections.append(current.strip())
                current = ""
            current += line
    if current :
        sections.append(current.strip())
    # Now Splitting large sections recursively
    final_chunks = []
    for section in sections:
        if len(section) <= chunk_size :
            final_chunks.append(section)
        else :
            final_chunks.extend(final_chunks(section,chunk_size,overlap))
    return final_chunks


#3rd type : Semantic
def split_into_units(text: str) :
    units = re.split(r"\n{2,}|\n(?=\S)", text)
    return [u.strip() for u in units if len(u.strip()) > 20]


def semantic_chunk(
    text: str,
    chunk_size: int = 1200,
    similarity_threshold: float = 0.7
) :

    units = split_into_units(text)
    chunks = []

    if not units:
        return chunks

    vectorizer = TfidfVectorizer().fit(units)
    vectors = vectorizer.transform(units)

    current_chunk = units[0]

    for i in range(1, len(units)):
        next_unit = units[i]

        would_be_too_long = len(current_chunk) + len(next_unit) > chunk_size

        if would_be_too_long:
            chunks.append(current_chunk.strip())
            current_chunk = next_unit
            continue

        chunk_vector = vectorizer.transform([current_chunk])
        sim = (vectors[i] @ chunk_vector.T).toarray()[0][0]

        if sim < similarity_threshold:
            chunks.append(current_chunk.strip())
            current_chunk = next_unit
        else:
            current_chunk += " " + next_unit

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


