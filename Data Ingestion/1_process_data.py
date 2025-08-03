import json
from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.title import chunk_by_title
from unstructured.documents.elements import PageBreak

# --- CONFIGURATION ---
SOURCE_FILE_PATH = "support-ticket-system.pdf"
OUTPUT_FILE_PATH = "data.json"

print(f"Starting data processing for: {SOURCE_FILE_PATH}")

# Partition the PDF, inferring table structure
print("Step 1: Partitioning the PDF...")
elements = partition_pdf(
    filename=SOURCE_FILE_PATH,
    strategy="hi_res",
    infer_table_structure=True
)

# Filter out page breaks
print("Step 2: Filtering out page breaks...")
filtered_elements = [el for el in elements if not isinstance(el, PageBreak)]

# Chunk the filtered elements by title
print("Step 3: Chunking elements by title...")
chunks = chunk_by_title(
    filtered_elements,
    max_characters=1000,
    new_after_n_chars=800,
    combine_text_under_n_chars=500
)

# Format chunks and add metadata
print("Step 4: Formatting chunks and adding metadata...")
output_data = []
for i, chunk in enumerate(chunks):
    output_data.append({
        "source": SOURCE_FILE_PATH,
        "content": str(chunk),
        "chunk_id": f"chunk_{i}",
        "page_number": chunk.metadata.page_number
    })

# Save the processed chunks to a JSON file
with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=2, ensure_ascii=False)

print(f"\nSUCCESS: Saved {len(output_data)} processed chunks to {OUTPUT_FILE_PATH}")