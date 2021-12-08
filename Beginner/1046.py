entrada = list(map(int,input().split()))
h0 = entrada[0]
hf = entrada[1]

if h0 == hf:
    print('O JOGO DUROU 24 HORA(S)')
elif h0 > hf:
    h0 = 24 - h0
    print('O JOGO DUROU {} HORA(S)'.format(h0 + hf))
else:
    print('O JOGO DUROU {} HORA(S)'.format(hf-h0))
