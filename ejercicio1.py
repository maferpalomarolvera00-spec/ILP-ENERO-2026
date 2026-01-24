#CALCULAR EL PROMEDIO DE 3 CALIFICACIONES Y DECIR SI ES APROBADO O REPROBADO

#LIBRERIAS
from colorama import Fore, Style
#ENTRADA
cal1 = float(input("Ingrese la primera calificacion: "))
cal2 = float(input("Ingrese la segunda calificacion: "))
cal3 = float(input("Ingrese la tercera calificacion: "))

#PROCESO
promedio = (cal1+cal2+cal3)/3

if promedio >= 6:
    print(Fore.GREEN + "Aprobado"+ Style.RESET_ALL)
else:
    print(Fore.RED +"Reprobado" +Style.RESET_ALL)

#SALIDA
print("El promedio es de: ", promedio)