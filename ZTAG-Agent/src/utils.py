import os
from docling.document_converter import DocumentConverter

def extract_nsa_rules(pdf_path):
    cache_path = pdf_path.replace(".pdf", ".md")
    
    # Si ya lo procesamos, devolvemos el cache instantaneo
    if os.path.exists(cache_path):
        with open(cache_path, "r", encoding='utf-8') as f:
            return f.read()
    
    print(f"[*] Primera vez: Procesando manual completo con IA (esto tomara un momento)...")
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    content = result.document.export_to_markdown()
    
    # Guardamos para la proxima vez
    with open(cache_path, "w", encoding='utf-8') as f:
        f.write(content)
        
    return content