# Even Number Sum
# Calculate sum of all even numbers from 1 to N using multiprocessing Pool.

import multiprocessing
import os


def EvenSum(No):
    Sum = 0

    for i in range(2, No + 1, 2):
        Sum = Sum + i

    return os.getpid(), No, Sum


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()
    Result = pobj.map(EvenSum, Data)
    pobj.close()

    for pid, no, ans in Result:
        print("Process ID:", pid)
        print("Input Number:", no)
        print("Sum of Even Numbers:", ans)
        print()


if __name__ == "__main__":
    main()
