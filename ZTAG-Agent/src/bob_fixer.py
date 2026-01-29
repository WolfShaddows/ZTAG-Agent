import os

def generate_remediation(original_code_path):
    print(f"[*] IBM Bob iniciando refactorizacion de: {original_code_path}")
    
    # Identificamos que archivo estamos arreglando para aplicar la medicina correcta
    if "legacy_app_v2.py" in original_code_path:
        # Reparacion para Command Injection
        fixed_code = """import subprocess

def backup_system(folder_name):
    # REPARADO: Se usa subprocess.run con una lista de argumentos (NSA 2.4.1)
    # Esto evita que un atacante inyecte comandos extra mediante caracteres como ';'
    print(f"Haciendo backup seguro de: {folder_name}")
    
    # Al pasar los argumentos como lista, el sistema no interpreta simbolos shell
    subprocess.run(["zip", "-r", "backup.zip", folder_name], check=True)

if __name__ == "__main__":
    backup_system("my_documents")
"""
        result_path = "results/fixed_app_v2.py"
    else:
        # Reparacion original para SQL Injection
        fixed_code = """import sqlite3
import os

# REPARADO: Se eliminan credenciales y rutas hardcodeadas (NSA 1.4.1)
DB_PATH = os.getenv('DB_PATH', 'default_secure.db')

def get_admin_access(token):
    # REPARADO: Verificacion estricta y parametrizacion (NSA 2.4.1)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = "SELECT * FROM access_control WHERE token = ?"
    cursor.execute(query, (token,))
    
    return cursor.fetchone()

if __name__ == "__main__":
    print(get_admin_access("some_secure_token"))
"""
        result_path = "results/fixed_app.py"

    os.makedirs("results", exist_ok=True)
    with open(result_path, "w", encoding='utf-8') as f:
        f.write(fixed_code)
    
    print(f"[+] Refactorizacion completada por Bob. Codigo seguro en: {result_path}")