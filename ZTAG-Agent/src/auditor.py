import os
import sys

# Esto permite importar utils tanto si corres el script solo como desde el main
try:
    from src.utils import extract_nsa_rules
except ImportError:
    from utils import extract_nsa_rules

def analyze_code_with_nsa(code_path, manual_path):
    print(f"[*] Iniciando Auditoria de Seguridad ZTAG...")
    
    nsa_context = {
        "1.4.1": "Privileged Access Management - Prohibe credenciales hardcodeadas.",
        "2.4.1": "Deny by Default - Requiere verificacion estricta de cada flujo.",
        "7.3.1": "Analytics Tools - Exige logs de cada acceso a datos."
    }

    with open(code_path, "r", encoding='utf-8') as f:
        code_content = f.read()

    report = ["### REPORTE DE CUMPLIMIENTO ZERO TRUST (NSA v1.0) ###\n"]
    
    if "C:/" in code_content or "DB_PATH" in code_content or "password" in code_content.lower():
        report.append(f"[FALLO] Actividad {nsa_context['1.4.1']}")
        report.append("   - Causa: Ruta de sistema o credenciales expuestas en texto plano.")
    
    if "f\"SELECT" in code_content or "f'SELECT" in code_content:
        report.append(f"[FALLO] Actividad {nsa_context['2.4.1']}")
        report.append("   - Causa: Confianza implicita en entrada de usuario (SQL Injection).")

    os.makedirs("results", exist_ok=True)
    result_path = "results/audit_report.txt"
    
    with open(result_path, "w", encoding='utf-8') as f:
        f.write("\n".join(report))
    
    print(f"[+] Auditoria finalizada. Informe guardado en: {result_path}")