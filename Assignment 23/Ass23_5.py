# Factorial
# Calculate factorials of multiple numbers using multiprocessing Pool.

import multiprocessing
import os


def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return os.getpid(), No, Fact


def main():
    Data = [10, 15, 20, 25]

    pobj = multiprocessing.Pool()
    Result = pobj.map(Factorial, Data)
    pobj.close()

    for pid, no, ans in Result:
        print("Process ID:", pid)
        print("Input Number:", no)
        print("Factorial:", ans)
        print()


if __name__ == "__main__":
    main()
