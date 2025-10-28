import datos
import bono
import resumen

def mostrar_mensaje_despedida():
    return print("Muchas gracias por usar el menú de PyCompany")

def menu():
    opcion = 0
    registrar_empleado = {}
    total = 0


    while opcion != 4:
        print("\nBienvenido al menú de PyCompany\n")
        print("1) Registrar la información de un empleado")
        print("2) Calcular su bono")
        print("3) Mostrar resumen del trabajador")
        print("4) Salir del programa\n")

        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                registrar_empleado = datos.ingresar_datos()
            case 2:
                if not registrar_empleado:
                    print("⚠️\tDebes registrar un empleado antes de calcular el bono!!")
                else:
                    total = bono.calcular_bono(registrar_empleado["sueldo_base"], registrar_empleado["porcentaje_bono"])
            case 3:
                if not registrar_empleado:
                    print("⚠️\tDebes registrar un empleado para mostrar el resumen!!")
                elif total == 0:
                    resumen.mostrarResumen(registrar_empleado["nombre"],registrar_empleado["edad"], registrar_empleado["cargo"], registrar_empleado["sueldo_base"])
                else:
                    resumen.mostrarResumen(registrar_empleado["nombre"],registrar_empleado["edad"], registrar_empleado["cargo"], total)
            case 4:
                mostrar_mensaje_despedida()


menu()
