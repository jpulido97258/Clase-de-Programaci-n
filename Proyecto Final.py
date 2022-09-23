#welcome al control parental o programa para prohibir a nuestros menores de edad
lista=["gonorrea , zunga , huevón , lámpara , garbimba , guiso , cachon , sapo , baboso , cacorro, gurrupleta, hijueputa , idiota, imbecil , malparido , mamerto"]#Palabras genricas para bloquear

palabra=input("Palabra o comando que desees prohibir: ")#nueva palabra para bloquear

lista.append(palabra)

palabra2=input("Palabra o comando permitido: ")#palabra sin necesidad de bloquear 



if palabra==lista and lista==palabra:
    print("Palabra o comando bloqueado"+str(palabra))
