lista = [10,9,12,15,18]
list =  [21,8,15,3,12]

#Concatenar las dos listas
lista.extend(list)
print(lista)
#Agregar el numero 30 a la segunda posicion
lista.insert(2,30)
print(lista)
#Ordenar de forma ascendente
lista.sort()
print(lista)
#insertar la lista
lis1=[4,5,6]
lista.extend(lis1)
print(lista)
#Suma de los numeros dentro de la lista
print("La suma de los numeros es",sum(lista))
#Obtener la media
print("La cantidad de sus elementos es",len(lista))
print("Su media es", sum(lista)/14)
#Obtener la mediana
print("La posicion de su mediana al ser un numero par es",len(lista)/2)
print("Entonces su mediana es",lista[7])



