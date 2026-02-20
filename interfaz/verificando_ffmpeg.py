
import customtkinter as ctk
from utileria.herramienta1 import ffmpeg_true
from utileria.herramientas_extras import centrar_ventana
from interfaz.panel_principal import panel1
import threading



"""creamos ventana de la gui"""

class ventana_verificacion(ctk.CTk):

    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.title("Validacion FFMPEG")
        centrar_ventana(self, 800, 200)
        self.resizable(False,False)
        


        #texto principal
        self.label_estado = ctk.CTkLabel(
            self,
            text="Verificando Dependencias .....⏳",
            justify ="center",
            font=(
                "inter", 15, "bold"
            )
        )

        self.label_estado.pack(pady=(25,10))

        # texto de informacion

        self.label_informacion = ctk.CTkLabel(
            self,
            text= "",
            justify= "center",
            font=(
                "inter", 15, "bold"
            )
        )

        self.label_informacion.pack(pady =(0, 10))

        # botones

        self.botones_frame = ctk.CTkFrame(
            self,
            fg_color= "transparent"
        )
        self.botones_frame.pack(
            pady = 10
            )

        self.boton_reintento=ctk.CTkButton(
            self.botones_frame,
            text= "reintentar",
            font=ctk.CTkFont(
                family= "inter", # ----> tipo de letra
                size= 14, # -----> tamaño
                weight="bold" # ------> remarcado
            ),
            text_color="#050101",
            fg_color="#7B3D0D",  # ---> color de fondo
            hover_color="#AC2285", # ----> color al pasar el mouse
            corner_radius= 10, # -----> borde redondeado
            command= self.autoverificacion
        )

        self.boton_reintento.grid(row=0,column=0,padx=10)

        self.boton_salir= ctk.CTkButton(
            self.botones_frame,
            font=ctk.CTkFont(
                family= "inter", # ----> tipo de letra
                size= 14, # -----> tamaño
                weight="bold" # ------> remarcado
            ),
            text= "salir",
            text_color="#110F0F",
            fg_color="#FF5555",  # ---> color de fondo
            hover_color="#FFC107", # ----> color al pasar el mouse
            corner_radius= 10, # -----> borde redondeado
            command= self.destroy
        )

        self.boton_salir.grid(row=0, column=1, padx=10)


        """Al iniciar el proceso de verificacion se desactiva el boton de reinicio 
            para evitar un bug en dado caso que usuario lo presione"""
        self.boton_reintento.configure(state="disabled")

        
        self.after(50, self.autoverificacion)



    # funciones para la actualizacion de la pantalla y llamada del comando de verificacion 

    def autoverificacion(self):
        self.boton_reintento.configure(state="disabled")
        self.label_estado.configure(text="Verificando Dependencias .....⏳")
        self.label_informacion.configure(text="")

        hilo = threading.Thread(target=self.verificar, daemon=True)
        hilo.start()

    def verificar(self):

        resultado, version, error = ffmpeg_true()

        def actualizar_ui():
            if resultado:

                # se usa after para que el hilo funcione bien y para impedir que la interfaz se congele
                self.after(1000, lambda: self.label_estado.configure(text="🟢 FFMPEG encontrado :")) 
                self.after(1000, lambda: self.label_informacion.configure(text=version))

                self.after(2000, self.siguiente_ventana)

        


            else:

                self.after(1000, lambda: self.label_estado.configure(text="❌ FFMPEG no encontrado:"))
                self.after(1000, lambda: self.label_informacion.configure(text=error))

            self.boton_reintento.configure(state="normal")

        self.after(1200, actualizar_ui)

    def siguiente_ventana(self):
            
        self.destroy()
        ventana2 = panel1()
        ventana2.mainloop()



            

    
        


