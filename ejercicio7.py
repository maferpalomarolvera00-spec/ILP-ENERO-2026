#Pedir el nivel del agua en metros de una cisterna
#ENTRADA
nivel = float(input("Ingresa el nivel del agua en metros: "))

#PROCESO
if nivel > 6: 
    print("Desbordamiento de Agua en Cisterna") #SALIDA
elif nivel == 6:
    print("Apagar bomba") 
elif (nivel >4 and nivel < 6):
    print("Desacelerar bomba") 
elif (nivel > 2 and nivel <=4):
    print("Bomba trabajando") 
elif (nivel>0 and nivel<=2):
    print("Acelerar bomba de agua") 
elif nivel==0:
    print("Encender bomba de agua") 
elif nivel<0:
    print("Fuga en cisterna")
else: 
    print("Valor inexistente") 
