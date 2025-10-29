def ingresar_datos():
    print("\n=== Registro de Empleado ===")

    nombre = input("Nombre: ").strip()
    while nombre == "" or nombre[0] >= "0" and nombre[0] <= "9":
        nombre = input("❎ Ingrese un nombre válido: ").strip()

    edad = input("Edad: ").strip()
    while edad == "" or edad[0] < "0" or edad[0] > "9" or int(edad) < 18:
        edad = input("❎ Ingrese una edad válida (18 o más): ").strip()
    edad = int(edad)

    cargo = input("Cargo: ").strip()
    while cargo == "" or cargo[0] >= "0" and cargo[0] <= "9":
        cargo = input("❎ Ingrese un cargo válido: ").strip()

    sueldo = input("Sueldo base: ").strip()
    while sueldo == "" or float(sueldo) <= 0:
        sueldo = input("❎ Ingrese un sueldo mayor que 0: ").strip()
    sueldo = float(sueldo)

    bono = input("Porcentaje de bono: ").strip()
    while bono == "" or float(bono) <= 0:
        bono = input("❎ Ingrese un porcentaje mayor que 0: ").strip()
    bono = float(bono)

    return nombre, edad, cargo, sueldo, bono
