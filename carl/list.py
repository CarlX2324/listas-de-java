import tkinter as tk
from tkinter import ttk

class FrmUsuarios(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Usuarios")
        self.geometry("500x400")

        
        self.usuarios = []

  
        tk.Label(self, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.txtNombre = tk.Entry(self)
        self.txtNombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Apellido:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtApellido = tk.Entry(self)
        self.txtApellido.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txtEmail = tk.Entry(self)
        self.txtEmail.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Clave:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.txtClave = tk.Entry(self, show="*")
        self.txtClave.grid(row=3, column=1, padx=10, pady=5)

      
        btnGuardar = tk.Button(self, text="Guardar", command=self.guardar_usuario)
        btnGuardar.grid(row=4, column=0, padx=10, pady=10)

        btnListar = tk.Button(self, text="Listar", command=self.listar_usuarios)
        btnListar.grid(row=4, column=1, padx=10, pady=10)

      
        self.panelListado = ttk.Treeview(self, columns=("Nombre", "Apellido", "Email"), show="headings")
        self.panelListado.heading("Nombre", text="Nombre")
        self.panelListado.heading("Apellido", text="Apellido")
        self.panelListado.heading("Email", text="Email")
        self.panelListado.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def guardar_usuario(self):
        """Guardar los datos de los campos en la lista"""
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        email = self.txtEmail.get()
        clave = self.txtClave.get()

        if nombre and apellido and email and clave:
            self.usuarios.append({
                "nombre": nombre,
                "apellido": apellido,
                "email": email,
                "clave": clave
            })
            self.limpiar_campos()

    def listar_usuarios(self):
        """Mostrar los usuarios en el panel (Treeview)"""
   
        for row in self.panelListado.get_children():
            self.panelListado.delete(row)

        for u in self.usuarios:
            self.panelListado.insert("", "end", values=(u["nombre"], u["apellido"], u["email"]))

    def limpiar_campos(self):
        """Borra el contenido de las cajas de texto"""
        self.txtNombre.delete(0, tk.END)
        self.txtApellido.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)
        self.txtClave.delete(0, tk.END)


if __name__ == "__main__":
    app = FrmUsuarios()
    app.mainloop()
