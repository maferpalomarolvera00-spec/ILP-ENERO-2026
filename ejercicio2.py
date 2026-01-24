#CALCULAR EL AREA Y PERIMETRO DE UN CIRCULO


#ENTRADA
PI = 3.1416
radio = float(input ("Ingrese el valor del radio: "))

#PROCESO
perimetro = 2*PI*radio

area = PI*(radio**2)

#SALIDA
print("El perimetro del circulo es de: ", perimetro)
print("El area del circulo es de: ", area)