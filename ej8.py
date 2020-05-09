import math

maxPos = 10.0
step = 0.1
pos = 0.0
amplitud = 30

while True:
    pos += step
    if pos > maxPos:
        break

    print(" "*int(amplitud*(math.sin(pos)+1))+"*")