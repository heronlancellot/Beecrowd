entrada = input().split()
val = float(entrada[0])
lim1 = val >= 0 and val <= 25.0000
lim2 = val > 25 and val <= 50.0000000
lim3 = val > 50 and val <= 75.0000000
lim4 = val > 75 and val <= 100.000000
if lim1:
    print('Intervalo [0,25]')
elif lim2:
    print('Intervalo (25,50]')
elif lim3:
    print('Intervalo (50,75]')
elif lim4:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
