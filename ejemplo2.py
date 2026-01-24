#Operaciones Matemáticas Básicas
import math
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
potencia = numero1 ** numero2
PotenciaP = pow(numero1, numero2)
raizCuadrada1 = numero1 ** 0.5
raizCuadrada2 = numero2 ** 0.5
raizCuadradaL = math.sqrt(numero1)
raizCuadradaL2 = math.sqrt(numero2)
raizCubica1 = numero1 ** (1/3)
raizCubica2 = numero2 ** (1/3)
modulo = numero1%numero2 

#CASTEO: Convertir un tipo de dato a otro
#SALIDA DE DATOS (Resultado)
print("SUMA= ", suma) #mostrar resultado de la suma
print("RESTA= ", resta) #mostrar resultado de la resta
print("MULTIPLICACION= "+ str(multiplicacion)) #CONTATENACIÓN con CASTEO. Mostrar resultado de la multiplicación
print(f"DIVISION= {division}") #Interpolación de cadenas. Mostrar resultado de la división
print("POTENCIA= ", potencia) #mostrar el resultado de la potencia
print("RAIZ CUADRADA DEL PRIMER NUMERO= ", raizCuadrada1) #mostrar la raiz cuadrada del primer numero
print("RAIZ CUADRADA DEL SEGUNDO NUMERO= ", raizCuadrada2) #mostrar la raiz cuadrada del segundo numero
print("RAIZ CUBICA DEL PRIMER NUMERO= ", raizCubica1) #mostrar raiz cubica del numero 1
print("RAIZ CUBICA DEL SEGUNDO NUMERO= ", raizCubica2) #mostrar raiz cubica del numero 2
print("MODULO= ", modulo) #mostrar el resultado del modulo

#COMENTAR CTRL + K + C
#DESCOMENTAR CTRL + K + U