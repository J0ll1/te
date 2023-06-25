#   Cajero de supermercado

# Primero hacemos una funcion que permita desglosar la cantidad de billetes con una lista
def calcular_vuelto(monto, pago):
    billetes = [20000,10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1]
    desglose = {}
    vuelto = pago - monto

    for billete in billetes:
        if vuelto >= billete:
            cantidad = vuelto // billete
            desglose[billete] = cantidad
            vuelto -= cantidad * billete

    return desglose

#Creamos un input para escoger un producto de la categoria estipulada
producto=int(input("Ingrese un numero para escoger un producto 1)Audifonos 2)Poleron 3)Zapatillas\n"))

#Un if por cada producto, el primer if es para dar a conocer que escogio 
#El segundo para imprimir la funcion ya estipulada si el monto para pagar es correcto, si no, no existe venta
if producto==1:
    print("Usted escogio audifonos su precio es 5000 mil pesos")
    pago_realizado=int(input("Con cuanto desea usted pagar\n"))
    monto_total=5000
    resultado = calcular_vuelto(monto_total, pago_realizado)
    if pago_realizado>monto_total:
       print("Su vuelto en billetes y/o monedas es", resultado)  
    elif pago_realizado<monto_total:
        print("Ingrese un valor valido")
elif producto>3:
    print("Escoga un numero valido")

if producto==2:
    print("Usted escogio poleron su precio es 25.990 mil pesos")
    pago_realizado=int(input("Con cuanto desea usted pagar\n"))
    monto_total=25990
    resultado = calcular_vuelto(monto_total, pago_realizado)
    if pago_realizado>monto_total:
        print("Su vuelto en billetes y/o monedas es", resultado)
    elif pago_realizado<monto_total:
        print("Ingrese un valor valido")
elif producto>3:
    print("Escoga un numero valido")

if producto==3:
    print("Usted escogio zapatillas 70500 mil pesos")
    pago_realizado=int(input("Con cuanto desea usted pagar\n"))
    monto_total=70500
    resultado = calcular_vuelto(monto_total, pago_realizado)
    if pago_realizado>monto_total:
        print("Su vuelto en billetes y/o monedas es", resultado)
    elif pago_realizado<monto_total:
        print("Ingrese un valor valido")
elif producto>3:
    print("Escoga un numero valido")

#Fin algoritmo


  

    