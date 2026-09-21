numeros = list(map(int, input("Introduce números para saber si son pares o impares separados por espacios: ").split()))

pares = [n for n in numeros if n % 2 == 0]

impares = [n for n in numeros if n % 2 != 0]

print("Números pares:", pares)

print("Números impares:", impares)