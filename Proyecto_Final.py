luz=60
est=91.96
valores=[]

def saludo():
    print ("Bienvenido, permitame calcular la carga eléctrica de su hogar \nDigite las cantidades correspondientes de los siguientes electrodomesticos:")
    return saludo

def next():
    input("Desea continuar? y/n ")
    return next

def info():
    entradas=[]
    a=int(input("luminarias: "))
    entradas.append(a)
    b=int(input("Nevera: "))
    entradas.append(b)
    c=int(input("Televisor: "))
    entradas.append(c)
    d=int(input("Sistema de sonido: "))
    entradas.append(d)
    e=int(input("Plancha: "))
    entradas.append(e)
    f=int(input("Horno microondas: "))
    entradas.append(f)
    g=int(input("Computador: "))
    entradas.append(g)
    h=int(input("Licuadora: "))
    entradas.append(h)
    i=int(input("Lavadora: "))  
    entradas.append(i)
    return entradas

hola=saludo()
continuar="y"
while continuar=="y":
    continuar=next()
    valores=info()
    valores[0]=(valores[0]*luz*180)
    valores[1]=(valores[1]*luz*5.5*450)
    valores[2]=(valores[2]*luz*2*150)
    valores[3]=(valores[3]*luz*1.5*120)
    valores[4]=(valores[4]*luz*12*20)
    valores[5]=(valores[5]*luz*9.5*150)
    valores[6]=(valores[6]*luz*2*150)
    valores[7]=(valores[7]*luz*3.5*30)
    valores[8]=(valores[8]*luz*3.5*16)
    total1=((sum(valores))/1000)
    total2=(total1*est)
    print ("el consumo de su hogar es de ",total1,"(kWats) mensuales con un costo de $", total2, " pesos")
    continuar=input("desea continuar y/n ")
if (continuar=="n"):
    print("Gracias, vuelva pronto")
else:
    print("Valor erroneo")