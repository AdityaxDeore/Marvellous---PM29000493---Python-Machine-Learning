# User-defined module named MarvellousNum containing ChkPrime() function.

def ChkPrime(No):
    if No <= 1:
        return False
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
    return True
