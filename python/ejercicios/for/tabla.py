import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')
        
borrar_mensaje()

digito=int(input(f"Por favor ingresa un numero del 1 al 10: "))

borrar_mensaje()

acumulador=0
for i in range(1, 13):
    acumulador=digito*i
    print(f"{digito} * {i} = {acumulador}")
