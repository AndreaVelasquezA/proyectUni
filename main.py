anio=int(input("digite en año:"))

if anio%4==0:
   if anio%100==0:
      if anio%400==0:
       print("es año bisiesto")
      else:
       print("no es año bisiesto")
   else:
    print("el año es bisiesto")
else:
 print("lo sentimos el año no es bisiesto")


print("fin del progama")