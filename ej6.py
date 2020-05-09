
"""
cad = "El fin del socialismo"

for i in range(0,len(cad)):
    s = cad[0:i+1]
    print(s)
"""

"""
num_veces = 10
vez_actual = 0

while True:
    #Lo que me interesa repetir
    print("Hola")
    #==================
    vez_actual += 1
    if vez_actual == num_veces:
        break
"""

"""
#List Comprehension

num_1_20 = [i+1 for i in range(0,20)]
print(num_1_20)

cad = "El fin del socialismo"
subcadenas = [cad[0:i+1] for i in range(0,len(cad))]
print(subcadenas)
"""


animales = [
    {"raza":"perro","edad_media":10,"domesticable":True},
    {"raza":"gato","edad_media":12,"domesticable":False},
    {"raza":"pez","edad_media":2,"domesticable":True},
    {"raza":"pato","edad_media":14,"domesticable":False},
    {"raza":"ganso","edad_media":16,"domesticable":True}
]

"""
for n in range(0,len(animales)):
    if animales[n]["domesticable"] == True:
        raza = animales[n]["raza"]
        edad = animales[n]["edad_media"]
        print("Tengo un " + raza + " que tiene " + str(edad) + " años.")
"""

i = 0
maximo = len(animales)

while True:
    if i >= maximo:
        break
    if animales[i]["domesticable"] == True:
        raza = animales[i]["raza"]
        edad = animales[i]["edad_media"]
        print("Tengo un " + raza + " que tiene " + str(edad) + " años.")
    i += 1

"""
tjta_cred = "5579100025263656"
abc = "abcdefghijklmnopqrstuvwxyz"

def tarjeta_valida(num_tarjeta):
    es_valida = True

    if len(num_tarjeta) != 16:
        es_valida = False

    for i in range(0,len(num_tarjeta)):
        for j in range(0,len(abc)):
            if num_tarjeta[i] == abc[j]:
                es_valida = False
    return es_valida

def tarjeta_valida_usando_in(num_tarjeta):
    es_valida = True

    if len(num_tarjeta) != 16:
        es_valida = False

    for i in range(0,len(abc)):
        if abc[i] in num_tarjeta:
            es_valida = False

    return es_valida
"""

#print(tarjeta_valida_usando_in(tjta_cred))