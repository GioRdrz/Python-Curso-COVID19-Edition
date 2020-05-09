"""
nombre = input("¿Cómo te llamas? ")
print("Hola {}".format(nombre))
"""

"""
num_a = int(input("Ingresa 'A': "))
num_b = int(input("Ingresa 'B': "))
print("La suma de {} y {} es: {}".format(num_a,num_b,num_a+num_b))
print("La resta de {} y {} es: {}".format(num_a,num_b,num_a-num_b))
print("La multplicacion de {} y {} es: {}".format(num_a,num_b,num_a*num_b))
print("La division de {} y {} es: {}".format(num_a,num_b,num_a/num_b))
"""

"""
    *
   **
  ***
 ****
*****

a = a + 1
a += 1

b = b - 4
b -= 4

c = c / 4.2
c /= 4.2

d = d * 9
d *= 9
"""

"""
n = int(input("Ingresa N: "))

for i in range(n):
    cad = ""
    for j in range(i+1):
        cad += "*"
    print(cad)
"""

vector = [1,2]
matriz = [
        [ 1, 2, 9,10,25],
        [ 4, 3, 8,11,24],
        [ 5, 6, 7,12,23],
        [16,15,14,13,22],
        [17,18,19,20,21]
    ]

def traza(matriz):
    tr = 0
    for i in range(len(matriz)):
        tr += matriz[i][i]
    return tr

print(traza(matriz))