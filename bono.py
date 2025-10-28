def calcular_bono(sueldo_base, porcentaje_bono):
    print("\n=== Cálculo del Bono ===")

    bono = sueldo_base * (porcentaje_bono / 100)

    total = sueldo_base + bono

    print("Sueldo base:", sueldo_base)
    print("Porcentaje de bono:", porcentaje_bono, "%")
    print("Monto del bono:", bono)
    print("Sueldo total con bono:", total)

    return total