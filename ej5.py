#Listas en Python 
l = ["a","e","i","o","u"]
meses = ["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]

#Diccionario
#Pares llave-valor
direccion = {"calle":"Abasolo","numero":52,"colonia":"Carrillo Puerto","ciudad":"Queretaro"}

alumnos = [
    {"nombre":"vivanco","edad":25,"feliz":"no"},
    {"nombre":"daniel","edad":25,"feliz":"no"},
    {"nombre":"jerry","edad":24,"feliz":"si"}
]

print(alumnos[2]["nombre"])

animales = [
    {"raza":"perro","edad_media":10,"domesticable":True},
    {"raza":"gato","edad_media":12,"domesticable":True},
    {"raza":"pez","edad_media":2,"domesticable":True},
    {"raza":"pato","edad_media":14,"domesticable":True},
    {"raza":"ganso","edad_media":16,"domesticable":True}
]

n = 0
if animales[n]["domesticable"] == True:
    raza = animales[n]["raza"]
    edad = animales[n]["edad_media"]
    print("Tengo un " + raza + " que tiene " + str(edad) + " años.")