def ingresar_datos():

    datos_empleado = {}
    datos_empleado["nombre"] = input("\nIngrese su nombre: ")
    datos_empleado["edad"] = int(input("Ingrese su edad: "))
    datos_empleado["cargo"] = input("Ingrese su cargo: ")
    datos_empleado["sueldo_base"] = int(input("Ingrese sueldo base: "))
    datos_empleado["porcentaje_bono"] = float(input("Ingrese porcentaje bono: "))

    return datos_empleado
