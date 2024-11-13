import os ##importa modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema= os.name
    
    if sistema == 'nt':
        os.system('cls')
        
numero=int(input("Ingrese numero random hasta el 999: ")) ##Que dijite el numero
borrar_mensaje() ##Llamando a la funcion


##Se usa el if para analizar el numero que ingreso.
##Se usa el abs para que el usuario cuando digite un numero negativo sea en valor absoluto, osea que sea numeros positivos

if abs(numero)<=9:          
    print (f"Su numero es de una sola cifra y es {numero}")
elif abs(numero)<=99:
    print(f"Su numero es de dos cifras y es {numero}")
elif abs(numero)<=999:
    print(f"Su numero es de tres cifras y es {numero}") 
else:
    print(f"Su numero no es valido")
