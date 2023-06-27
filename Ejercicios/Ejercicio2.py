palabra1=input("Ingrese primera palabra\n")
palabra2=input("ingrese segunda palabra\n")
print(len(palabra1))
print(len(palabra2))
if len(palabra1)<len(palabra2):
    print (palabra2,"es mayor en numero de caracteres")
elif len(palabra1)>len(palabra2):
     print(palabra1,"es mayor en numero de caracteres")    
