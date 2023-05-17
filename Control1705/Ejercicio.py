#Datos:
id=8
id1=10
nombre="Bio-Bio"
nombre1="Los lagos"
superficie=23890
superficie1=48593
habitantes=1556805
habitantes1=828708
capital="Concepcion"
capital1="Puerto Montt"
Densidad=habitantes/superficie
Densidad1=habitantes1/superficie
Comunas=["Lota", "Lebu","Los angeles"]
comunas1=["Castro", "Puerto Varas", "Purranque"]
provi=("Biobío", "Arauco","Concepción")
provi1=("Osorno", "Llanquihue","Chiloé", "Palena")




#Diccionarios:

datos={"ID De Region":id,
       "Nombre de la region":nombre,
          "Superficie total": superficie,
             "Cantidad de habitantes":habitantes}
datos1={"ID De Region":id1,
       "Nombre de la region":nombre1,
          "Superficie total": superficie1,
             "Cantidad de habitantes":habitantes1}


#Diccionarios con las nuevas claves

datos2={"ID De Region":id,
       "Nombre de la region":nombre,
          "Superficie total": superficie,
             "Cantidad de habitantes":habitantes,
               "Densidad poblacional":Densidad,
               "Capital":capital,
               "Comunas":Comunas,
               "Provincia":provi}

datos3={"ID De Region":id1,
       "Nombre de la region":nombre1,
          "Superficie total": superficie1,
             "Cantidad de habitantes":habitantes1,
             "Densidad poblacional":Densidad1,
             "Capital":capital1,
             "Comunas":comunas1,
             "Provincia":provi1}

print("Datos de la region de Bio-Bio\n")
print(datos)

print("Datos de la region de los Lagos\n")
print(datos1)

print("Datos Actualizados de la region del Bio-Bio\n")
print(datos2)

print("Datos Actualizados de la region de los Lagos\n")
print(datos3)