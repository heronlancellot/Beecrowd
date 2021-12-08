lista = list(map(int, input().split()))
a = lista[0]
b = lista[1]
c = lista[2]
listaAux = lista.copy()
for i in range(len(listaAux)):
     for k in range(i+1, len(listaAux)):
        if (listaAux[i] > listaAux[k]):
            elemento = listaAux[i]
            listaAux[i] = listaAux[k]
            listaAux[k] = elemento

for item in listaAux:
    print(item)

print("")

for item in lista:
    print(item)
