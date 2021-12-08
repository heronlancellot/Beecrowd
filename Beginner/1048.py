sal = float(input())
if sal >= 0 and sal <= 400.00:
    newsal = sal * 1.15
    print('Novo salario: {:.2f}'.format(newsal))
    print('Reajuste ganho: {:.2f}'.format(newsal - sal))
    print('Em percentual: {} %'.format('15'))
elif sal >= 400.01 and sal <= 800.00:
    newsal = sal * 1.12
    print('Novo salario: {:.2f}'.format(newsal))
    print('Reajuste ganho: {:.2f}'.format(newsal - sal))
    print('Em percentual: {} %'.format('12'))
elif sal >= 800.01 and sal <= 1200.00:
    newsal = sal * 1.10
    print('Novo salario: {:.2f}'.format(newsal))
    print('Reajuste ganho: {:.2f}'.format(newsal - sal))
    print('Em percentual: {} %'.format('10'))
elif sal >= 1200.01 and sal <= 2000.00:
    newsal = sal * 1.07
    print('Novo salario: {:.2f}'.format(newsal))
    print('Reajuste ganho: {:.2f}'.format(newsal - sal))
    print('Em percentual: {} %'.format('7'))
else:
    newsal = sal * 1.04
    print('Novo salario: {:.2f}'.format(newsal))
    print('Reajuste ganho: {:.2f}'.format(newsal - sal))
    print('Em percentual: {} %'.format('4'))
    