import os ##importa modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema= os.name
    
    if sistema == 'nt':
        os.system('cls')
        
x=1
cantidad=int(input("Cuantas alturas va a promediar "))
alt=0
suma=0

while x<=cantidad:
    alt=float(input(f"Ingrese la altura de la persona en cm y con un punto (Ej:1.70) "))
    suma= suma+alt
    x+=1
promedio= suma/cantidad

print(f"Este es el promedio de estatura de las personas que digito {promedio}")


        