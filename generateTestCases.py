from random import randint
from algorithms import Solution
from algorithms import isPrime0


n = 10000
with open('numbers.txt', 'w+') as f:
    f.write(str(n)+"\n")
    nums = []
    for i in range(n):
        num = randint(100,200000)
        f.write(str(num) + " " + str(Solution.isThree0(num)) + "\n")
print("  Done!")

