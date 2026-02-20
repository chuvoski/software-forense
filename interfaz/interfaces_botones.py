import customtkinter as ctk
from PIL import Image
import os
from ffmpeg.funcion_ffmpeg import elegir_archivo, llamar_barra




#=======================panel boton convertir img/videos======================================#

def imagen_video(contenedor):
    label_titulo = ctk.CTkLabel(
        contenedor,
        text="Elige la opcion:",
        text_color="#050505",
        font=(
            "arial", 28
            )
         )
    
    label_titulo.grid(row=0, column=0,   padx=350, sticky="n")

    #--------------------label archivo seleccionado-------------------------------#
    
    label_archivo_seleccionado= ctk.CTkLabel(
        contenedor,
        text="sin archivo selecionado",
        text_color="#1F2656",
        font=(
            "arial", 22
            )
         )
    label_archivo_seleccionado.grid(row=2, column=0, pady= 25, padx=170, sticky="n")

    #--------------------label archivo convertido-------------------------------#

    label_estado = ctk.CTkLabel(
    contenedor,
    text="",
    text_color="#050505",
    font=("arial", 16)
    )
    label_estado.grid(row=4, column=0, pady=(10, 0), sticky="n")
    

    label_salida = ctk.CTkLabel(
    contenedor,
    text="",
    text_color="#1F2656",
    font=("arial", 14)
    )
    label_salida.grid(row=5, column=0, pady=(5, 0), sticky="n")

    #--------------------barra de progreso-------------------------------#

    progreso = ctk.CTkProgressBar(contenedor,
                                  width=350,
                                  progress_color= "#0CDA16", # ----> color de la barra
                                  fg_color= "#EEF4F5", # -----> fondo de la barra
                                  mode="indeterminate")
    progreso.grid(row=6, column=0,padx=350)
    progreso.set(0) # -----> lo pocicionamos en 0
    progreso.grid_remove() # ------> la ocultamos al inicio




  #--------------------bonton elegir-------------------------------#
    boton_elegir = ctk.CTkButton(
        contenedor,
        text="elegir archivo",
        font=ctk.CTkFont(
                family= "arial", # ----> tipo de letra
                size= 18 # -----> tamaño
                #weight="bold" # ------> remarcado
            ),
        text_color="#F8F8F8",
        fg_color="#000000",  # ---> color de fondo
        hover_color="#091150", # ----> color al pasar el mouse
        corner_radius= 2, # -----> borde redondeado,
        command= lambda: elegir_archivo(contenedor, label_archivo_seleccionado)
           
    )

    boton_elegir.grid(row=1, column=0, pady= 25, padx=350, sticky="n")

    

    

 #--------------------bonton convertir-------------------------------#
    

    boton_convertir = ctk.CTkButton(
        contenedor,
        text="convertir archivo",
        font=ctk.CTkFont(
                family= "inter", # ----> tipo de letra
                size= 18 # -----> tamaño
                #weight="bold" # ------> remarcado
            ),
        text_color="#F8F8F8",
        fg_color="#000000",  # ---> color de fondo
        hover_color="#091150", # ----> color al pasar el mouse
        corner_radius= 2, # -----> borde redondeado
        command= lambda: llamar_barra(contenedor, progreso,label_estado, label_salida)
    )

    boton_convertir.grid(row=3, column=0, pady= 25, padx=350, sticky="n")
    
    contenedor.configure(fg_color= "#EAE2E2")







    
#=======================panel boton info_dispositivo======================================#

def info_dispositivo(contenedor):

    frame = ctk.CTkFrame(contenedor, fg_color="transparent",width=135,
        height=290)

    ruta = os.path.join("imagenes", "dispositivo.png")

    img_dispositivo = Image.open(ruta)

    frame.dispositivo = ctk.CTkImage(
        light_image=img_dispositivo,
        dark_image=img_dispositivo,
        size=(200, 290)  # tamaño final (ancho, altura)
    )

    label_dispositivo = ctk.CTkLabel(
        frame,
        image= frame.dispositivo,
        text= ""
    )

    label_dispositivo.place(
        relx=0.6,
        rely=0.5,
        anchor="center"
    )

    frame.place(
        x=30, 
        y=80 
        ) 

    return frame

    

