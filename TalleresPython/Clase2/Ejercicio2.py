# Este programa te dice si eres mayor de edad ademas de pedir tu nombre y apellido

#aqui defino las variables de una vez.
nombre = "";
apellido = "";
edad = 0;

#aqui solicito los datos del nombre
print("Escribe tu nombre(sin apellido): ");
nombre = input();
print("Ingresa ahora tu apellido: ");
apellido = input();

#aqui solicito la edad
print("Hola", nombre , apellido, ", Escribe tu edad por favor: " );
edad = int(input()); #aqui se transforma lo que ingresa el usuario a entero para poder lo verificar en el If

if edad >= 18:
    print("Veo que eres mayor de edad");
else: 
    print("Eres menor de edad");

