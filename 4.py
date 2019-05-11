def isPolindrome(num):
    raw = str(num)
    rNum = int(raw[::-1])
    if rNum == num:
        return True
    else:
        return False

pol = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if isPolindrome(i*j):
            pol.append(i*j)
#print(pol)
print("max = %d" % max(pol))