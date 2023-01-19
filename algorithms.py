from math import sqrt


def isPrime0(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def isPrime1(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def isPrime2(n):
    if n == 1:
        return False
    vis = [0] * n
    for i in range(2, int(sqrt(n))+1):
        rem = n % i
        if not rem or vis[rem]:
            return False
        vis[n-rem] = 1
    return True

def isPrime3(n):
    dd = [0] * n
    prev_b = 2
    a, b = 2, n//2
    rem = n % (a*b)
    while a <= b:
        if rem == 0 or rem == b:
            return False
        if dd[rem]:
            return False
        else:
            dd[n-rem] = 1
        while b == prev_b:
            a += 1 + (((b+rem) % a)//a)
            b = n // a
            rem = n % (a*b)
        prev_b = b
    return True

def isPrime4(n):
    prev_b = 2
    a, b = 2, n//2
    rem = n % (a*b)
    while a <= int(sqrt(n))+1:
        if rem == 0 or rem == b:
            return False
        while b == prev_b:
            a += 1 + (((b+rem) % a)//a)
            b = n // a
            rem = n % (a*b)
        prev_b = b
    return True

def isPrime5(n):
    a, b = 2, n//2
    rem = n % (a*b)
    while a <= int(sqrt(n))+1:
        if rem == 0 or rem == b:
            return False
        a += 1 + (((b+rem) % a)//a)
        b = n // a
        rem = n % (a*b)
    return True


class Solution:

    def isThree0(n: int) -> bool:
        if n < 3:
            return False
        n = sqrt(n)
        return n == (n//1) and isPrime1(n)

    def isThree1(n: int) -> bool:
        if n < 3:
            return False
        n = sqrt(n)
        return n == (n//1) and isPrime1(n)

    def isThree2(n: int) -> bool:
        if n <= 3:
            return False
        sqrt_n = sqrt(n)
        return sqrt_n == int(sqrt_n) and isPrime2(int(sqrt_n))

    def isThree3(n: int) -> bool:
        if n <= 3:
            return False
        sqrt_n = sqrt(n)
        return sqrt_n == int(sqrt_n) and isPrime3(int(sqrt_n))

    def isThree4(n: int) -> bool:
        if n <= 3:
            return False
        sqrt_n = sqrt(n)
        return sqrt_n == int(sqrt_n) and isPrime4(int(sqrt_n))

    def isThree5(n: int) -> bool:        
        if n <= 3:
            return False
        sqrt_n = sqrt(n)
        return sqrt_n == int(sqrt_n) and isPrime5(int(sqrt_n))




