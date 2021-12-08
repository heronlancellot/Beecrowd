sal = float(input())
if sal >= 0 and sal <= 2000.00:
    print('Isento')
elif sal >= 2000.01 and sal <= 3000.00:
    sal = (sal - 2000.01) * 0.08
    print('R$ {:.2f}'.format(sal))
elif sal >= 3000.01 and sal <= 4500.00:
    sal = 79.9992 + ((sal - 3000.0) * 0.18)
    print('R$ {:.2f}'.format(sal))
else:
    sal = 349.9974 + ((sal - 4500.00) * 0.28)
    print('R$ {:.2f}'.format(sal))
    