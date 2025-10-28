import datos        
import bono         
import resumen      

def mostrar_mensaje_despedida():
    print("\nGracias por usar PyCompany. ¡Hasta pronto!")

def menu():
    nombre = ""
    edad = 0
    cargo = ""
    sueldo_base = 0
    porcentaje_bono = 0.0
    total = 0

    while True:
        print("\n=== Menú Principal de PyCompany ===")
        print("1) Registrar información del empleado")
        print("2) Calcular bono")
        print("3) Mostrar resumen del trabajador")
        print("4) Salir del programa")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            nombre, edad, cargo, sueldo_base, porcentaje_bono = datos.ingresar_datos()

        elif opcion == 2:
            if sueldo_base > 0:
                total = bono.calcular_bono(sueldo_base, porcentaje_bono)
            else:
                print("❎ Primero debe registrar un empleado.")

        elif opcion == 3:
            if total > 0:
                resumen.mostrar_resumen(nombre, edad, cargo, total)
            else:
                print("❎ Debe calcular el bono antes (opción 2).")

        elif opcion == 4:
            mostrar_mensaje_despedida()
            break

        else:
            print("❎ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()