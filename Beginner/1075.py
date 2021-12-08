n = int(input())
lista = []
for i in range(1,10000):
    if i % n == 2:
        lista = i
        print(lista)
        