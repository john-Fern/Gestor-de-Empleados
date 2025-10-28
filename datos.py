def ingresar_datos():
    print("\n=== Registro de Empleado ===")

    nombre = str(input("Ingrese el nombre del empleado: "))
    edad = int(input("Ingrese la edad del empleado: "))
    cargo = str(input("Ingrese el cargo del empleado: "))
    sueldo_base = int(input("Ingrese el sueldo base del empleado: "))
    porcentaje_bono = float(input("Ingrese el porcentaje de bono (%): "))

    return nombre, edad, cargo, sueldo_base, porcentaje_bono