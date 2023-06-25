Set1 = {100, 250, 300, 1000}
Set2 = {150, 250, 500, 1000}

print("¿El numero 100 se encuentra en los dos sets?")

print(Set1.intersection(Set2))
print("Al buscar su interseccion no se encuentra en los dos")
print("Esta el numero 500 o 700 en los sets?")
print(500 in Set1 )
print(500 in Set2)
print(700 in Set2)
print(700 in Set2)



print(Set1.union(Set2))