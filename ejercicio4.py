#PEDIR LA CANTIDAD DE GRADOS Y CONVERTIRLOS A °C, °F Y °K

#ENTRADA
can = float (input("Ingrese los grados: "))
unidad = input("Ingrese C, K o F: ").strip().upper()
unidadC = input("Ingrese a que grados se va a convertir: ").strip().upper()

#PROCESO
match unidad:
    case "C":
        match unidadC:
            case "K":
                con = can + 273.15
            case "F":
                con = (9 * can / 5) + 32
            case "C":
                con = can
            case _:
                print("Unidad destino no válida")
                con = None

    case "F":
        match unidadC:
            case "C":
                con = (5 * (can - 32)) / 9
            case "K":
                con = (5 * (can - 32)) / 9 + 273.15
            case "F":
                con = can
            case _:
                print("Unidad destino no válida")
                con = None

    case "K":
        match unidadC:
            case "C":
                con = can - 273.15
            case "F":
                con = (9 * (can - 273.15) / 5) + 32
            case "K":
                con = can
            case _:
                print("Unidad destino no válida")
                con = None

    case _:
        print("Unidad origen no válida")
        con = None
                     
    

#SALIDA
print("El resultado de la conversion es de: ", con)