import sqlite3

# VIOLACIÓN 1.4.1: Credenciales y paths hardcodeados
DB_PATH = "C:/Users/PC/Desktop/NSA-ZeroTrust-Refactor/ZTAG-Agent/results/database.db"

def get_admin_access(token):
    # VIOLACIÓN 2.4.1: Confianza implícita en el token sin verificar origen
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # VIOLACIÓN: Vulnerable a Inyección SQL
    query = f"SELECT * FROM access_control WHERE token = '{token}'"
    cursor.execute(query)
    
    return cursor.fetchone()

# Ejecución insegura
print(get_admin_access("admin' OR '1'='1"))