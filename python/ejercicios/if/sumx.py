import os


def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')
        
numeros = []

cantidad = 3

for i  in range(3):
    numero=int(input("Por favor ingrese el numero: "))
    numeros.append(numero)

borrar_mensaje()


num1= numeros[0]
num2= numeros[1]
num3= numeros[2]

if num1 == num2:
    resultado=((num1+num2)* num3)
    print(f"Los numeros ingresados son: \n {num1} \n {num2} \n {num3} \n la suma y la multiplicacion de estos son {resultado}")
else:
    print("Valores no iguales, no valido")
    