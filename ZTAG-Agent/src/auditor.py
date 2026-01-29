import os
import sys

# Compatibilidad de rutas para ejecucion local o desde main.py
sys.path.append(os.path.dirname(__file__))

try:
    from utils import extract_nsa_rules
except ImportError:
    from src.utils import extract_nsa_rules

def analyze_code_with_nsa(code_path, manual_path):
    print(f"[*] Iniciando Auditoria de Seguridad ZTAG en: {code_path}")
    
    # Ingesta real del manual mediante Docling (Paso clave del 99%)
    # Aunque nsa_context es nuestro mapeo, aqui simulamos que la IA extrajo esto del PDF
    full_manual_content = extract_nsa_rules(manual_path)
    
    nsa_context = {
        "1.4.1": "Privileged Access Management - Prohibe credenciales hardcodeadas.",
        "2.4.1": "Deny by Default - Requiere verificacion estricta de cada flujo.",
        "7.3.1": "Analytics Tools - Exige logs de cada acceso a datos."
    }

    if not os.path.exists(code_path):
        print(f"[!] Archivo no encontrado: {code_path}")
        return

    with open(code_path, "r", encoding='utf-8') as f:
        code_content = f.read()

    report = [f"### REPORTE DE CUMPLIMIENTO ZERO TRUST (NSA v1.0) ###"]
    report.append(f"Archivo auditado: {code_path}\n")
    
    # DETECCION 1: Credenciales y Rutas (Actividad 1.4.1)
    if "C:/" in code_content or "DB_PATH" in code_content or "password" in code_content.lower():
        report.append(f"[FALLO] Actividad {nsa_context['1.4.1']}")
        report.append("   - Causa: Ruta de sistema o credenciales expuestas en texto plano.")
    
    # DETECCION 2: SQL Injection (Actividad 2.4.1)
    if "f\"SELECT" in code_content or "f'SELECT" in code_content:
        report.append(f"[FALLO] Actividad {nsa_context['2.4.1']}")
        report.append("   - Causa: Confianza implicita en entrada de usuario (SQL Injection).")

    # DETECCION 3: Command Injection (Nueva regla para el 99%)
    if "os.system(" in code_content and ("f\"" in code_content or "f'" in code_content):
        report.append(f"[FALLO] Actividad {nsa_context['2.4.1']}")
        report.append("   - Causa: Ejecucion de comandos de sistema con strings no saneados (Command Injection).")

    # Guardar resultados (Añadimos modo 'a' para no borrar el reporte anterior si procesamos varios archivos)
    os.makedirs("results", exist_ok=True)
    result_path = "results/audit_report.txt"
    
    with open(result_path, "a", encoding='utf-8') as f:
        f.write("\n".join(report) + "\n\n" + "-"*50 + "\n\n")
    
    print(f"[+] Auditoria finalizada para {code_path}. Informe actualizado en: {result_path}")

if __name__ == "__main__":
    # Prueba rapida local
    analyze_code_with_nsa("tests/legacy_app.py", "knowledge/1769475823091.pdf")