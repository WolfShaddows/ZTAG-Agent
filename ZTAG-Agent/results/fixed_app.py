import sqlite3
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
