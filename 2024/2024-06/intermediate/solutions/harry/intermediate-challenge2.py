def isPrime(input):
    if input == 2:
        return True

    for i in range(3, input, 2):
        if input % i == 0:
            return False
    return True


def getNextPrime(input):
    if input == 2:
        return 3
    while True:
        if isPrime(input) == True:
            return input
        else:
            input += 2


def divide(input):
    prime = 2
    while True:
        if (input / prime) % 1 == 0:
            return [prime, input // prime]
        else:
            prime = getNextPrime(prime)


def primeFactorization(input):
    output = []
    num = input
    while True:
        l = divide(num)
        output.append(l[0])
        num = l[1]
        if (isPrime(num)):
            output.append(num)
            return output


print(primeFactorization(56))
print(primeFactorization(45))
