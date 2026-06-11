import json
from pathlib import Path


def save_chunks(chunks, output_path: str = "data/chunks/chunks.jsonl"):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
