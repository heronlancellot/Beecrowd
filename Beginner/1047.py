entrada = input().split()
hi = int(entrada[0])
mi = int(entrada[1])
hf = int(entrada[2])
mf = int(entrada[3])
h = hf - hi
m = mf - mi
if  h == 0 and m == 0:
    h = 24
    m = 0
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h,m))
else:
    if  h < 0:
        h += 24
    if  m < 0:
        m += 60
        h -= 1
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))
    