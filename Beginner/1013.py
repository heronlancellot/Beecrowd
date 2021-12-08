entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])
maiorab = (a + b + abs(a-b))/2
if maiorab > c:
    print('{:.0f} eh o maior'.format(maiorab))
else:
    print('{:.0f} eh o maior'.format(c))
