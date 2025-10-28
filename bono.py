import datos

def calcular_bono():
    sueldo = int(input("Ingrese Sueldo: "))
    porcentaje = float(input("Ingrese Porcentaje: "))

    if sueldo <= 0:
        print("❎ Error: El sueldo debe ser mayor que 0.")
        return None

    if porcentaje < 0:
        print("❎ Error: El porcentaje no puede ser negativo.")
        return None

    bono = sueldo * (porcentaje / 100)
    total = sueldo + bono

    print("==== Calculo de Bono ====")
    print("Sueldo base:", sueldo)
    print("Porcentaje de bono:", porcentaje)
    print("Sueldo total con bono:", total)

    return total

calcular_bono()
