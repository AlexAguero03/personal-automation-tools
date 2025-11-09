# File Organizer

Script en **Python** que organiza automáticamente los archivos de una carpeta en subcarpetas según su tipo (imágenes, documentos, videos u otros).  
Incluye detección de archivos duplicados y registro de movimientos en un archivo `log.txt`.

---

## 🧠 Funcionalidad

1. Abre una ventana para seleccionar la carpeta a organizar.  
2. Crea subcarpetas según las extensiones de los archivos.  
3. Mueve cada archivo a su categoría correspondiente.  
4. Evita sobrescribir archivos duplicados (añade sufijos como `_1`, `_2`, etc.).  
5. Registra todos los movimientos en `log.txt`.

---

## 🚀 Ejecución

Desde tu entorno virtual:

```bash
python main.py

Aparecerá un cuadro de diálogo para elegir la carpeta.
Ejemplo de salida en terminal:

foto.png -> imagenes
informe.pdf -> documentos
video.mp4 -> videos
Organización completa: /home/usuario/Descargas

## ⚙️ Requisitos

- Python 3.x
- Tkinter (para el selector visual de carpetas)

Instalar Tkinter en Ubuntu:
sudo apt install python3-tk

## 📋 Notas

- Los archivos ocultos y el propio log.txt no se mueven.

- Puedes ejecutar el script desde cualquier ubicación; solo afectará la carpeta seleccionada.

- Este proyecto forma parte del portafolio de prácticas de desarrollo en Python.