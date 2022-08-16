import usuarios.usuario as modelo
import notas.acciones 


class Acciones:

    def registro(self):
        print("\nRegistro en el sistema...")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        email = input("Email: ")
        password = input("Contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} has sido registrado con el email {registro[1].email}")
        
        else:
            print("No ha sido posible registrarte")

    def login(self):
        print("Identificate en el sistema\n")
        try:
            email = input("Email: ")
            password = input("Contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f'\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}')
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f'Error al loguear')

    
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles.
        -> Crear nota (crear)
        -> Mostrar notas (mostrar)
        -> Eliminar nota (eliminar)
        -> Salir (salir)
        """)
        accion = input(" -> Accion: ")
        hacer = notas.acciones.Acciones()

        if accion == "crear":
            print("-- Creador de notas --")
            hacer.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            print("-- Inventario de notas --")
            hacer.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("-- Eliminacion de notas --")
            hacer.eliminar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f'Bien {usuario[1]}, hasta pronto!')
            exit()
