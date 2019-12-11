from tqdm import tqdm

def rfibs(n):
    if n == 0:
        return n
    if n == 1:
        return 1
    return rfibs(n - 1) + rfibs(n - 2)

def lfibs(target):
    a, b = 0, 1
    for i in tqdm(range(0, target)):
        a, b = b, a + b

    return a

def bifibs(target):
    if target == 0:
        return 0

    if target > 0:
        a, b = 0, 1
        for i in tqdm(range(0, target)):
            a, b = b, a + b,
        return a

    if target < 0:
        a, b = 0, -1
        for i in tqdm(range(0, target, -1)):
            a, b = b, a + b
        return a

def bitribonaci(target):
    if target == 0:
        return 0

    if target > 0:
        a, b,c = 1, 1, 1
        for i in tqdm(range(0, target)):
            a, b, c = b, a + b + c, 
        return a

    if target < 0:
        a, b = 0, -1
        for i in tqdm(range(0, target, -1)):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    print(f"{rfibs(10)}")
    print(f"{lfibs(100)}")
    print(f"{bifibs(0)}")
    print(f"{bifibs(2)}")

