import os ##importar modulo para el poder escribir en la consola un mensaje automatico

def borrar_mensaje():
    sistema = os.name
    
    if sistema == 'nt':
        os.system('cls')
        
    
    
x=1
termino=11

while x<=25:
    print(termino)
    x=x+1
    termino=termino+11  
