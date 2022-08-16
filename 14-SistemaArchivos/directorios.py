import os, shutil

#   Crear carpeta   #
if not os.path.isdir('./carpeta1'):
    os.mkdir('./carpeta1')
else:
    print('Ya existe el directorio')


#   Copiar   #
rutaOriginal = './carpeta1'
rutaNueva = '/carpeta1Copiada'

#shutil.copytree(rutaOriginal, rutaNueva)


#   Eliminar carpeta    #
#os.rmdir('./carpeta1')


print('Contenido de la carpeta: ')
contenido = os.listdir('./carpeta1')

for fichero in contenido:
    print(f'Fichero: {fichero}')