import os
import subprocess
import sys


"esta linea sirve para detectar la carpeta de la aplicacion no importando de donde la ejecutes"

BASE_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

#verificamos que ffmpeg este

def ffmpeg_true():
    
    """
    Verifica si existe ffmpeg
    dentro de las carpetas de
    la aplicacion:

    1) En carpeta ./ffmpeg (portable)
    2) En el PATH del sistema

    
    """
    if sys.platform.startswith("win"): #---> detecta,mos que sistema operativo es, indicamos que si es windows haga lo que sigue
        ffmpeg_local = os.path.join(BASE_DIR, "ffmpeg", "ffmpeg.exe") # ----> buscamos ffmpeg.exe conforme a windows dentro de las carpetas de la aplicacion y la guardamos en una variable
    else:
       ffmpeg_local = os.path.join(BASE_DIR, "ffmpeg", "ffmpeg") # ---> si no pues se da por entendido que es linux, y se busca ffmpeg

    "si existe el archivo portable ffmpeg"
    if os.path.isfile(ffmpeg_local):

        resultado,version,error = version_ffmpeg(ffmpeg_local) # -----> las tres variables saldran de lo que arroge la funcion version_ffmpep

        if resultado:
            return True, version, None
        else:
            return False, None, error
        
    """si nom existe el archivo en las carpetas de la aplicacion
    buscar entonces en el sistema"""

    resultado, version, error = version_ffmpeg("ffmpeg")

    if resultado == True:
        return resultado,version, None
    else:
        return resultado, None, error

    
    




# funcion para optener la version de ffmpeg

def version_ffmpeg(comando):

    try:
        peticion = subprocess.run(
            [comando, "-version"],
            stdout=subprocess.PIPE, # -----> se captura la salida del comando
            stderr=subprocess.PIPE, # -----> se captura la salida de error
            text=True # -----> se tranforma en string las salidas stdout,stderr
        )

        "si devuelve true y stdout, se guarda la captura de la primera linea de la salida"

        if peticion.returncode == 0 and peticion.stdout:
            version = peticion.stdout.split("\n")[0].strip() # -----> divide la salida por lineas, y extrae la primera linea
            return True, version, None
        else:
            error = peticion.stderr.strip() # ------> se guarda la informacion del error
            return False, None, error # ---> se crean tres variables segunel caso (negativo/positivo, version, error), los ultimos dos si no hay informacion se da como variable vacia
    
    except FileNotFoundError as e:
        return False, None, f"ffmpeg no esta: {e}"

    except Exception as e:
        return False, None, f"Ocurrio un error: {e}"


   


if __name__ == "__main__":
    resultado, version, error = ffmpeg_true()
    
    if resultado == True:
        print("\nTienes FFMPEG instalado\n")
        print(f"version: {version}\n")
    else:
        print("""Hay un problema!!!
              No se encontro FFMPEG""")
        print(error)
    
