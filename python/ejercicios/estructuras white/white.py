import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema=os.name
    
    if sistema == 'nt':
        os.system('cls')

##Empezamos a usar el while para ciclo

x=1         #Inicializar la variable del contador desde donde 1 que quiero que empieze
mayor=0     #Variables para contador para que vaya guardando el valor 
menor=0
#Suma
promedio_mayor=0
suma_mayor=0
#Resta
promedio_menor=0
suma_menor=0
##Le escribimos hasta donde debe ir el ciclo
while x<=10:
    nota=int(input(f"Ingrese la nota del alumno {x}: "))
    if nota>=7:             #Usar un if para encuentre los numeros que son mayores o iguales a 7
        mayor=mayor+1    #Usar una variable que sirva como contador para que vaya guardando cada valor ingresado en el while
        suma_mayor=suma_mayor+nota #Suma de los numeros mayores o iguales a 7 
    else:                   #Usarlo para cuando los numeros son menores a 7
        menor=menor+1
        suma_menor=suma_menor+nota      #Suma de os numeros menores a 7
        
    x=x+1                  #Variable para que en algún momento salga del while


##If para sacar el promedio de las notas 

if mayor > 0:
     promedio_mayor=suma_mayor/mayor ##Evaluar para sumar y sacar el promedio por las notas digitadas
    
if menor > 0:
    promedio_menor= suma_menor/menor
    
borrar_mensaje()
    
##Imprimiendo las notas y promedio

print(f"Las notas mayor o iguales a 7 son: {mayor}")
print(f"El promedio es: {promedio_mayor}")
print(f"Las notas menores a 7 son: {menor}")
print(f"El promedio es: {promedio_menor}")

