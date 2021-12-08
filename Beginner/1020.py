n = int(input())
anos = n // 365
resto = n % 365
meses = resto // 30
resto = resto % 30
dias = resto
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
