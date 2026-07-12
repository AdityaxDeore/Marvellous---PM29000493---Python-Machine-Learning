
import multiprocessing


def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False

    return True


def CountPrime(No):
    Count = 0

    for i in range(1, No + 1):
        if ChkPrime(i):
            Count = Count + 1

    return Count


def main():
    Data = [10000, 20000, 30000, 40000]

    pobj = multiprocessing.Pool()
    Result = pobj.map(CountPrime, Data)
    pobj.close()

    print(Result)


if __name__ == "__main__":
    main()
