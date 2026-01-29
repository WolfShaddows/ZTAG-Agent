from docling.document_converter import DocumentConverter

def extract_nsa_rules(pdf_path):
    # Esto procesa TODO el PDF, no importa si tiene 200 paginas
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    return result.document.export_to_markdown()