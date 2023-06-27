print("Calculadora de triangulos")
lado1=float(input("Ingrese primer lado del triangulo\n"))
lado2=float(input("Ingrese segundo lado del triangulo\n"))
lado3=float(input("Ingrese tercer lado del triangulo\n"))
if lado1==lado2 and lado2==lado3:
    print("El triangulo es equilatero\n")
elif lado1==lado2 or lado2==lado3 or lado3==lado1:
    print("El triangulo es isoceles\n")
else:
   print("El triangulo es escaleno")   
   
p=lado1+lado2+lado3
p1=p/2
print(p1)
Area = p1*(p1 - lado1) * (p1 - lado2 ) * (p1 - lado3)
Area1=Area**0.5
print("El area del triangulo es", round(Area1))