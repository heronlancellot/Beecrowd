val = float(input())
lista = [[0,100],[0,50], [0,20], [0,10], [0,5], [0,2],[0,1], [0,0.50], [0,0.25],[0,0.10],[0,0.050],[0,0.01]]
moedas = True
if val >= 0 and val <= 1000000.00:
    print('NOTAS:')
    for item in lista:
        if val >= item[1]:
            if item[1] == 0.01:
                item[0] += val * 100
            else:
                item[0] += val // item[1]
                val = round(val - item[1] * item[0],2)
        if item[1] <= 1:
            if moedas:
                print('MOEDAS:')
                moedas = False
            print('{:.0f} moeda(s) de R$ {:.2f}'.format(item[0],item[1]))
        else:
            print('{:.0f} nota(s) de R$ {:.2f}'.format(item[0],item[1]))
