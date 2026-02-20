import customtkinter as ctk
from PIL import Image
import os
from utileria.herramientas_extras import centrar_ventana
from utileria.herramientas_extras import actualizar_hora
from .interfaces_botones import info_dispositivo, imagen_video


# ======================= TEMA (como el mockup) ======================= #
THEME = {
    "bg_app": "#0B0E14",
    "header": "#1B2240",
    "sidebar": "#121723",
    "main": "#0F131C",

    "card": "#171D2B",

    "btn": "#141A28",
    "btn_hover": "#2A1BAE",
    "btn_active": "#1F6AA5",

    "text": "#EDEDED",
    "muted": "#AAB0C0",
    "danger": "#9B3636",
}


class panel1(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("PDI VERACRUZ")
        centrar_ventana(self, 1100, 600)
        self.configure(fg_color=THEME["bg_app"])

        # ======================= CONFIGURACION GENERAL DE LOS GRID ======================= #
        self.grid_rowconfigure(0, weight=0)  # header fijo
        self.grid_rowconfigure(1, weight=1)  # body crece
        self.grid_rowconfigure(2, weight=0)  # footer fijo

        self.grid_columnconfigure(0, weight=0)  # sidebar fijo
        self.grid_columnconfigure(1, weight=1)  # main crece

        # ======================= CONBTENEDOR 1 ======================= #
        self.contenedor1 = ctk.CTkFrame(
            self,
            fg_color=THEME["header"],
            corner_radius=0,
            height=72
        )
        self.contenedor1.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.contenedor1.grid_propagate(False)

        # Logo opcional (si tienes una imagen)
        # Si no existe, no truena
        logo_path = os.path.join("imagenes", "pain.png")
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path)
                self.logo = ctk.CTkImage(light_image=logo_img, dark_image=logo_img, size=(44, 44))
                ctk.CTkLabel(self.contenedor1, image=self.logo, text="").place(x=18, y=14)
            except Exception:
                pass

        # Título + subtítulo (estilo mockup)
        self.lbl_titulo = ctk.CTkLabel(
            self.contenedor1,
            text="Software Forence Móvil",
            text_color=THEME["text"],
            font=("Inter", 24, "bold")
        )
        self.lbl_titulo.place(x=70, y=12)

        self.lbl_subtitulo = ctk.CTkLabel(
            self.contenedor1,
            text="Interfaz principal (CustomTkinter)",
            text_color=THEME["muted"],
            font=("Inter", 14)
        )
        self.lbl_subtitulo.place(x=72, y=42)

        # Hora
        self.label_hora = ctk.CTkLabel(
            self.contenedor1,
            text="00:00:00",
            text_color=THEME["danger"],
            font=("Inter", 18, "bold")
        )
        self.label_hora.place(x=720, y=12)

        # Fecha
        self.label_fecha = ctk.CTkLabel(
            self.contenedor1,
            text="",
            text_color="#95224A",
            font=("Inter", 16, "bold")
        )
        self.label_fecha.place(x=720, y=40)

        actualizar_hora(self.contenedor1, self.label_hora, self.label_fecha)

        # Badge "Investigador"
        self.badge_user = ctk.CTkFrame(self.contenedor1, fg_color="#0E1426", corner_radius=14)
        self.badge_user.place(x=930, y=18)

        ctk.CTkLabel(
            self.badge_user,
            text="Investigador",
            text_color=THEME["text"],
            font=("Inter", 14, "bold")
        ).pack(padx=14, pady=8)

        # ======================= SIDEBAR (contenedor2) ======================= #
        self.contenedor2 = ctk.CTkFrame(
            self,
            fg_color=THEME["sidebar"],
            corner_radius=0,
            width=240
        )
        self.contenedor2.grid(row=1, column=0, sticky="ns")
        self.contenedor2.grid_propagate(False)

        # ======================= MAIN (contenedor3) ======================= #
        self.contenedor3 = ctk.CTkFrame(
            self,
            fg_color=THEME["main"],
            corner_radius=0
        )
        self.contenedor3.grid(row=1, column=1, sticky="nsew")
        self.contenedor3.grid_propagate(False)

        # ======================= FOOTER ======================= #
        self.footer = ctk.CTkFrame(self, fg_color=THEME["bg_app"], corner_radius=0, height=64)
        self.footer.grid(row=2, column=0, columnspan=2, sticky="nsew")
        self.footer.grid_propagate(False)

        self.btn_reporte = ctk.CTkButton(
            self.footer,
            text="Generar Reporte",
            height=42,
            font=("Inter", 16, "bold"),
            fg_color=THEME["btn_active"],
            hover_color=THEME["btn_hover"],
            text_color=THEME["text"],
            corner_radius=10,
            command=self.generar_reporte_placeholder  # placeholder
        )
        self.btn_reporte.pack(pady=10)

        # ======================= BOTONES LATERALES ======================= #
        self.botones_sidebar = []  # se llena después

        self.boton_convertir = self._crear_boton_sidebar(
            "Convertidor",
            command=lambda: (
                self.activar_boton(self.boton_convertir),
                self.limpiar_contenedor3(),
                imagen_video(self.contenedor3)  # ✅ tu módulo actual
            )
        )

        self.boton_dispositivo = self._crear_boton_sidebar(
            "Dispositivo",
            command=lambda: (
                self.activar_boton(self.boton_dispositivo),
                self.mostrar_dispositivo()  # ✅ tu módulo actual
            )
        )

        # 👇 Estos se quedan sin lógica real (solo UI), como pediste:
        self.boton_imagenes = self._crear_boton_sidebar(
            "Imágenes",
            command=lambda: (
                self.activar_boton(self.boton_imagenes),
                self.limpiar_contenedor3()
                # módulo futuro aquí (NO se toca)
            )
        )

        self.boton_videos = self._crear_boton_sidebar(
            "Videos",
            command=lambda: (
                self.activar_boton(self.boton_videos),
                self.limpiar_contenedor3()
                # módulo futuro aquí (NO se toca)
            )
        )

        self.boton_audios = self._crear_boton_sidebar(
            "Audios",
            command=lambda: (
                self.activar_boton(self.boton_audios),
                self.limpiar_contenedor3()
                # módulo futuro aquí (NO se toca)
            )
        )

        self.boton_redes = self._crear_boton_sidebar(
            "Conexión a redes",
            command=lambda: (
                self.activar_boton(self.boton_redes),
                self.limpiar_contenedor3()
                # módulo futuro aquí (NO se toca)
            )
        )

        # Registrar para estado activo
        self.botones_sidebar = [
            self.boton_convertir,
            self.boton_dispositivo,
            self.boton_imagenes,
            self.boton_videos,
            self.boton_audios,
            self.boton_redes
        ]

        # Vista inicial: dashboard (como mockup)
        self.mostrar_dashboard()

    # ======================= CREAR BOTÓN SIDEBAR ======================= #
    def _crear_boton_sidebar(self, texto, command):
        btn = ctk.CTkButton(
            self.contenedor2,
            text=f"  {texto}",
            height=42,
            font=("Inter", 15, "bold"),
            text_color=THEME["text"],
            fg_color=THEME["btn"],
            hover_color=THEME["btn_hover"],
            corner_radius=10,
            anchor="w",
            command=command
        )
        btn.pack(padx=12, pady=6, fill="x")
        return btn

    # ======================= ESTADO ACTIVO BOTÓN ======================= #
    def activar_boton(self, boton_activo=None):
        for boton in self.botones_sidebar:
            boton.configure(fg_color=THEME["btn"])
        if boton_activo:
            boton_activo.configure(fg_color=THEME["btn_active"])

    # ======================= LIMPIEZA MAIN ======================= #
    def limpiar_contenedor3(self):
        """Borra lo que haya en contenedor3 para que no se encime."""
        for w in self.contenedor3.winfo_children():
            w.destroy()
        self.contenedor3.configure(fg_color=THEME["main"])

    # ======================= DISPOSITIVO (tu módulo) ======================= #
    def mostrar_dispositivo(self):
        self.limpiar_contenedor3()
        # Mantengo tu estilo claro si lo deseas:
        # self.contenedor3.configure(fg_color="#EDEFF5")
        info_dispositivo(self.contenedor3)

    # ======================= DASHBOARD (mockup) ======================= #
    def _card(self, parent, title):
        card = ctk.CTkFrame(parent, fg_color=THEME["card"], corner_radius=14)
        card.grid_propagate(False)

        lbl = ctk.CTkLabel(card, text=title, text_color=THEME["text"], font=("Inter", 16, "bold"))
        lbl.pack(anchor="w", padx=14, pady=(12, 8))

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=14, pady=(0, 12))
        return card, body

    def mostrar_dashboard(self):
        self.limpiar_contenedor3()
        self.activar_boton(None)

        # grid tipo mockup (2 columnas)
        self.contenedor3.grid_rowconfigure((0, 1, 2), weight=1)
        self.contenedor3.grid_columnconfigure((0, 1), weight=1)

        # Convertidor
        c1, b1 = self._card(self.contenedor3, "Conversión de Archivos")
        c1.grid(row=0, column=0, sticky="nsew", padx=14, pady=14)
        self._dash_btn(b1, "Ir a Convertidor", lambda: self.boton_convertir.invoke())

        # Dispositivo
        c2, b2 = self._card(self.contenedor3, "Información del Dispositivo")
        c2.grid(row=0, column=1, sticky="nsew", padx=14, pady=14)
        self._dash_btn(b2, "Ver Dispositivo", lambda: self.boton_dispositivo.invoke())

        # Imágenes
        c3, b3 = self._card(self.contenedor3, "Galería de Imágenes")
        c3.grid(row=1, column=0, sticky="nsew", padx=14, pady=0)
        ctk.CTkLabel(b3, text="(Módulo en construcción)", text_color=THEME["muted"]).pack(anchor="w", pady=10)

        # Videos
        c4, b4 = self._card(self.contenedor3, "Archivos de Video")
        c4.grid(row=1, column=1, sticky="nsew", padx=14, pady=0)
        ctk.CTkLabel(b4, text="(Módulo en construcción)", text_color=THEME["muted"]).pack(anchor="w", pady=10)

        # Audios
        c5, b5 = self._card(self.contenedor3, "Archivos de Audio")
        c5.grid(row=2, column=0, sticky="nsew", padx=14, pady=14)
        ctk.CTkLabel(b5, text="(Módulo en construcción)", text_color=THEME["muted"]).pack(anchor="w", pady=10)

        # Redes
        c6, b6 = self._card(self.contenedor3, "Conexión a Redes")
        c6.grid(row=2, column=1, sticky="nsew", padx=14, pady=14)
        ctk.CTkLabel(b6, text="(Módulo en construcción)", text_color=THEME["muted"]).pack(anchor="w", pady=10)

    def _dash_btn(self, parent, text, command):
        btn = ctk.CTkButton(
            parent,
            text=text,
            height=40,
            corner_radius=12,
            fg_color="#202945",
            hover_color=THEME["btn_hover"],
            text_color=THEME["text"],
            font=("Inter", 14, "bold"),
            anchor="w",
            command=command
        )
        btn.pack(fill="x", pady=6)

    # ======================= PLACEHOLDER REPORTE ======================= #
    def generar_reporte_placeholder(self):
        print("[+] Generar Reporte (placeholder)")

    

        



