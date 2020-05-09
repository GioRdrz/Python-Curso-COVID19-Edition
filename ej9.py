print("Menu Interactivo")

msg = """
Escoge una de las siguientes opciones:
1) Sumar dos numeros.
2) Concatenar dos cadenas.
3) Comparar dos variables.
4) Salir

"""

while(True):
    print(msg)
    num = int(input("Ingresa tu elección: "))

    #Tu programa va aqui

    if num == 1:
        #Haz lo del caso 1
    elif num == 2:
        #Haz lo del caso 2
    elif num == 3:
        #Haz lo del caso 3

    #===================

    elif num == 4:
        break
    else:
        print("Ingresa una opción válida")

