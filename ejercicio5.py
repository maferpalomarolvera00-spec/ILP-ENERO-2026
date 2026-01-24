#OBTENER VALORES PARA: a, b y c. CALCULAR LA FORMULA GENERAL

#ENTRADA
a = float(input("Dame el valor de a: "))
b = float(input("Dame el valor de b: "))
c = float(input("Dame el valor de c: "))

#PROCESO
x1 = ((-b-(b**2-(4*a*c))**0.5)/(2*a))
x2 = ((-b+(b**2-(4*a*c))**0.5)/(2*a))

#SALIDA
print("El valor de X1 es de: ", x1)
print("El valor de X2 es de: ", x2)