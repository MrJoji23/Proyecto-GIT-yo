
## Creando un diccionario (dict)
## la palabra str sirve para pasar los numeros a cadena texto
## Primero se define el key y despues se le da un valor (key : value, ... ... ...)

diccionario = {
    'name' : 'Jean Paul',
    'password' : 'lionazulverde1930',
    'esta_depresivo' : True,
    'cm' : str(1.7) + " cm",
    'dato_duplicado' : 'Jean Paul'
}

print(diccionario['cm'])

## otra manera
## 'cm' : f"{1.7} cm",
## lo de usar la f sirve como para que en las comillas se escriba lo que quiere que se muestre y las llaves {} se muestren el valor o lo que se escribio de la variable 
