def calcular_bono(sueldo, porcentaje):

    sueldo = int(sueldo)               
    porcentaje = float(porcentaje)     

    bono = sueldo * (porcentaje / 100)  
    total = sueldo + bono           

    print("==== Calculo de Bono ====")
    print("Sueldo base:", sueldo)
    print("Porcentaje de bono:", porcentaje)
    print("Sueldo total con bono:", total)

    return total  

 
