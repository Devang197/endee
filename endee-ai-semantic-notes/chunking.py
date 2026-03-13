def chunk_text_streaming(pages, chunk_size=120, overlap=20):
    chunks = []

    for page_text in pages:
        start = 0
        while start < len(page_text):
            end = start + chunk_size
            chunks.append(page_text[start:end])
            start = end - overlap

    return chunks