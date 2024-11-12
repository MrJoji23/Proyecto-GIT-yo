numeros = [] ##Inicializar las variable a que sea una tabla

num_repeticion=3 ## La cantidad de veces que va a repetir para preguntar

for i in range(num_repeticion):             ##Ciclo para que pregunte por el numero 
    numero=int(input(f"Ingresa el numero {i+1}: "))
    numeros.append(numero)      #Variable para que se vaya guardando en la tabla
print(f"Estos son sus numeros {numeros}")

num1= numeros[0]        ##Darle el valor a la variable donde se ubica especificamente
num2= numeros[1]
num3= numeros[2]


if num1>num2:              #Un if  para que vea si es más grande que el segundo
    if num1>num3:           #Un if aninado para seguir comprobando si el numero 1 es grande
        mayor = num1
        mayor2= "Primer"    ##Imprime el numero 
    else:
        mayor = num3
        mayor2 = "Tercero"     #Si no es mayor el 1, es el tercer
elif num2>num3:
    mayor = num2                #If para comprobar si el numero dos es más mayor 
    mayor2= "Segundo"
else:
    mayor =num3   
    mayor2= "Tercero"

    
##El salto de linea es (texto \n texto)


texto=(f"Su numero mayor es {mayor} tambien \nFue el {mayor2} que digito").capitalize()
   
   
print(texto)    ##Se imprime el numero mayor que digito y se coloca en que numero del ciclo lo digito



#####Funcion para encontrar el numero maximo que ingresaron los datos #######

##max_numeros= max(numeros)         
##print(f"Este es el numero más grande que usted digito {max_numeros}")



