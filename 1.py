import math
a, b = float(input("Inserte el valor del cateto a: ")), float(input("Inserte el valor del cateto b: "))
hipotenusa = math.sqrt((a**2) + (b**2))
print("La hipotenusa es: " + str(hipotenusa))