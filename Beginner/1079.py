n = int(input())
while n > 0:
    casos = list(map(float, input().split()))
    c1 = casos[0] * 2
    c2 = casos[1] * 3
    c3 = casos[2] * 5
    media = (c1 + c2 + c3) / 10
    n -= 1
    print("{:.1f}".format(media))
    