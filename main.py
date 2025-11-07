import os
import shutil
from tkinter import Tk, filedialog

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


def generar_destino_unico(destino_inicial: str) -> str:
    """
    Si el archivo destino ya existe, agrega _1, _2, etc. antes de la extensión.
    """
    carpeta = os.path.dirname(destino_inicial)
    nombre = os.path.basename(destino_inicial)
    nombre_sin_ext, ext = os.path.splitext(nombre)

    destino = destino_inicial
    contador = 1
    while os.path.exists(destino):
        nuevo_nombre = f"{nombre_sin_ext}_{contador}{ext}"
        destino = os.path.join(carpeta, nuevo_nombre)
        contador += 1

    return destino


def registrar_movimiento(origen: str, destino: str, ruta_log: str) -> None:
    with open(ruta_log, "a", encoding="utf-8") as f:
        f.write(f"{origen} -> {destino}\n")


def mover_archivo(ruta_archivo: str, categoria: str, ruta_log: str) -> None:
    carpeta_base = os.path.dirname(ruta_archivo)
    carpeta_destino = os.path.join(carpeta_base, categoria)
    os.makedirs(carpeta_destino, exist_ok=True)

    nombre_archivo = os.path.basename(ruta_archivo)
    destino_inicial = os.path.join(carpeta_destino, nombre_archivo)
    destino_final = generar_destino_unico(destino_inicial)

    shutil.move(ruta_archivo, destino_final)
    print(f"{nombre_archivo} -> {categoria}")
    registrar_movimiento(ruta_archivo, destino_final, ruta_log)


def organizar_carpeta(ruta: str) -> None:
    ruta_log = os.path.join(ruta, "log.txt")

    for nombre in os.listdir(ruta):
        if nombre.startswith("."):
            continue
        if nombre == "log.txt":
            continue

        ruta_archivo = os.path.join(ruta, nombre)
        if os.path.isfile(ruta_archivo):
            _, ext = os.path.splitext(nombre)
            categoria = obtener_categoria(ext)
            mover_archivo(ruta_archivo, categoria, ruta_log)


if __name__ == "__main__":
    Tk().withdraw()  # oculta la ventana principal
    ruta = filedialog.askdirectory(title="Selecciona la carpeta a organizar")

    if ruta:
        organizar_carpeta(ruta)
        print(f"Organización completa: {ruta}")
    else:
        print("No se seleccionó ninguna carpeta.")
