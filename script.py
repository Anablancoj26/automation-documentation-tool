import os
import shutil
from pathlib import Path

def organize_directory(base_path: str):
    """
    Organiza automáticamente los archivos de un directorio en subcarpetas 
    según su extensión (Imágenes, Documentos, Código, etc.)
    """
    target_dir = Path(base_path)
    
    if not target_dir.exists():
        print(f"❌ La ruta especificada no existe: {base_path}")
        return

    # Definir categorías de archivos
    extensions_map = {
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Código": [".py", ".js", ".html", ".css", ".json", ".sql"],
        "Comprimidos": [".zip", ".rar", ".tar", ".gz"]
    }

    print(f"🚀 Iniciando organización en: {target_dir.absolute()}")

    # Contador de archivos movidos
    moved_count = 0

    for file_path in target_dir.iterdir():
        if file_path.is_file() and file_path.name != "script.py":
            file_ext = file_path.suffix.lower()
            moved = False

            for category, exts in extensions_map.items():
                if file_ext in exts:
                    category_dir = target_dir / category
                    category_dir.mkdir(exist_ok=True)
                    
                    shutil.move(str(file_path), str(category_dir / file_path.name))
                    print(f"📁 Movido: {file_path.name} -> {category}/")
                    moved_count += 1
                    moved = True
                    break
            
            if not moved:
                other_dir = target_dir / "Otros"
                other_dir.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(other_dir / file_path.name))
                print(f"📦 Movido a 'Otros': {file_path.name}")
                moved_count += 1

    print(f"\n✅ ¡Proceso finalizado! Total de archivos organizados: {moved_count}")

if __name__ == "__main__":
    # Ruta de prueba (puedes cambiarla por la ruta que desees organizar)
    path_to_organize = input("Ingresa la ruta de la carpeta a organizar (deja en blanco para usar la carpeta actual): ").strip()
    if not path_to_organize:
        path_to_organize = "."
    
    organize_directory(path_to_organize)
