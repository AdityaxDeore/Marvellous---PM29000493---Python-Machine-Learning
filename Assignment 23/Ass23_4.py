# Odd Number Count
# Count odd numbers between 1 and N using multiprocessing Pool.

import multiprocessing
import os


def OddCount(No):
    Count = 0

    for i in range(1, No + 1):
        if i % 2 != 0:
            Count = Count + 1

    return os.getpid(), No, Count


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()
    Result = pobj.map(OddCount, Data)
    pobj.close()

    for pid, no, ans in Result:
        print("Process ID:", pid)
        print("Input Number:", no)
        print("Odd Number Count:", ans)
        print()


if __name__ == "__main__":
    main()
