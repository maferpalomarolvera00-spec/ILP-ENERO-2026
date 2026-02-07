"""
REALIZAR UN PROGRAMA QUE REALICE UN CUESTIONARIO CON LAS SIGUIENTES 12 PREGUNTAS, MUESTRE SU RESULTADO 
ACIERTOS/12 Y MOSTRAR LA CALIFICACION=(ACIERTOS/12)*10
"""
from colorama import Fore, Style
aciertos=0

print("1. Herramienta de programacion, parecido al lenguaje español utilizado para crear codigo.")
print("a) IDE     b) Pseudocodigo     c) Compilador     d) ANSI/ISO")
respuesta1= input("Respuesta 1: ").strip().lower()
if (respuesta1 == "b"):
    aciertos+=1

print("2. Conjunto de simbolos, letras, numeros, imagenes, audio y video organizadas y que son " 
"elevantes en un tiempo y forma determinados.")
print("a) Informacion     b) Datos     c) Programa     d) Codigo")
respuesta2= input("Respuesta 2: ").strip().lower()
if (respuesta2 == "a"):
    aciertos+=1

print("3.  Instituciones encargadas de estandarizar reglas y simbologia de los Diagramas de Flujo.")
print("a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode")
respuesta3= input("Respuesta 3: ").strip().lower()
if (respuesta3 == "c"):
    aciertos+=1

print("4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.")
print("a) Proceso     b) Solucion     c) Funcion     d) Algoritmo")
respuesta4= input("Respuesta 4: ").strip().lower()
if (respuesta4 == "d"):
    aciertos+=1

print("5. Conjunto de elementos que se relacionan para cumplir una funcion determinada.")
print("a) Estructura     b) Datos     c) Operación     d) Sistema")
respuesta5= input("Respuesta 5: ").strip().lower()
if (respuesta5 == "d"):
    aciertos+=1

print("6. Componente de un IDE que se encarga de traducir el codigo fuente a codigo maquina.")
print("a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete")
respuesta6= input("Respuesta 6: ").strip().lower()
if (respuesta6 == "d"):
    aciertos+=1

print("7. Elemento que se usa para almacenar una cantidad donde cambia su valor.")
print("a) Constante     b) Variable     c) Libreria     d) Tipo de Dato")
respuesta7= input("Respuesta 7: ").strip().lower()
if (respuesta7 == "b"):
    aciertos+=1

print("8. Conjunto de simbolos, letras, numeros que no tienen un significado.")
print("a) Proceso     b) Solucion     c) Funcion     d) Algoritmo")
respuesta8= input("Respuesta 8: ").strip().lower()
if (respuesta8 == "a"):
    aciertos+=1

print("9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.")
print("a) Filosofia     b) Sociologia     c) Logica     d) Argumentacion")
respuesta9= input("Respuesta 9: ").strip().lower()
if (respuesta9 == "c"):
    aciertos+=1

print("10. Medida, patron, modelo o norma universal para realizar una actividad o producir un objeto.")
print("a) Evento     b) Estandar     c) Calidad     d) Productividad")
respuesta10= input("Respuesta 10: ").strip().lower()
if (respuesta10 == "b"):
    aciertos+=1

print("11. Conjunto de elementos ordenados que componen y son la base de algo fisico o no fisico.")
print(" a) Estructura     b) Sistema     c) Objeto     d) Virtual")
respuesta11= input("Respuesta 11: ").strip().lower()
if (respuesta11 == "a"):
    aciertos+=1

print("12. Conjunto de instrucciones (codigo) que indican a la computadora tareas a realizar.")
print("a) Operaciones/Calculos     b) Sintaxis     c) Programa de Computadora     d) Comando")
respuesta12= input("Respuesta 12: ").strip().lower()
if (respuesta12 == "c"):
    aciertos+=1

print("Aciertos: ",aciertos,"/12")
calificacion=(aciertos/12)*10
print("La calificacion es de: ", calificacion)
if (calificacion >=6):
    print(Fore.GREEN+"APROBADO"+Style.RESET_ALL)
else:
    print(Fore.RED+"REPROBADO"+Style.RESET_ALL)