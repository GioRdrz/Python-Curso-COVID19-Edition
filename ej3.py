# Manejo de numeros reales
# Caldula la longitud del ecuador utilizando pi y el radio de la tierra
pi = 3.1415926
radio_tierra = 6371
ecuador = pi*2*radio_tierra
volumen = 4/3*pi*radio_tierra**3
print("La longitud del ecuador es de {:.2f} kms".format(ecuador))
print("El volumen de la tierra es de {:.2f} km3".format(volumen))