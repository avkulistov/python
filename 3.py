import time
import math

def isSimple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    a = 600851475143
    i = 1
    m = 0
    while i <= math.ceil(math.sqrt(a)):
        if (a % i == 0) and (isSimple(i)):
            m = i
            print(i)
        i += 1
    print('max = ' + str(m))

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))