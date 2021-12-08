n = int(input())
cont, contf = 0, 0
if n < 10000:
    for i in range(n):
        x = int(input())
        if (x > -10 ** 7) and (x < 10 ** 7):
            if (x >= 10) and (x <= 20):
                cont += 1
            else:
                contf += 1
    print(cont, 'in')
    print(contf, 'out')
