x = int(input())
val = [x]
par = []
impar = []
for i in range(x, x + 12, 1):
    if i % 2 == 0:
        par = i
    else:
        impar = i
        print(impar)
        