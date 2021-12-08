a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
lista = [a,b,c,d,e]
par= 0
for item in lista:
    if item % 2 == 0:
        par += 1
print(par,"valores pares")
