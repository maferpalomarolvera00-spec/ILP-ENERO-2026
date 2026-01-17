#Operaciones Matemáticas Básicas

#ENTRADAS DE DATOS
#= asignación simple
#Declaración de variables
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))



#PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2


#CASTEO: Convertir un tipo de dato a otro
#SALIDA DE DATOS (Resultado)
print("SUMA= ", suma) #mostrar resultado de la suma
print("RESTA= ", resta) #mostrar resultado de la resta
print("MULTIPLICACION= "+ str(multiplicacion)) #CONTATENACIÓN con CASTEO. Mostrar resultado de la multiplicación
print(f"DIVISION= {division}") #Interpolación de cadenas. Mostrar resultado de la división

#COMENTAR CTRL + K + C
#DESCOMENTAR CTRL + K + U