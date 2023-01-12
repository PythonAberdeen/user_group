LIMIT = 28123
DIVISORS = {}

def is_perfect(num):
    return sum(divisors(num)) == num

def divisors(num):
    # We started working on saving results to reduce duplicate
    # computation but it isn't complete so DIVISORS doesn't help any
    # here
    result = DIVISORS.get(num)
    if result is None:
        result = [i for i in range(1, num) if num%i==0]
        DIVISORS[num] = result
    return result

def is_abundant(num):
    return sum(divisors(num)) > num

def limit_finder(n, abundant_sums=None):
    if abundant_sums == None:
        abundant_sums = []
    if n == LIMIT:
        return sum(abundant_sums)
    for i in range(n):
        limit_finder(i)

if __name__=="__main__":
    abundant = [is_abundant(i) for i in range(LIMIT)]
    abundant_nums = [i for (i, x) in enumerate(abundant) if x]
    expressible = [False] * LIMIT
    for i in abundant_nums:
        for j in abundant_nums:
            if i+j >= LIMIT: break
            expressible[i+j] = True
    print(sum([i for (i, x) in enumerate(expressible) if not x]))
