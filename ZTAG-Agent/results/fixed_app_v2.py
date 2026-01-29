import subprocess

def backup_system(folder_name):
    # REPARADO: Se usa subprocess.run con una lista de argumentos (NSA 2.4.1)
    # Esto evita que un atacante inyecte comandos extra mediante caracteres como ';'
    print(f"Haciendo backup seguro de: {folder_name}")
    
    # Al pasar los argumentos como lista, el sistema no interpreta simbolos shell
    subprocess.run(["zip", "-r", "backup.zip", folder_name], check=True)

if __name__ == "__main__":
    backup_system("my_documents")
