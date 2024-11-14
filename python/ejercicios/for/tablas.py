import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')

num=int(input(f"Ingrese el numero de la tabla que quiere ver: ")) ##   Ingresar el numero para ver que tabla quiere ver
hasta_donde=int(input(f"Ingrese el numero de hasta donde quiere ir a verla: "))         ##Ingresar hasta donde quiere ver la tabla


#Ciclo for para que cuente desde donde hasta donde hacer la tabla
numero=5

for i in range(1, hasta_donde+1):
    operacion=num*i             #Operacion para que multiplique los numeros
    print(f"{num} * {i} = {operacion}")  