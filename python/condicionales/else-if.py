#en python el else if no se escribe tal cual, se escribe solo elif y abajo la accion 

ingreso_mensual=33000
gasto_mensual=33000
porcentaje= 65

##Operaciones
restante=((ingreso_mensual* porcentaje)/100)- gasto_mensual

if ingreso_mensual >= 10000:
  if restante < 0:
      print (f"estas en perdidas pa {restante} " + "de dolares" )
  elif ingreso_mensual - gasto_mensual > 3000:
      print("bien pa, estas bien ")
  else:
      print("y bueno parcero, toca que mire si le alcanza")
    

elif ingreso_mensual >=1000:
    print("Sos re rico en latinoamerica")
elif ingreso_mensual >=500:
    print("Parce vives re bien en colombia xd")
elif ingreso_mensual >=200:
    print("Sos re rico en venezuela")
else:
    print("sos re probre")