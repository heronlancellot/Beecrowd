n1 = int(input())
n2 = int(input())
soma = 0
for n in range((n2+1),n1):
    if n % 2 != 0:
        soma += n
print(soma)
