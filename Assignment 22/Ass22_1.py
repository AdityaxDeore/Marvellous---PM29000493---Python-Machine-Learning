import multiprocessing


def SumOfSquares(No):
    total = 0

    for i in range(1, No + 1):
        total = total + (i * i)

    return total


def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumOfSquares, Data)
    pobj.close()

    print(Result)


if __name__ == "__main__":
    main()
