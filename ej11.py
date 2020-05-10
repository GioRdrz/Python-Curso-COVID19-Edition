cad =  "sometemos"

def esPalindromo(cad):
    for i in range(len(cad)):
        if cad[i] != cad[-i-1]:
            return False
    return True

print("{} es palindromo: {}".format(cad,esPalindromo(cad)))