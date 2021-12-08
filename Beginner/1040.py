notas = list(map(float,input().split()))
n1 = notas[0]
n2 = notas[1]
n3 = notas[2]
n4 = notas[3]
med = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print('Media: {:.1f}'.format(med))
if med >= 7.0:
    print('Aluno aprovado.')
elif med < 5.0:
    print('Aluno reprovado.')
elif med >= 5.0 and med <= 6.9:
    print('Aluno em exame.')
    nota_ex = float(input())
    med_ex = ((nota_ex + med) / 2)
    print('Nota do exame:',nota_ex)
    if med_ex >= 5.0:
        print('Aluno aprovado.')
        print('Media final: {}'.format(med_ex))
    else:
        print('Aluno reprovado.')
        print('Media final: {}'.format(med_ex))
    