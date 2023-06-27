def vocal(g):
    vocales=['a','e','i','o','u']
    if vocales in g:
        return ("Es una vocal")
    else:
       return ("Es una consonante")

letra=input("Ingrese una letra para saber si es vocal o consonante\n")
t=vocal(letra)
print(t)
