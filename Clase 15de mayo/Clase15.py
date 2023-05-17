#Condicionales
#OPERADORES ARITMETICOS
a=5
b=2
print("a=5 ,b=2")
ab=a+b
print("La suma entre a+b es",a+b)
g=9.81
t=5.39
print("velocidad es = a gravedad * tiempo")
print("v=g*t ")
v=g*t 
print(v)
c2=complex(3,-5)
print(c2.real)

print(c2)
#Multiplicar string por numero
print("Hola"*5)
#Operadores de comparacion
animaldomestico = "Gato"
Animalsalvaje="Leopardo"
print(animaldomestico!=Animalsalvaje)
print(animaldomestico<Animalsalvaje)
print(animaldomestico>Animalsalvaje)
print(animaldomestico<=Animalsalvaje)
print(animaldomestico>=Animalsalvaje)
#Operadores Logicos
bencina=True
encendido=True
edad=19
if bencina and encendido:
    print("El vehiculo puede avanzar")
else: 
  print("El vehiculo no puede avanzar")    
if bencina or encendido:
   print("El vehiculo puede avanzar")
else:print("El vehiculo no puede arrancar")       
if not bencina and encendido:
   print("El vehiculo no puede arrancar")


if not bencina or(encendido and edad>=18):
   print("El vehiculo puede arrancar")
else:
   print("El vehiculo no puede avanzar")   



