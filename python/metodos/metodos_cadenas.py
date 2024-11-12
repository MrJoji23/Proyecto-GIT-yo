#Estructura de los metodos es
# dato.nombredelmetodo()

cadena1 = ("Juan Pablo Marin Rodriguez")
cadena2 = ("Bienvenido parcero")


mayus= cadena1.upper() ##Convierte a mayusculas
minus= cadena1.lower() ##Convierte en minusculas
PriLetrMayus= cadena1.capitalize() ##Convertir la primera letra en mayuscula  
#busqueda= cadena1.find() ##Buscamos una cadena dentro de otra cadena, si no hay coincidencias devuelve -1
#busqueda_index =  cadena1.index() ##Buscamos una cadena dentro de otra cadena, pero cuando no encuentra nada salta un error

numerico= cadena1.isnumeric() ## Si es numerico devuelve true, si no false

contar_coincidencias = cadena1.count("a") #Buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
 
contar_caracteres= len(cadena1) #Contamos cuantos caracteristicas tiene una cada una

empieza_con = cadena1.startswith("Juan")#Verifica la cadena empieza con otra cadena dada si es asi la devuelve

termina_con = cadena2.endswith("cero")#Verifica la cadena termina con otra cadena dada si es asi la devuelve

cadena_nueva = cadena2.replace("ro","ra" )
cadena_nueva= cadena_nueva.replace("ido", "ida")

print(cadena_nueva) 