import time



#centrar ventana
def centrar_ventana(self, ancho, alto):
    self.update_idletasks()  # ---> se solicita info de pantalla

    ancho_pantalla = self.winfo_screenwidth()
    alto_pantalla = self.winfo_screenheight()

    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)

    self.geometry(f"{ancho}x{alto}+{x}+{y}")



# actualizar hora

def actualizar_hora(ventana, label_hora, label_fecha):

    hora = time.strftime("%-I:%M:%S %p").lower().lstrip("0") # -----> colocamos la hora en formato de 12 horas, y que sea compatible con windows
    label_hora.configure(text=hora)

    #se establece los dias y meses en español

    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    """se empiza a desglosar el tiempo a como deseemos"""
    tiempo = time.localtime()  # ------> se optiene el tiempo local (maquina)

    dia_semana = dias[tiempo.tm_wday].upper() # ------> se optiene el nunmero de dia, que empieza de 0 y empiza en lunes, por eso la lista comienza en lunes
    numero_dia = tiempo.tm_mday #  --------> se optiene el numero de dia de mes
    mes = meses[tiempo.tm_mon - 1].upper() # -------> los meses empiezan en 1 por lo que se resta 1 para concordar con la lista de meses que emoiezan en 0
    año = tiempo.tm_year

    fecha = f"{dia_semana} {numero_dia}, {mes}, {año}"
    label_fecha.configure(text=fecha)

    # volver a llamarse cada 1 segundo
    ventana.after(1000, lambda: actualizar_hora(ventana, label_hora, label_fecha))
    

