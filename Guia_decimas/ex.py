
def desglosar_vuelto(vuelto):
    bs = [10000, 5000, 2000, 1000, 500]
    ms = [100, 50, 10, 1]
    
    desglose = {}
    
    for b in bs:
        cantidad_b = vuelto // b
        if cantidad_b > 0:
            desglose[b] = cantidad_b
            vuelto = vuelto % b
    
    for m in ms:
        cantidad_m = vuelto // m
        if cantidad_m > 0:
            desglose[m] = cantidad_m
            vuelto = vuelto % m
    
    return desglose


def retirar_dinero(cajero):
    print("")
    print("---------------------[Retiro]--------------------")
    print("")
    print("Tienes en tu cuenta")
    print(f"${cajero} pesos")
    print("")
    cantidad = int(input("Ingrese la cantidad a retirar en pesos chilenos: "))
    print("")
    
    if cantidad <= cajero:
        cajero -= cantidad
        vuelto = desglosar_vuelto(cantidad)
        print("Retiraste", cantidad, "pesos.")
        print("Desglose del vuelto:")
        for b, cantidad_b in vuelto.items():
            print(cantidad_b, "billetes de", b, "pesos.")
        print("Quedan", cajero, "pesos en el cajero.")
        print("")
    else:
        print("-----------------[Intente Otravez]----------------")
        print("")
        print("No hay suficiente dinero en el cajero para retirar esa cantidad.")
    
    return cajero


def depositar_dinero(cajero):
    print("")
    print("-------------------[Deposito]-------------------")
    print("")
    cantidad = int(input("Ingrese la cantidad a depositar en pesos chilenos: "))
    
    cajero += cantidad
    print("Depositaste", cantidad, "pesos.")
    print("Total en el cajero:", cajero, "pesos.")
    print("")
    
    return cajero


def cajero_principal():
    cajero = 1000000
    
    while True:
        print("\n----------------[Menu]-------------------------")
        print("Bienvenido al cajero automático.")
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Cerrar sesión")
        
        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 1:
            cajero = retirar_dinero(cajero)
        elif opcion == 2:
            cajero = depositar_dinero(cajero)
        elif opcion == 3:
            print("")
            print("------------------[Cierre]----------------------")
            print("")
            print("Sesión cerrada. Gracias por utilizar el cajero automático.")
            print("")
            print("--------------------------------------------------")
            print("")
            break
        else:
            print("")
            print("-----------------[Intente Otravez]----------------")
            print("")
            print("Opción inválida. Por favor, seleccione una opción válida.")


# Ejemplo de uso:
cajero_principal()