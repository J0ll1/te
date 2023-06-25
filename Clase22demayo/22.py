#Condicionales
edad=18
if edad>=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad") 

#Operadores ternarios
#Una expresion condicional en una sola linea
edad=19
print("Usted puede votar" if edad >=18 else "Usted no puede votar")

#Bucles: Condiciones que permiten ejectuar un codigo las veces que se necesite
#Dos tipos de ciclos
#Iteraciones: Cantidad de veces que se repite
#1 Iteraciones definidas
#2 Iteraciones no definidas
#While #Iteraciones no definidas
#For #Interaciones definidas
 
#ejemplo de While

num=0

while num<=100:
    print(num)
    num+=2
#Definido

#While infinito
# while True:
# print(num)
# num+=2

#Combinar un bucle con una condicional

while num<=100:
    print(num)
    num+=2
else:
    print("Mi condicion es igual o mayor a 100")

#For
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)
for lis in lista:
    print(lis)
for i in range (1,11):
    print(i)

