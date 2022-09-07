# funcion multivariable
def imc(masa, estatura):
    resultado = masa/(estatura**2)
    return resultado

print("Ingresa tu peso");
weight = float(input());
print("ingresa tu estatura en metros, separa con un punto.");
height = float(input());

res = imc(weight, height);


print("Tu imc es de: " , res);

if res < 18.5:
    print("Tu peso es mas bajo de lo normal");
elif res < 24.9:
    print("Tu peso esta en el rango normal");
elif res < 29.9:
    print("Tienes sobrepeso, pero no obesidad");
else:
    print("tienes obesidad");