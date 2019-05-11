a = 1
b = 1
c = 0
summ = 0
print(a, end = ' ')
while True:
    c = a + b
    if c >= 4000000:
        break
    print(c, end = ' ')
    if c % 2 == 0:
        summ += c
    a = b
    b = c
print()
print('summ = ' + str(summ))