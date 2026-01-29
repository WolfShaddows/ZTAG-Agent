import os
from src.auditor import analyze_code_with_nsa
from src.bob_fixer import generate_remediation

def run_full_demo():
    print("====================================================")
    print("   ZTAG: ZERO-TRUST AGENTIC GUARD - NSA EDITION     ")
    print("====================================================\n")
    
    # Configuracion de rutas
    pdf_nsa = "knowledge/1769475823091.pdf"
    # Lista de archivos a auditar para demostrar escalabilidad
    target_codes = ["tests/legacy_app.py", "tests/legacy_app_v2.py"]
    
    # Limpieza previa de reportes para una demo limpia
    report_path = "results/audit_report.txt"
    if os.path.exists(report_path):
        os.remove(report_path)

    # Ciclo de Gobernanza Automatizada
    for code_file in target_codes:
        if not os.path.exists(code_file):
            print(f"[!] Saltando {code_file}: No encontrado.")
            continue

        print(f"\n>>> PROCESANDO: {code_file}")
        
        # PASO 1: Auditoria basada en normativa NSA
        print("[PASO 1] El Auditor esta consultando el manual y analizando riesgos...")
        analyze_code_with_nsa(code_file, pdf_nsa)
        
        # PASO 2: Remediacion Agentic con IBM Bob
        print("[PASO 2] IBM Bob aplicando parches de seguridad Shift-Left...")
        generate_remediation(code_file)
    
    print("\n====================================================")
    print("DEMO COMPLETADA: Se han auditado y reparado todos los archivos.")
    print("Revisa 'results/audit_report.txt' para el historial completo.")
    print("====================================================")

if __name__ == "__main__":
    run_full_demo()