import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f'{usuario[1]}, Crea una nota!!!')
        
        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Introduce el contenido de la nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'Nota <{nota.titulo}> guardada!!!')

        else:
            print(f'No se ha guardado la nota, disculpe {usuario[1]}')


    def mostrar(self, usuario):
        print(f'\nVale {usuario[1]}, estas son tus notas')

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n**********************************************************")
            print(nota[2])
            print(nota[3])
            print("\n**********************************************************")

    def eliminar(self, usuario):
        print(f'{usuario[1]}, elimina una nota')

        titulo = input('Introduce el titulo de la nota a eliminar: ')

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f'Nota <{nota.titulo}> eliminada')
        
        else:
            print('No ha sido posible elmininar la nota')