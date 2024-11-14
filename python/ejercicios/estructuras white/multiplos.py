import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')
        
        
x=1
numero=int(input("Ingrese el numero que quiera ver los numeros primos de ese mismo: "))
fin=int(input("Ingrese hasta donde quiere ver los numeros primos de ese numero: "))
multiplo=numero

while x<=fin:
    while multiplo<=fin:
        print(f"{numero} * {x} = {multiplo} ")
        multiplo=multiplo+numero
        x=x+1