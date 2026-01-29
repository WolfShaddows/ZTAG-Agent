import os

def backup_system(folder_name):
    # FALLO: Confianza implicita en entrada de usuario (NSA 2.4.1)
    # Un atacante podria pasar: "folder; rm -rf /"
    print(f"Haciendo backup de: {folder_name}")
    os.system(f"zip -r backup.zip {folder_name}")

if __name__ == "__main__":
    backup_system("my_documents")