print("Bienvenido a su agenda telefonica personal ingrese nuevo contacto")
nombre=input("Ingrese nombre\n")
direccion=input("Ingrese su direccion\n")
ciudad=input("Ingrese la ciudad\n")
tel=input("Ingrese numero telefonico\n")
datos={"nombre":nombre,
       "Direccion":direccion,
       "Ciudad":ciudad,
       "Numero telefonico":tel}
print(datos)
clave=input("Redes sociales ingrese un numero 1)Facebook,2)Instagram,3)Twiter\n")

if clave=="1":
    rad=input("Ingrese nombre de facebook\n") 
    print("Facebook",rad)
elif clave=="2":
    red1=input("Ingrese nombre de instagram\n")
    print("Instagram",red1)
if clave=="3":
    red2=input("Ingrese Nombre de Twiter\n")
    print("Twiter",red2)
      

