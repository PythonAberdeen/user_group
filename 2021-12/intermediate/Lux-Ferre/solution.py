from functools import wraps


def cooler(n):
    def decorator(func):
        @wraps(func)
        def wrapper():
            result = func() * (1 + n/100)
            return result
        return wrapper
    return decorator


def replace_arg(position, new_value):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            l = list(args)
            l[position] = new_value
            result = func(*l)
            return result
        return wrapper
    return decorator


def multi(func):
    @wraps(func)
    def wrapper(a, b):
        result = {}
        for x in a:
            for y in b:
                result[(x, y)] = func(x, y)
        return result
    return wrapper


def argmin(func):
    @wraps(func)
    def wrapper(a, b):
        input_dict = func(a, b)
        m = min(input_dict.values())
        result = set()

        for key in input_dict:
            if input_dict[key] == m:
                result.add(key)
        return result

    return wrapper


@cooler(20)
def cooler_ex():
    return 42


@replace_arg(position=0, new_value=21)
def multiply(a, b):
    return a * b


@multi
def add(x, y):
    return x + y


@argmin
@multi
def mul(x, y):
    return x * y


def main():
    print(cooler_ex())
    print(multiply(10, 2))
    print(add((1, 3, 5, 7), (10, 100)))
    print(mul((-5, 0, 5), (4, -4)))


if __name__ == '__main__':
    main()
