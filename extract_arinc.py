import os
import pdfplumber
import camelot
from pathlib import Path

PDF_PATH = "/home/inna/workspace/Claude_projects/ARINC424-15/Arinc424-15.pdf"
OUTPUT_DIR = "./arinc_extracted"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Текст по страницам ---
with pdfplumber.open(PDF_PATH) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        if text:
            with open(os.path.join(OUTPUT_DIR, f"page_{page_num:03d}_text.md"), "w", encoding="utf-8") as f:
                f.write(f"# Страница {page_num}\n\n{text}\n")

# --- Таблицы (Camelot) ---
# pages="all" — ищет таблицы на всех страницах
tables = camelot.read_pdf(PDF_PATH, pages="all", flavor="lattice")  # lattice лучше для сеточных таблиц

for i, table in enumerate(tables, start=0):
    # Сохраняем как Markdown-таблицу
    md_table = table.df.to_markdown(index=False)
    with open(os.path.join(OUTPUT_DIR, f"table_{i:03d}.md"), "w", encoding="utf-8") as f:
        f.write(f"# Таблица {i}\n\n{md_table}\n")

print(f"Готово. Файлы в папке: {OUTPUT_DIR}")
