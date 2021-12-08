a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
lis = [a, b, c, d, e]
pares = 0
impares = 0
positivos = 0
negativos = 0
nulos = True
for x in lis:
    if x % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
for x in lis:
    if x == 0:
        nulos = False
    elif x > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
print(pares,'valor(es) par(es)')
print(impares,'valor(es) impar(es)')
print(positivos,'valor(es) positivo(s)')
print(negativos,'valor(es) negativo(s)')
