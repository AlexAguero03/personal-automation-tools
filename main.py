import os

def listar_archivos(ruta):
    for nombre in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, nombre)
        if os.path.isfile(ruta_completa):
            print(nombre)

if __name__ == "__main__":
    ruta = input("Ruta de la carpeta a organizar: ")
    listar_archivos(ruta)
