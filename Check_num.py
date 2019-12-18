import math
import random

def quickMult(a, b, c):
    result = 0
    while b > 0:
        if b & 1:
            result = (result + a) % c
        a = (a + a) % c
        b >>= 1
    return result

def quickPower(a, b, c):
    result = 1
    while b > 0:
        if (b & 1):

            result = quickMult(result, a, c)
        a = quickMult(a, a, c)
        b >>= 1
    return result


def MillerRabinPrimeTest(n):
    a = random.randint(2,n-2)
    s = 0
    d = n - 1
    while (d & 1) == 0:
        s += 1
        d >>= 1
 
    x = quickPower(a, d, n)
    for i in range(s):
        newX = quickPower(x, 2, n)
        if newX == 1 and x != 1 and x != n - 1:
            return False #用二次定理的逆否命题，此时n确定为合数。
        x = newX
 
    if x != 1:  # 用费马小定理的逆否命题判断，此时x=a^(n-1) (mod n)，那么n确定为合数。
        return False
 
    return True  # 用费马小定理的逆命题判断。能经受住考验至此的数，大概率为素数。
 
 
# 经过连续特定次数的Miller-Rabin测试后，
# 如果返回值为TRUE表示n为素数，返回值为FALSE表示n为合数。
def isPrimeByMR(n):
    if ((n & 1) == 0 or n % 5 == 0):
        return False
    for i in range(100):
        if MillerRabinPrimeTest(n) == False:
            return False
    return True




