entrada = list(map(float,input().split()))
a = entrada[0]
b = entrada[1]
c = entrada[2]
if a < b + c and b < a + c and c < a + b:
    area = b * c / 2
    perimetro = a + b + c
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area = ((a + b)* c) / 2
    print('Area = {:.1f}'.format(area))
    