def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def potencia(a,b):
    return a**b

def factorial(n):
    if(n==0):
        return 1
    else:
        return n * factorial(n-1)

texto = "The economic anarchy of capitalist society as it exists today is, in my opinion, the real source of the evil."

def subcadena(texto,posFinal):
    t = texto[:posFinal]
    print(t)
    if(posFinal+1 > len(texto)):
        return
    subcadena(texto,posFinal+1)

subcadena(texto,1)