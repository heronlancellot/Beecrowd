lista_i = []
lista_j = []
for i in range(1, 38, 3):
    lista_i.append(i)
for j in range(60, 0 - 1, -5):
    lista_j.append(j)
for i in range(len(lista_i)):
    print('I={} J={}'.format(lista_i[i], lista_j[i]))