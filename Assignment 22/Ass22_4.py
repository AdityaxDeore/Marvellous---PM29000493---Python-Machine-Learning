
import multiprocessing
import time


def SumPowerFive(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i ** 5)

    return Sum


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    StartTime = time.time()

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumPowerFive, Data)
    pobj.close()

    EndTime = time.time()

    print(Result)
    print("Total execution time is:", EndTime - StartTime)


if __name__ == "__main__":
    main()
