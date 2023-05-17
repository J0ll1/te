#Lista
lista=["Lunes","Martes","Miercoles", "Jueves","Viernes"]
print(lista)
#Como colocar un solo elemnto
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
#Que pasa si colocamos numeros negativos
print(lista[-1])#Da el ultimo numero
#Si queremos que se imprima solo una cantidad de elementos
print(lista[0:3])
print(lista[:2])
print(lista[2:])
#Funciones
#Convertir una lista en tupla, una tupla en lista
tupla=("Julio","Agosto","Septiembre")
lista1=tuple(lista)
print(lista1)
tupla1=list(tupla)
print(tupla1)
#Añadir un valor a una lista existente
lista.append(15)
print(lista)
#Colocar un valor en una posicion en especifico
lista.insert(2,32)
print(lista)
#Eliminar valores de una lista
lista.remove(15)
print(lista)
lista.pop(2)
print(lista)
#Pop retorna el valor que va a eliminar
#Limpiar una lista por completo
list1=["Julio","Agosto","Santiago"]
print(list1)
list1.clear()
print(list1)
#Contar la cantidad de elementos que existen en una lista
lista3=[2,3,4,5,6,7,8,9,2,2,2,2,2,2]
cantidad=lista3.count(2)
print(cantidad)
lista4=["Mayo","Junio","Julio"]
#Unir dos listas en una 
lista.extend(lista4)
print(lista)

