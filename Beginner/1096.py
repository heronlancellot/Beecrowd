i = 1
j = 8
while i < 10:
    if j == 5:
        j = 8
        i += 2
    j -= 1
    if i == 11 and j == 7:
        break
    print('I={} J={}'.format(i, j))

