
## matriz

matriz= ["Juan Pablo", "Jean Poll", 19, "Solo voleibol",
         "Camila", "Milita", 16, "Baile",
         "Camilo", "Juan", 17, "Futbol"]

for i in range(0, len(matriz), 4):
    nombre= matriz[i]
    segundo_nombre= matriz[i+1]
    edad= matriz[i+2]
    hobbit= matriz[i+3]
    
    if edad < 18:
        print( nombre)
        



