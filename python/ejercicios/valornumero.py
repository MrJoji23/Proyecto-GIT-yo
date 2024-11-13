import os ##Se importa un modulo para que deje interactuar con la consolo que pueda detectar que sistema operativo esta usando, en este caso windows

def borrar_pantalla(): ##Se define una funcion que se llama borrar_pantalla
    sistema = os.name   ##Linea para detectar que sistema se esta usando 
    if sistema=='nt':   ##Cuando lo detecte el programa lanzara 'nt'
        os.system('cls')    ##Lo que realizara es eliminar lo que se ha escrito por el momento en la consola

for i in range(1):              ## Ciclo para pregunte por el numero, y que se guarde en la variable numero
    numero=int(input(f"Ingrese el numero: " ))
    
borrar_pantalla()               ## Funcion para borrar la pantalla 

print(f"Su numeros es {numero}")  ##Se mostrara el numero que digito el usuario


##If para evaluar que numero escogio el usuario si es un numero positivo, negativo o nulo

if numero>0:                                
    print(f"Su numero es positivo y es {numero}")
elif numero==0:
    print(f"Su numero es nulo, es decir cero {numero}")
else:
    print(f"Su numero es negativo y es {numero}")
    
