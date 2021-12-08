n = int(input())
if n < 10000:
    for i in range(n):
        x = int(input())
        if (x > -10 ** 7) and (x < 10 ** 7):
            if x == 0:
                print('NULL')
            elif x > 0:
                if (x % 2 == 0):
                    print('EVEN POSITIVE')
                else:
                    print('ODD POSITIVE')
            else:
                if (x % 2 == 0):
                    print('EVEN NEGATIVE')
                else:
                    print('ODD NEGATIVE')
                