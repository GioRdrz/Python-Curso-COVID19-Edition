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
    esEntero = True
    try:
        num = int(input("Ingresa tu elección: "))
    except:
        esEntero = False
        print("Ingresa un valor entero valido")

    if esEntero:
        #Tu programa va aqui

        if num == 1:
            #Haz lo del caso 1
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            print("La suma de tus dos numeros es: {}".format(num1 + num2))
        elif num == 2:
            #Haz lo del caso 2
            cad1 = input("Ingresa la primera cadena: ")
            cad2 = input("Ingresa la segunda cadena: ")
            print("La concatenacion de las cadenas es: {}".format(cad1 + cad2))
        elif num == 3:
            #Haz lo del caso 3
            var1 = input("Ingresa la primera variable: ")
            var2 = input("Ingresa la segunda variable: ")
            if var1 == var2:
                print("Las variables son iguales.")
            else:
                print("Las variables son diferentes.")
        #===================

        elif num == 4:
            break
        else:
            print("Ingresa una opción válida")

