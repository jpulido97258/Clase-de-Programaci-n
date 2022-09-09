# Este programa es un intento de login

# aqui defino las variables que voy a utilizar
cuenta = False;
nombre = "";
contraseña = "";
loged = False;
intentos = 0;

inpNombre = "";
inptContra = "";

print("Bienvenido a Py.com");

while loged == False and intentos != 3: #Este while verifica que no esten logeados y los intentos no sean iguales a 3
    if cuenta: #este if verifica si existe una cuenta.
        print("parece que ya tienes una cuenta, vamos a iniciar sesion") 
        for e in nombre: #este bucle se repite no se cuantas veces la verdad, pero funciona.
            inpNombre = input("Escribre tu nombre de usuario: ")
            if nombre == inpNombre:
                print("El usuario es correcto.")
                break #aqui si el usuario es correcto el bucle se rompe.
            print("El usuario es incorrecto")
            intentos = intentos +1
            if intentos == 3: #esta parte hace que si el bucle se repite 3 veces sin exito se "bloquee" la cuenta (se detiene el programa)
                print("La cuenta se ha bloqueado por llegar al numero maximo de intentos")
                break
        
        if nombre == inpNombre:
            for e in contraseña:
                inptContra = input("Escribe tu contraseña:")
                if inptContra == contraseña:
                    print("Contraseña correcta")
                    print("Sesion iniciada")
                    loged = True    
                    break # aqui si la contraseña es correcta se rompe el bucle for
                print("Contraseña incorrecta")
                intentos = intentos +1
                if intentos == 3: #esta parte hace que si el bucle se repite 3 veces sin exito se "bloquee" la cuenta (se detiene el programa)
                    print("La cuenta se ha bloqueado por llegar al numero maximo de intentos")
                    break
    else: # si no se tiene una cuenta aqui se crea.
        print("no tienes una cuenta, vamos a registrarnos")
        nombre = input("Ingresa un nombre de usuario: ")
        contraseña = input("Ingresa una contraseña: ")
        
        if nombre != "" and contraseña != "":
            cuenta = True;

