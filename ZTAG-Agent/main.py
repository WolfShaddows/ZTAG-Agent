import os
from src.auditor import analyze_code_with_nsa
from src.bob_fixer import generate_remediation

def run_full_demo():
    print("====================================================")
    print("   ZTAG: ZERO-TRUST AGENTIC GUARD - NSA EDITION     ")
    print("====================================================\n")
    
    pdf_nsa = "knowledge/1769475823091.pdf"
    target_code = "tests/legacy_app.py"
    
    print("[PASO 1] El Auditor esta procesando el manual de la NSA...")
    analyze_code_with_nsa(target_code, pdf_nsa)
    
    print("\n[PASO 2] IBM Bob recibe el reporte y genera el parche...")
    generate_remediation(target_code)
    
    print("\n====================================================")
    print("DEMO FINALIZADA: Revisa la carpeta 'results/'")
    print("====================================================")

if __name__ == "__main__":
    run_full_demo()