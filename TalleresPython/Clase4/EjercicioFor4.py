#otro ejemplo para el bucle for

nums = ["A","B","C","D","E","F","G","H","J","K"];

for e in nums:
    if e == "I":
        print("Nos detuvimos en I");
        break
    print(e);
else:
    print("La letra I no se encontro");