# 🗂️ File Organizer

Script en **Python** que organiza automáticamente los archivos de una carpeta en subcarpetas según su tipo: **imágenes**, **documentos**, **videos** u **otros**.  
Incluye detección de archivos duplicados y registro detallado de movimientos en un archivo `log.txt`.

---

## 🚀 Características principales

- 🧭 Selector visual de carpeta mediante **Tkinter**.  
- 📁 Clasificación automática por tipo de archivo.  
- ⚙️ Creación dinámica de subcarpetas.  
- 🔁 Manejo de archivos duplicados (añade sufijos como `_1`, `_2`, etc.).  
- 🧾 Registro completo de acciones en `log.txt`.  
- 🚫 Ignora archivos ocultos y el propio `log.txt`.

---

## 🧠 Funcionamiento

1. Ejecuta el script.  
2. Se abrirá una ventana para seleccionar la carpeta a organizar.  
3. El programa clasificará los archivos por tipo:  
   - **Imágenes:** `.jpg`, `.png`, `.gif`, `.jpeg`, `.bmp`, etc.  
   - **Documentos:** `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`, etc.  
   - **Videos:** `.mp4`, `.mov`, `.avi`, `.mkv`, etc.  
   - **Otros:** cualquier otro tipo no reconocido.  
4. Todos los movimientos se registran en `log.txt` dentro de la misma carpeta.

---

## 💻 Ejemplo de ejecución

```bash
python main.py
```

Salida esperada en la terminal:

```
foto.png -> imagenes
informe.pdf -> documentos
video.mp4 -> videos
Organización completa: /home/usuario/Descargas
```

---

## ⚙️ Requisitos

- **Python 3.x**
- **Tkinter** (para el selector de carpetas)

Instalación en Ubuntu:

```bash
sudo apt install python3-tk
```

---

## 📋 Notas

- El archivo `log.txt` no se mueve ni se sobreescribe.  
- Los archivos ocultos se omiten automáticamente.  
- Puedes ejecutar el script desde cualquier ruta; solo afectará la carpeta seleccionada.  
- Ideal para proyectos de automatización o prácticas de organización en Python.
