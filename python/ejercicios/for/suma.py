import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')
        
valores=[]       #Creo una lista para que se vaya guardando los valores de cada numero 
        
for f in range(10):     #Se hace un ciclo for para que repitas 10 veces que numero ingresa
    valor=int(input(f"Ingrese los digito #{f+1}: "))
    valores.append(valor)   #Funcion para que el valor de la variable "valor" se guarde en en la lista de valores
    

acumulador=0
for i in range(5):  # Solo necesitamos leer 5 veces para hacer las sumas
    suma = valores[i] + valores[i + 5]  # El primer valor se suma con el sexto, el segundo con el séptimo, etc.
    print(f"La suma del valor  ({i + 6}) es: {suma}")
    acumulador += suma  # Acumulamos la suma total


print(f"La suma de los valores que ingreso son: {acumulador}")
        