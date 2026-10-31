import os
from pathlib import Path

INPUT_DIR = "arinc_extracted"
OUTPUT_DIR = "arinc_chunks"
CHUNK_SIZE_WORDS = 600
OVERLAP_WORDS = 80

os.makedirs(OUTPUT_DIR, exist_ok=True)

def split_into_chunks(text, chunk_size, overlap):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk_words = words[i:i + chunk_size]
        chunk = " ".join(chunk_words)
        if chunk.strip():
            chunks.append(chunk)
    return chunks

for file in Path(INPUT_DIR).glob("page_*.md"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Убираем заголовок страницы, оставляем только текст
    lines = content.splitlines()
    if lines and lines[0].startswith("# Страница"):
        text_only = "\n".join(lines[1:]).strip()
    else:
        text_only = content

    chunks = split_into_chunks(text_only, CHUNK_SIZE_WORDS, OVERLAP_WORDS)

    for idx, chunk in enumerate(chunks):
        out_name = file.stem.replace("page_", f"chunk_") + f"_{idx:03d}.md"
        with open(os.path.join(OUTPUT_DIR, out_name), "w", encoding="utf-8") as f:
            f.write(chunk)

print(f"Чанки сохранены в: {OUTPUT_DIR}")
