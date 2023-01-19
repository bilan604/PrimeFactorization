from algorithms import Solution
from timeit import default_timer


def check(numbers, function, answers):
    ans = [False] * len(numbers)
    s = default_timer()
    for i in range(len(numbers)):
        if function(numbers[i]):
            ans[i] = True
    t = default_timer()
    print(f"{function}: {100*(t-s)}")
    print("Error:", sum([0 if ans[i] == answers[i] else 1 for i in range(len(answers))])/len(answers))
    return ans


numbers = []
answers = []
with open("numbers.txt", "r") as f:
    n = int(f.readline().strip())
    for i in range(n):
        row = f.readline().strip()
        row = row.split(" ")
        numbers.append(int(row[0]))
        answers.append(row[1] == "True")


ans_isPrime1 = check(numbers, Solution.isThree1, answers)
ans_isPrime2 = check(numbers, Solution.isThree2, answers)
ans_isPrime3 = check(numbers, Solution.isThree3, answers)
ans_isPrime4 = check(numbers, Solution.isThree4, answers)
ans_isPrime4 = check(numbers, Solution.isThree5, answers)