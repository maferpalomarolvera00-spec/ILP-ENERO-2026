#Calcular la nomina para un empleado en el mes de Mayo del 2023 cocociendo su pago por día de $250
#ENTRADA
dias = int(input("Ingrese los dias: "))
pagoDia = float(input("Ingresa el pago por dia: "))

#PROCESO
pagoBase = pagoDia*dias
ivaTrasladado = pagoBase*0.16
subtotal=pagoBase+ivaTrasladado
ivaRetenido = (2/3)*ivaTrasladado
isrRetenido = pagoBase*0.10
pagoNeto=subtotal-ivaRetenido-isrRetenido

#SALIDA
print("Pago base: ", pagoBase)
print("IVA Trasladado: ", ivaTrasladado)
print("Subtotal: ", subtotal)
print("IVA Retenido: ", ivaRetenido)
print("ISR Retenido: ", isrRetenido)
print("El pago neto es de: ", pagoNeto)