#CALCULAR EL PROMEDIO DE 3 CALIFICACIONES Y DECIR SI ES APROBADO O REPROBADO

#LIBRERIAS
from colorama import Fore, Style
#ENTRADA
cal1 = float(input("Ingrese la primera calificacion: "))
cal2 = float(input("Ingrese la segunda calificacion: "))
cal3 = float(input("Ingrese la tercera calificacion: "))

#PROCESO
while ((cal1<0 or cal1>10) or (cal2<0 or cal2>10) or (cal3<0 or cal3>10)):
    print("-----------------CALIFICACIONES-----------------")
    cal1 = float(input("Ingrese la primera calificacion: "))
    cal2 = float(input("Ingrese la segunda calificacion: "))
    cal3 = float(input("Ingrese la tercera calificacion: "))
    promedio = (cal1+cal2+cal3)/3


if (promedio > 6 and promedio <=10):
    print(Fore.GREEN + "Aprobado"+ Style.RESET_ALL)
elif (promedio <6 and promedio >=0):
    print(Fore.RED +"Reprobado" +Style.RESET_ALL)
elif promedio==6:
    print(Fore.YELLOW+"Apenas aprobado"+Style.RESET_ALL)
elif (promedio<0 or promedio>10):
    print("Calificacion invalida")
else:
    print("Error")
    

#SALIDA
print("El promedio es de: ", promedio)