import customtkinter as ctk

# Configuración global de apariencia
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# --- BASE DE DATOS / DICCIONARIO DE PRODUCTOS ---
DICCIONARIO_PRODUCTOS = {
    "P001": {"nombre": "Laptop Pro 15\" Intel i7", "precio": 1250.00, "categoria": "Equipos"},
    "P002": {"nombre": "Monitor Gamer 27\" 144Hz", "precio": 320.50, "categoria": "Monitores"},
    "P003": {"nombre": "Teclado Mecánico RGB", "precio": 85.00, "categoria": "Periféricos"},
    "P004": {"nombre": "Mouse Ergonómico Inalámbrico", "precio": 45.00, "categoria": "Periféricos"},
    "P005": {"nombre": "Auriculares Noise Cancelling", "precio": 180.00, "categoria": "Audio"},
    "P006": {"nombre": "Silla Ergonómica Ejecutiva", "precio": 290.00, "categoria": "Mobiliario"},
    "P007": {"nombre": "Webcam Full HD 1080p", "precio": 65.00, "categoria": "Video"},
    "P008": {"nombre": "Disco Duro Externo 2TB SSD", "precio": 110.00, "categoria": "Almacenamiento"}
}


class VentanaCatalogo(ctk.CTkToplevel):
    """
    Ventana Secundaria (Catálogo/Diccionario)
    Recibe una función 'callback' que se ejecuta cuando el usuario selecciona un producto.
    """
    def __init__(self, parent, callback_seleccion):
        super().__init__(parent)
        self.callback_seleccion = callback_seleccion
        
        self.title("Diccionario de Productos / Catálogo")
        self.geometry("550x500")
        self.resizable(False, False)
        self.attributes("-topmost", True)  # Mantener al frente le nueva venatana
        self.configure(fg_color="#0F172A")

        # Título
        lbl_titulo = ctk.CTkLabel(
            self, 
            text="Seleccione un Producto del Catálogo", 
            font=("Segoe UI", 18, "bold"),
            text_color="#F8FAFC"
        )
        lbl_titulo.pack(pady=15)

        # Buscador / Filtro
        self.entry_buscar = ctk.CTkEntry(
            self,
            placeholder_text="Buscar producto por nombre...",
            width=480,
            height=38,
            corner_radius=8,
            border_color="#3B82F6",
            fg_color="#1E293B"
        )
        self.entry_buscar.pack(pady=(0, 10))
        self.entry_buscar.bind("<KeyRelease>", self.filtrar_productos)

        # Frame Desplazable (CTkScrollableFrame) para mostrar la lista
        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            width=480,
            height=320,
            corner_radius=10,
            fg_color="#1E293B"
        )
        self.scroll_frame.pack(pady=10)

        # Cargar lista inicial
        self.renderizar_productos(DICCIONARIO_PRODUCTOS)

    def renderizar_productos(self, productos_dict):
        """Limpia el frame desplegable y vuelve a dibujar los productos."""
        # Limpiar widgets anteriores
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # Generar un "card" por cada producto en el diccionario
        for codigo, info in productos_dict.items():
            card = ctk.CTkFrame(self.scroll_frame, fg_color="#334155", corner_radius=8)
            card.pack(fill="x", pady=5, padx=5)

            # Información del producto
            texto_prod = f"[{codigo}] {info['nombre']}\nCategoría: {info['categoria']} | Precio: ${info['precio']:.2f}"
            lbl_info = ctk.CTkLabel(
                card, 
                text=texto_prod, 
                justify="left", 
                font=("Segoe UI", 12),
                text_color="#F8FAFC"
            )
            lbl_info.pack(side="left", padx=12, pady=10)

            # Botón para seleccionar y enviar a la ventana principal
            btn_seleccionar = ctk.CTkButton(
                card,
                text="Seleccionar",
                width=100,
                height=32,
                fg_color="#10B981",
                hover_color="#059669",
                font=("Segoe UI", 12, "bold"),
                command=lambda item=info: self.seleccionar_y_cerrar(item)
            )
            btn_seleccionar.pack(side="right", padx=12)

    def filtrar_productos(self, event=None):
        """Filtra el diccionario en tiempo real según la búsqueda."""
        texto = self.entry_buscar.get().lower()
        productos_filtrados = {
            cod: info for cod, info in DICCIONARIO_PRODUCTOS.items()
            if texto in info["nombre"].lower() or texto in info["categoria"].lower()
        }
        self.renderizar_productos(productos_filtrados)

    def seleccionar_y_cerrar(self, producto_info):
        """Ejecuta el callback para mandar los datos a la ventana principal y cierra esta ventana."""
        self.callback_seleccion(producto_info)
        self.destroy()


