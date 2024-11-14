import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')
        

triangulos=int(input("Ingrese los triangulos que va a analizar: "))

lado=[]
for i in(triangulos):
    for l in(2):
        lados=int(input(f"Digite el lado {l} del triangulo: "))
        lado.append(lados)

if lado[0] == lado[1] == lado [2]:
    print(f"Su {i} Triangulo digitado es un equilatero ")
else: lado[0]==lado[1] or lado[0]==lado[2] or lado[1]==lado[2]
print(f"Su {i} Triangulo digitado es un isoceles ")

        