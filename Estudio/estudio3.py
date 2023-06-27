def funcion(x):
    return x*10

y=funcion(5)
print(f"el resultado de la funcion es", y)

def funcion1(z):
    return z*50

e=funcion1(5)
print(f"El resultado de la funcion es", e)

def saludo(nombre):
    print("Hola mi nombre es", nombre)

saludo("Tomás")

saludo("Fernanda")

def notas(nota1,nota2,nota3):
    sum=nota1+nota2+nota3
    return (sum/3)
    
nota1=float(input("Escriba una nota\n"))
nota2=float(input("Escriba una segunda nota\n"))
nota3=float(input("Escriba una tercera nota\n"))

calcular_notas= notas(nota1,nota2,nota3)
print(calcular_notas)

e=("Buenos dias")
print(e.upper())
print(e.lower())
print(e.swapcase())

def saludo(nombre1):
    print("Hola mi nombre es",nombre1)

saludo("Renata")

#Biblioteca 

#Que es una biblioteca

import numpy as np

lista=[1,2,5,7,9,10]
a=np.argmax(lista)
print(a)
ar=input("Ingrese su correo electronico\n")
def arroba(email):
    if "@" in email:
        return True
    else:
        return False

if arroba(ar):
    print("Correo electronico valido")
else:
    print("Correo electronico invalido")

numero1=input("Ingrese un numero")
numero2=input("Ingrese otro numero")

def max(num1,num2):
    if num1>num2:
        print("Es mayor", num1)
    else: 
        print("Es mayor", num2)    

max(numero1,numero2)















def max(num1,num2):
    if num2>num1:
        print("Es mayor", num2)
    if num1>num2: 
       print("Es mayor", num1)    
numero1=input("Ingrese un numero\n")
numero2=input("Ingrese otro numero\n")

max(numero1,numero2)
nume1=input("Ingrese un numero\n")
nume2=input("Ingrese un numero\n")                
nume3=input("Ingrese un numero\n")
def max3(j1,j2,j3):
    
    if j1>=j2 and j1>=j3: 
        return ("El numero mayor es",j1)
    elif j2>=j1 and j2<=j3:
        return ("El numero mayor es",j2) 
    if j3>=j2 and j3>=j1:
        return ("El numero mayor es",j3)
    


print(max3(nume1,nume2,nume3))

def cantidad(cadena):
    c=len(cadena)
    return ("La cantidad de caracteres es", c)

frase=input("Ingrese una palabra\n")    
cantidad1= cantidad(frase)
print (cantidad1)

