import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')
        

empleados=int(input("Ingrese cuantos empleados hay en su empresa: "))

x=1
acumulador1=0
acumulador2=0
total=0
while x<=empleados:
    sueldo=float(input(f"Ingrese el sueldo de sus empleado {x}: "))
    if sueldo<=300: 
        acumulador1=acumulador1+1
    else:
        acumulador2=acumulador2+1
    total=total+sueldo
    x=x+1
    
borrar_mensaje()    
  
  
    
print(f"Los empleados que ganan menos de 300 son: {acumulador1}")
print(f"Los empleados que ganan mas de 300 son: {acumulador2}")
print(F"El total de de sueldo en personal es: {total}")