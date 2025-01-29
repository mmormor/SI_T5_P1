import keyboard

def imprime_tecla(tecla): 
    print(tecla.name)
    
    # Abrir el archivo en modo 'a' para agregar el texto al final
    with open('texto.txt', 'a') as file:
        if tecla.name == 'space':
            file.write(' ')  # Escribir un espacio si la tecla es 'space'
        else:
            file.write(tecla.name)  # Escribir el nombre de la tecla

# Registra la función para que se ejecute cuando se presiona una tecla
keyboard.on_press(imprime_tecla)

# Mantén el programa en ejecución esperando la entrada del teclado
keyboard.wait()
