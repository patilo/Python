from customtkinter.windows.widgets.appearance_mode import appearance_mode_base_class
from tkinter import CENTER
import customtkinter as ctk

# Configuración global de apariencia
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class VentanaAjustesAvanzados(ctk.CTkToplevel):
    """Ventana secundaria que se abre al hacer clic en un botón."""
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Opciones Adicionales")
        self.geometry("380x280")
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.configure(fg_color="#0F172A")
        
        
        lbl = ctk.CTkLabel(self, text="Preferencias del Sistema", font=("Segoe UI", 16, "bold"))
        lbl.pack(pady=15)

        self.sw_dark = ctk.CTkSwitch(self, text="Modo Desarrollador")
        self.sw_dark.pack(pady=10)

        self.chk_logs = ctk.CTkCheckBox(self, text="Guardar registros de auditoría")
        self.chk_logs.pack(pady=10)

        btn_guardar = ctk.CTkButton(
            self, 
            text="Guardar Preferencias", 
            fg_color="#10B981", 
            hover_color="#059669",
            command=self.destroy
        )
        btn_guardar.pack(pady=20)


class AppPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Propiedades de la Ventana Principal
        self.title("Panel de Control - CustomTkinter Lab")
        self.geometry("520x620")
        self.resizable(False, False)
        
        # Redefinir fondo de la ventana principal
        self.configure(fg_color="#0F172A")

        # 2. Título Header
        self.lbl_titulo = ctk.CTkLabel(
            self, 
            text="Configuración de Perfil", 
            font=("Segoe UI", 22, "bold"),
            text_color="#F8FAFC"
        )
        self.lbl_titulo.pack(pady=(25, 15))

        # 3. Campo para rellenar (Entry)
        self.entry_nombre = ctk.CTkEntry(
            self,
            placeholder_text="Ingrese su nombre completo...",
            width=360,
            height=42,
            corner_radius=10,
            border_color="#3B82F6",
            fg_color="#1E293B"
        )
        self.entry_nombre.pack(pady=10)

        # 4. Caja de opciones (OptionMenu)
        self.lbl_rol = ctk.CTkLabel(self, text="Rol del Usuario:", text_color="#94A3B8")
        self.lbl_rol.pack(pady=(10, 2))
        
        self.combo_rol = ctk.CTkOptionMenu(
            self,
            values=["Administrador", "Analista de Datos", "Invitado"],
            width=360,
            height=38,
            corner_radius=8,
            fg_color="#334155",
            button_color="#475569",
            button_hover_color="#64748B"
        )
        self.combo_rol.pack(pady=5)

        # 5. Deslizador (Slider)
        self.lbl_nivel = ctk.CTkLabel(self, text="Nivel de Acceso (0-100):", text_color="#94A3B8")
        self.lbl_nivel.pack(pady=(15, 2))

        self.slider_acceso = ctk.CTkSlider(
            self,
            from_=0,
            to=100,
            number_of_steps=100,
            width=360,
            button_color="#3B82F6",
            button_hover_color="#1D4ED8",
            progress_color="#60A5FA"
        )
        self.slider_acceso.set(50)
        self.slider_acceso.pack(pady=5)

        # 6. Botón para abrir Sub-Ventana
        self.btn_mas_opciones = ctk.CTkButton(
            self,
            text="Más Opciones Avanzadas",
            width=360,
            height=40,
            corner_radius=8,
            fg_color="#475569",
            hover_color="#334155",
            command=self.abrir_subventana
        )
        self.btn_mas_opciones.pack(pady=20)

        # 7. Contenedor de Botones de Acción (Guardar y Limpiar)
        self.frame_acciones = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_acciones.pack(pady=10)

        self.btn_guardar = ctk.CTkButton(
            self.frame_acciones,
            text="Guardar",
            width=170,
            height=42,
            corner_radius=10,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            font=("Segoe UI", 13, "bold"),
            command=self.accion_guardar
        )
        self.btn_guardar.grid(row=0, column=0, padx=10)

        # Botón para limpiar campos
        self.btn_limpiar = ctk.CTkButton(
            self.frame_acciones,
            text="Limpiar Todo",
            width=170,
            height=42,
            corner_radius=10,
            fg_color="#EF4444",
            hover_color="#DC2626",
            font=("Segoe UI", 13, "bold"),
            command=self.limpiar_campos
        )
        self.btn_limpiar.grid(row=0, column=1, padx=10)

        # Label de Mensajes de Estado
        self.lbl_estado = ctk.CTkLabel(self, text="", font=("Segoe UI", 12))
        self.lbl_estado.pack(pady=15)

    def abrir_subventana(self):
        """Abre la ventana flotante de opciones extra."""
        subventana = VentanaAjustesAvanzados(self)
        

    def accion_guardar(self):
        nombre = self.entry_nombre.get()
        if not nombre.strip():
            self.lbl_estado.configure(text="Por favor ingrese un nombre.", text_color="#F59E0B")
        else:
            self.lbl_estado.configure(
                text=f"Usuario '{nombre}' guardado como {self.combo_rol.get()}",
                text_color="#10B981"
            )

    def limpiar_campos(self):
        """Resetea todos los controles a sus valores iniciales."""
        self.entry_nombre.delete(0, "end")
        self.combo_rol.set("Administrador")
        self.slider_acceso.set(50)
        self.lbl_estado.configure(text="🧹 Formulario limpiado correctamente.", text_color="#94A3B8")


if __name__ == "__main__":
    app = AppPrincipal()
    app.mainloop()