from tkinter import filedialog
import os
import subprocess
import threading

#=======================funcion para botos de elegir y convertir archivos======================================#

def elegir_archivo(contenedor, label_archivo):
    archivo = filedialog.askopenfilename(
        title= "selecciona archivo",
        # initialdir = "carpeta de donde quiera que se habra" # -----> con esto le indicamos de que carpeta quiero que se habra
        filetypes=[("videos", "*.mp4 *.mpg *.avi *.MP4"),
                   ("Imágenes", "*.jpg *.png *.jpeg *.webp *.JPG"),
                   ("Audios", "*.mp3 *.wav *.ogg *.opus *.m4a *.aac *.flac"),
                    ("Todos los archivos", "*.*")]
    )

    if archivo:
        contenedor.ruta_archivo = archivo   # -------> guardamos la ruta en el contenedor
        label_archivo.configure(text= f"seleccion: {os.path.basename(archivo)}") # ------- indicamos que se modificara el label para mostrar el archivo

        return archivo # ----- devolvemos la variable para que quede guardada en el contenedor y asi se pueda elegir de cualquier funcion
    
    return None


def convertir(contenedor, label_estado=None, label_salida=None, ffmpeg_cmd="ffmpeg"):

    ruta = getattr(contenedor, "ruta_archivo", None) # --- mandamos a seleccionar la variablke de la ruta devuelta con la funcion elegir_archivo
    if not ruta:
        if label_estado:
            label_estado.configure(text="❌ Primero selecciona un archivo")
        return None

    nombre, ext = os.path.splitext(ruta) 
    ext = ext.lower() # --- convertimos la extencion en miniscula para poder comparar con la lista

    # ---------- VIDEO ----------
    if ext in [".avi", ".mpg", ".mpeg", ".mkv", ".mov", ".wmv",".mp4",".MP4"]:
        salida = nombre + "_convertido.mp4"
        
        cmd = [   #------ se procede a impregnar el comando correcto para la convercion
            
            ffmpeg_cmd,
            "-y",
            "-i", ruta,
             # VIDEO
            "-c:v", "libx264",
            "-profile:v", "baseline",
            "-level", "3.1",
            "-pix_fmt", "yuv420p",
            "-preset", "fast",
            "-crf", "23",

            # AUDIO
            "-c:a", "aac",
            "-b:a", "192k",

            # OPTIMIZACIÓN
            "-movflags", "+faststart",
            salida
        ]
        tipo = "video → mp4"

    # ---------- AUDIO ---------- #
    elif ext in [".wav", ".aac", ".ogg", ".opus",".flac", ".m4a"]:
        salida = nombre + "_convertido.mp3"
        cmd = [
            ffmpeg_cmd,
            "-y",
            "-i", ruta,
             "-vn",
            "-c:a", "libmp3lame",
            "-b:a", "192k",
            "-ar", "44100",
            salida
        ]
        tipo = "audio → mp3"

    # ---------- IMAGEN ---------- #
    elif ext in [".jpg", ".jpeg", ".webp", ".bmp", ".tiff",".JPG"]:
        salida = nombre + "_convertido.png"
        cmd = [
            ffmpeg_cmd,
            "-y",
            "-i", ruta,

            # Conversión segura
            "-vf", "scale=iw:ih",   # mantiene resolución
            "-pix_fmt", "rgba",     # compatible
            salida
        ]

        tipo = "imagen → png"

    else:
        if label_estado:
            label_estado.configure(text="❌ Formato no soportado")
        return None
    

    print("RUTA ENTRADA:", ruta),
    print("RUTA SALIDA:", salida),
    print("CMD:", " ".join(cmd)),

    if label_estado:
        label_estado.configure(text=f"⏳ Convirtiendo {tipo}...")

    proceso = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if proceso.returncode == 0:
        contenedor.ruta_salida = salida
        if label_estado:
            label_estado.configure(text="✅ Conversión finalizada")
        if label_salida:
            label_salida.configure(text=os.path.basename(salida))
        return salida
    else:
        error = proceso.stderr.splitlines()[-1] if proceso.stderr else "Error desconocido"
        if label_estado:
            label_estado.configure(text="❌ Error al convertir")
        if label_salida:
            label_salida.configure(text=error)
        return None


# ---------- llamar a barra de estado ---------- #


def iniciar_barra(barra):
    barra.grid() # -----  mostramos la barra
    barra.start() #----> iniciamos la barra

def detener_barra(barra):
    barra.stop()  # -----> paramos la barra
    barra.set(0) # ------> lo reiniciamos a cero
    barra.grid_remove() # ----> la ocultamos



def llamar_barra(contenedor,barra, label_estado, label_salida, ffmpeg_cmd="ffmpeg"):

    # ----> iniciamos barra
    contenedor.after(0, lambda: (iniciar_barra(barra),
                                 label_estado.configure(text="⏳ Convirtiendo... no cierres la app"),
                                 label_salida.configure(text=""))) 

    def proceso():
         salida = convertir(contenedor, label_estado=None, label_salida=None, ffmpeg_cmd=ffmpeg_cmd)

         # ----- creamos una funcion cuando se termine el proceso de convercion

         def fin_convertir():
             detener_barra(barra)

             if salida:
                 label_estado.configure(text= "convercion finalizada")
                 label_salida.configure(text= os.path.basename(salida))

             else:
                label_estado.configure(text="error")

         contenedor.after(0,fin_convertir)

    threading.Thread(target=proceso, daemon=True).start()


