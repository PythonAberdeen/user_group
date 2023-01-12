from time import time


def fib(n):
    # only positive numbers
    return n if n <= 1 else (fib(n-1) + fib(n-2))


def fib_neg(n):
    #  positive and negative
    if -1 <= n <= 1:
        return n
    else:
        if n > 0:
            return fib_neg(n - 1) + fib_neg(n - 2)
        else:
            return fib_neg(n + 1) + fib_neg(n + 2)


start = time()
tmp = []
for i in range(100):
    tmp.append(fib(i))

print("Overall time:", time() - start)