class AppFormularioPrincipal(ctk.CTk):
    """
    Ventana Principal del Sistema (Formulario de Pedidos)
    """
    def __init__(self):
        super().__init__()

        # Propiedades de la Ventana Principal
        self.title("Sistema de Gestión de Pedidos")
        self.geometry("600x700")
        self.resizable(False, False)
        self.configure(fg_color="#0F172A")

        # --- HEADER ---
        self.lbl_header = ctk.CTkLabel(
            self, 
            text="🛒 Formulario de Registro de Pedido", 
            font=("Segoe UI", 22, "bold"),
            text_color="#F8FAFC"
        )
        self.lbl_header.pack(pady=(20, 15))

        # --- SECCIÓN CLIENTE ---
        self.frame_cliente = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=12)
        self.frame_cliente.pack(pady=10, padx=30, fill="x")

        lbl_sec_cliente = ctk.CTkLabel(
            self.frame_cliente, 
            text="Datos del Cliente", 
            font=("Segoe UI", 14, "bold"), 
            text_color="#60A5FA"
        )
        lbl_sec_cliente.pack(anchor="w", padx=15, pady=(10, 5))

        self.entry_cliente = ctk.CTkEntry(
            self.frame_cliente,
            placeholder_text="Nombre del Cliente...",
            width=500,
            height=38,
            corner_radius=8
        )
        self.entry_cliente.pack(padx=15, pady=(0, 12))

        # --- SECCIÓN PRODUCTO SELECCIONADO ---
        self.frame_producto = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=12)
        self.frame_producto.pack(pady=10, padx=30, fill="x")

        lbl_sec_prod = ctk.CTkLabel(
            self.frame_producto, 
            text="Producto Seleccionado", 
            font=("Segoe UI", 14, "bold"), 
            text_color="#60A5FA"
        )
        lbl_sec_prod.pack(anchor="w", padx=15, pady=(10, 5))

        # Botón para abrir la subventana de catálogo
        self.btn_abrir_catalogo = ctk.CTkButton(
            self.frame_producto,
            text="🔍 Abrir Catálogo / Diccionario de Productos",
            height=40,
            fg_color="#3B82F6",
            hover_color="#2563EB",
            font=("Segoe UI", 13, "bold"),
            command=self.abrir_ventana_catalogo
        )
        self.btn_abrir_catalogo.pack(fill="x", padx=15, pady=5)

        # Campos rellenados automáticamente
        self.entry_prod_nombre = ctk.CTkEntry(
            self.frame_producto,
            placeholder_text="Ningún producto seleccionado",
            width=500,
            height=38,
            corner_radius=8,
            state="disabled"  # Inhabilitado para evitar escritura manual libre
        )
        self.entry_prod_nombre.pack(padx=15, pady=5)

        self.entry_prod_precio = ctk.CTkEntry(
            self.frame_producto,
            placeholder_text="Precio unitario: $0.00",
            width=500,
            height=38,
            corner_radius=8,
            state="disabled"
        )
        self.entry_prod_precio.pack(padx=15, pady=(0, 12))

        # --- SECCIÓN CANTIDAD Y TOTAL ---
        self.frame_calculo = ctk.CTkFrame(self, fg_color="#1E293B", corner_radius=12)
        self.frame_calculo.pack(pady=10, padx=30, fill="x")

        self.lbl_cantidad = ctk.CTkLabel(
            self.frame_calculo, 
            text="Cantidad de Unidades: 1", 
            font=("Segoe UI", 13, "bold"),
            text_color="#94A3B8"
        )
        self.lbl_cantidad.pack(pady=(10, 2))

        # Slider para cambiar cantidad
        self.slider_cantidad = ctk.CTkSlider(
            self.frame_calculo,
            from_=1,
            to=20,
            number_of_steps=19,
            width=480,
            command=self.actualizar_calculos
        )
        self.slider_cantidad.set(1)
        self.slider_cantidad.pack(pady=5)

        self.lbl_total = ctk.CTkLabel(
            self.frame_calculo, 
            text="TOTAL A PAGAR: $0.00", 
            font=("Segoe UI", 18, "bold"),
            text_color="#10B981"
        )
        self.lbl_total.pack(pady=12)

        # Variables internas para cálculos
        self.precio_unitario_actual = 0.0

        # --- BOTONES DE ACCIÓN (Procesar y Limpiar) ---
        self.frame_botones = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botones.pack(pady=15)

        self.btn_confirmar = ctk.CTkButton(
            self.frame_botones,
            text="Confirmar Pedido",
            width=230,
            height=45,
            corner_radius=10,
            fg_color="#10B981",
            hover_color="#059669",
            font=("Segoe UI", 14, "bold"),
            command=self.procesar_pedido
        )
        self.btn_confirmar.grid(row=0, column=0, padx=10)

        self.btn_limpiar = ctk.CTkButton(
            self.frame_botones,
            text="🧹 Limpiar Formulario",
            width=230,
            height=45,
            corner_radius=10,
            fg_color="#EF4444",
            hover_color="#DC2626",
            font=("Segoe UI", 14, "bold"),
            command=self.limpiar_formulario
        )
        self.btn_limpiar.grid(row=0, column=1, padx=10)

        # Mensaje de estado final
        self.lbl_estado = ctk.CTkLabel(self, text="", font=("Segoe UI", 13))
        self.lbl_estado.pack(pady=5)

    def abrir_ventana_catalogo(self):
        """Abre la subventana del catálogo pasándole la función de callback."""
        ventana_cat = VentanaCatalogo(self, callback_seleccion=self.recibir_producto)

    def recibir_producto(self, producto):
        """
        Función Callback: Se ejecuta desde la subventana cuando se elige un producto.
        Recibe un diccionario con los datos del producto seleccionado.
        """
        # Habilitar temporalmente los campos para modificar su contenido
        self.entry_prod_nombre.configure(state="normal")
        self.entry_prod_precio.configure(state="normal")

        # Limpiar contenido anterior
        self.entry_prod_nombre.delete(0, "end")
        self.entry_prod_precio.delete(0, "end")

        # Insertar datos recibidos del catálogo
        self.entry_prod_nombre.insert(0, producto["nombre"])
        self.entry_prod_precio.insert(0, f"${producto['precio']:.2f}")

        # Bloquear de nuevo los campos para que sean de solo lectura
        self.entry_prod_nombre.configure(state="disabled")
        self.entry_prod_precio.configure(state="disabled")

        # Guardar precio numérico y actualizar total
        self.precio_unitario_actual = producto["precio"]
        self.actualizar_calculos()

        self.lbl_estado.configure(
            text=f" Producto '{producto['nombre']}' cargado al formulario.",
            text_color="#3B82F6"
        )

    def actualizar_calculos(self, val=None):
        """Actualiza la etiqueta de cantidad y recalcula el monto total."""
        cant = int(self.slider_cantidad.get())
        self.lbl_cantidad.configure(text=f"Cantidad de Unidades: {cant}")
        
        total = cant * self.precio_unitario_actual
        self.lbl_total.configure(text=f"TOTAL A PAGAR: ${total:.2f}")

    def procesar_pedido(self):
        """Valida que todos los datos estén completos."""
        cliente = self.entry_cliente.get().strip()
        prod_nombre = self.entry_prod_nombre.get()

        if not cliente:
            self.lbl_estado.configure(text="Ingrese el nombre del cliente.", text_color="#F59E0B")
            return

        if not prod_nombre:
            self.lbl_estado.configure(text=" Debe seleccionar un producto del catálogo.", text_color="#F59E0B")
            return

        cant = int(self.slider_cantidad.get())
        total = cant * self.precio_unitario_actual
        self.lbl_estado.configure(
            text=f"🎉 ¡Pedido registrado para {cliente}! Total: ${total:.2f}",
            text_color="#10B981"
        )

    def limpiar_formulario(self):
        """Resetea todos los campos a su estado por defecto."""
        self.entry_cliente.delete(0, "end")

        self.entry_prod_nombre.configure(state="normal")
        self.entry_prod_precio.configure(state="normal")
        self.entry_prod_nombre.delete(0, "end")
        self.entry_prod_precio.delete(0, "end")
        self.entry_prod_nombre.configure(state="disabled")
        self.entry_prod_precio.configure(state="disabled")

        self.slider_cantidad.set(1)
        self.precio_unitario_actual = 0.0
        self.actualizar_calculos()

        self.lbl_estado.configure(text="🧹 Formulario limpiado correctamente.", text_color="#94A3B8")


if __name__ == "__main__":
    app = AppFormularioPrincipal()
    app.mainloop()