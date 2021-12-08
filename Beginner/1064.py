a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
vals = [a, b, c, d, e, f]
positivo = 0
soma = 0
for item in vals:
    if item > 0:
        positivo += 1
        soma += item
print('{} valores positivos'.format(positivo))
print('{:.1f}'.format(soma / positivo))
