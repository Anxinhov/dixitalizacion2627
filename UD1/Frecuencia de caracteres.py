palabra =input("Escribe una palabra: ")
diccionario = {}
contador = int (0)
for n in palabra:
    for m in palabra:
        if n==m: contador = contador +1
    if not n in diccionario:
        diccionario[n]=contador
        print(n, '\t', contador)
    contador = 0