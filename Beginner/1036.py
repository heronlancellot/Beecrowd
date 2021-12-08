entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])
delta = b ** 2 - 4 * a * c
if (b ** 2 - 4 * a * c) < 0 or a == 0.0:
    print('Impossivel calcular')
else:
    x1 = (-b +(delta)**(1/2))/(2*a)
    x2 = (-b -(delta)**(1/2))/(2*a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
    