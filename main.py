import os

CATEGORIAS = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "documentos": [".pdf", ".docx", ".txt"],
    "videos": [".mp4", ".avi", ".mov"],
    "otros": []
}


def obtener_categoria(extension: str) -> str:
    extension = extension.lower()
    for categoria, extensiones in CATEGORIAS.items():
        if extension in extensiones:
            return categoria
    return "otros"


def listar_archivos(ruta):
    for nombre in os.listdir(ruta):
        if nombre.startswith("."):
            continue
        ruta_completa = os.path.join(ruta, nombre)
        if os.path.isfile(ruta_completa):
            _, ext = os.path.splitext(nombre)
            categoria = obtener_categoria(ext)
            print(f"{nombre} -> {categoria}")



if __name__ == "__main__":
    ruta = input("Ruta de la carpeta a organizar: ")
    listar_archivos(ruta)
