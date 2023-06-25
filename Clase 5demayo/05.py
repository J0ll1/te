#Desafio

Nombre=input("Ingrese nombre del estudiante\n")
Asignatura=input("Ingrese nombre de la asignatura\n")
nota1=float(input("Ingrese primera nota\n"))
nota2=float(input("Ingrese segunda nota\n"))
Promedio_final=float(nota1*0.30)+(nota2*0.70)
datos_personales={"Nombre":Nombre,
                  "Asignatura":Asignatura,
                  "Nota 1":nota1,
                  "Nota 2":nota2,
                  "Promedio":round(Promedio_final,1)}
print(datos_personales)

