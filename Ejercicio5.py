print("Notas asignatura programacion")

nota1=float(input("Ingrese primera nota\n"))
nota2=float(input("Ingrese segunda nota\n"))
nota3=float(input("ingrese tercera nota\n"))
Promedio=nota1*0.3+nota2*0.4+nota3*0.3
print("El promedio ponderado de la asignatura es",Promedio)
if Promedio<4.0:
    print("El estudiante reprobo la asignatura")

if Promedio>4.0 and Promedio<6.0:
    print("El estudiante aprobo la asignatura")

if Promedio>6.0:
    print("El estudiante aprobo con distinción")