import datos.py
import bono.py
import resumen.py

def mostrar_mensaje_despedida():
    return print("Muchas gracias por usar el menú de PyCompany")
def menu():
    while True:
        print("Bienvenido al menú de PyCompany")
        print("1) Registrar la información de un empleado")
        print("2) Calcular su bono")
        print("3) Mostrar resumen del trabajador")
        print("4) Salir del programa")

        opcion = int(input("Ingrese una opcion"))
        match opcion:
            case 1:
                datos.ingresar_datos()
            case 2:
                sueldo = int(input("Ingrese sueldo: "))
                porcentaje = float(input("Ingrese porcentaje del bono: "))
                bono.calcular_bono(sueldo,porcentaje)
            case 3:
                resumen.ingresar_datos()
                
            case 4:
                mostrar_mensaje_despedida()
                break
