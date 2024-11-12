#Cada funcion para que funcione tiene que agresarse al fina un ()

#Crear una lista con list
lista= list(["Hola", "Juan", "Pablo", 28])

lista.append("Caida") ##Agregando un elemento a la lista 

lista.insert(1, "Un osito Dormilon") ##Agregando un elemento a la lista en un indice 

lista.extend([28, True, "Pepita", False]) ##Agregando varios elementos a la lista

lista.pop(1) #Para poder eliminar el elemento de una tabla especifico

lista.remove(28) #Removiendo un elemento de la lista por su valor

#lista.clear() #eleminando todos los elementos de una lista


cantidad_de_elementos = len(lista) #dcuenta la cantidad de elementos que hay en una lista



print(lista)