entrada = list(map(int,input().split()))
a = entrada[0]
b = entrada[1]
if b % a == 0 or a % b ==0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
    