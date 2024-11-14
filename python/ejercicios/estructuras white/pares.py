import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')
        
    
    
x=1
termino=11

##Ciclo para sacar los pares de 11 en 11 que se repita 25 veces

while x<=25:            
    print(termino)
    x=x+1
    termino=termino+11  ##El termino se va sumando el mismo + 11 oara que saque los pares
