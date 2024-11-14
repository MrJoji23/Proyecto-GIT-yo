import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema= os.name
    
    if sistema == 'nt':
        os.system('cls')
    
sueldo= int(input("Ingrese su sueldo: "))               
años= int(input("Ingrese los años que lleva en la empresa: "))

borrar_mensaje()

##If para ver en que rango esta el sueldo y los años que digitarón
if sueldo<500 and años>10:
    aumento= sueldo*0.20
    resultado= aumento+sueldo
    print(f"Su sueldo a pagar sería {resultado}")
elif sueldo<500 and años<10:
    aumento= sueldo*0.05
    resultado= aumento+sueldo
    print(f"Su sueldo a pagar seria de {resultado}")
else: 
    print(f"Su sueldo sigue siendo {sueldo}")
    