i, j, stop = 1, 7, 4
cont = 0
while i < 10:
    for k in range(j, stop, -1):
        print('I={} J={}'.format(i, k))
        cont += 1
        if cont == 3:
            j += 2
            stop += 2
            cont = 0
    i += 2

