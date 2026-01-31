#Calcular la nomina para un empleado en el mes de Mayo del 2023 cocociendo su pago por día de $250
#ENTRADA
pagoDia = 300

#PROCESO
pagoBase = pagoDia*31
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
print("La nomina es de: ", pagoNeto)