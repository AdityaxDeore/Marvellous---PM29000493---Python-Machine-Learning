import multiprocessing
import os

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calculate(n):
    fact = factorial(n)
    return os.getpid(),n,fact


def main():
    Data = [10,15,20,25]
    pobj = multiprocessing.Pool()
    Result = pobj.map(calculate, Data)

    print(Result)
    pobj.close()


if __name__ == "__main__":
    main()
