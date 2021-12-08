a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
lista = [a,b,c,d,e,f]
positivos = 0
for item in lista:
    if item > 0:
        positivos += 1
print("{} valores positivos" .format(positivos))
