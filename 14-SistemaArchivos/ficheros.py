from io import open
import pathlib #-> Con esta libreria, python siempre va a encontrar la ruta al fichero#
import shutil #-> Modulo para copiar archivos #

#   Abrir archivo   #
ruta = str(pathlib.Path().absolute()) + '/ficheroTexto.txt'
archivo = open(ruta, 'a+')

#   Escribir en el fichero  #
archivo.write('---- Texto ingresado desde python ----\n')

#   Cerrar el archivo   #
archivo.close()


#   Abrir archivo   #

archivoLectura = open(ruta, 'r') #read#

#   Leer contenido  #
#contenido = archivoLectura.read()
#print(contenido)

#   Leer contenido y guardarlo en una lista   #
lista = archivoLectura.readlines()

archivoLectura.close()

for frase in lista:
    #listaFrase = frase.split()
    #print(listaFrase)
    print('- ' + frase.upper())
    print('- ' + frase.center(100))


#   Copiar archivo  #
"""
rutaNueva = str(pathlib.Path().absolute()) + '/ficheroCopiado.txt'
#rutaAlternativa = ruta = str(pathlib.Path().absolute()) + '/../13-Paquetes/ficheroAlternativo.txt'
shutil.copyfile(ruta, rutaNueva)
"""

#   Mover archivo   #
"""
rutaOriginal = str(pathlib.Path().absolute()) + '/ficheroCopiado.txt'
rutaNueva = str(pathlib.Path().absolute()) + '/ficheroCopiadoNUEVO.txt'

shutil.move(rutaOriginal, rutaNueva)
"""

#   Eliminar archivo    #
"""
import os
rutaNueva = str(pathlib.Path().absolute()) + '/ficheroCopiadoNUEVO.txt'
os.remove(rutaNueva)
"""

#   Comprobar si existe   #
import os.path

#print(os.path.abspath('./'))

rutaComprobar = os.path.abspath('./') + '/ficheroTexto66.txt'

if os.path.isfile(rutaComprobar):
    print('El archivo existe')
else:
    print('No existe el archivo')