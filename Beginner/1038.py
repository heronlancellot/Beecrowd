cod = [[1, 4.00], [2, 4.5], [3, 5.0], [4, 2], [5, 1.5]]

vals = list(map(int, input().split()))

val1 = vals[0]
val2 = vals[1]

total = 0
for item in cod:
    if (val1 == item[0]):
        total += (item[1] * val2)

print("Total: R$ {:.2f}".format(total))
