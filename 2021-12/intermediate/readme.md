# APUG December 2021 Intermediate Challenge

Click [here](https://github.com/PythonAberdeen/user_group/blob/master/2021-12/intermediate/challenge.ipynb) to vie this challenege as a Jupyter Notebook.

To get you started, here is a template for a decorator which does not take arguments:

    from functools import wraps

    def my_decorator_name_goes_here(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            ...
            result = f(*args, **kwargs)
            ...
            return result

        return wrapper

And here is a template for a decorator which takes arguments:

    from functools import wraps

    def my_decorator_name_goes_here(...):

        def decorator(f):

            @wraps(f)
            def wrapper(*args, **kwargs):

                ...
                result = f(*args, **kwargs)
                ...
                return result

            return wrapper

        return decorator
        
---

## 1. Challenge 1

Write a decorator `@cooler` which makes the return value of a function bigger by a given percentage.

For example, `@cooler(10)` will cause the returned value to be 10% higher.

### 1.1. Example Usage 1:

    @cooler(10)
    def answer():
        return 42
    
    >>> answer()
    46.2

---

## 2. Challenge 2 - Argument Replacer

Write a decorator `@replace_arg` which itself takes 2 arguments called `position` and `new_value`.

- `position` - the index (starting at 0) to replace
- `new_value` - the new value use

The decorator will wrap any function (any number of inputs) and when the function is called will replace the specified argument.

### 2.1. Example Usage 1:

The value given by the user for the first argument will be ignored and replaced by `21`.
    
    @replace_arg(position=0, new_value=21)
    def multiply(a, b):
        return a * b
        
    >>> multiply(10, 2)
    42

### 2.2. Example Usage 2:

The value given by the user for the third argument will be ignored and replaced by `'dogecoin'`.

    @replace_arg(position=2, new_value='dogecoin')
    def order(order_type, size, currency, price):
        print(f'Placing {order_type} for {size} {currency} at ${price}')
        
    >>> order('buy', 10, 'bitcoin', 40000)
    Placing buy for 10 dogecoin at $40000

---

## 3. Challenge 3

Write a decorator `@multi` which gives a function of `2` arguments the ability to take a tuple of posibilities in each position and reeturns all combinations as a map.

Further, write a decorator `@argmin` which can be added before `@multi` to return a set of only the tuples representing the minmimum value.

### 3.1. Example Usage (`@multi`)

    @multi
    def add(x, y):
        return x + y

    >>> add((1, 3, 5, 7), (10, 100))
    {(1, 10) : 11,
     (1, 100) : 101,
     (3, 10) : 13,
     (3, 100) : 103,
     (5, 10) : 15,
     (5, 100) : 105,
     (7, 10) : 17,
     (7, 100) : 107}

### 3.2. Example Usage (`@multi` and `@argmin`)

The minimum value for the `mul` function with these arguments is `-20`, and there are two possible ways to make it given the possible listed argument values: `mul(-5, 4)` and `mul(5, -4)`.

    @argmin
    @multi
    def mul(x, y):
        return x * y
    
    >>> mul((-5, 0, 5), (4, -4))
    {(-5, 4), (5, -4)}
    
---

## 4. Bonus Challenges

## 4.1. Bonus 1

Write a version of `cooler` which takes an optional extra argument `plus` which adds to the result. e.g. this will add 10% of the origonal value, then add a further number 15.

    @cooler(10, plus=15)

## 4.2. Bonus 2

Write a version of `replace_args` which takes a dictionary of named arguments to replace. e.g.

    @replace_arg({'order_type' : 'sell', 'price' : 10})

## 4.3. Bonus 3

Write a version of `multi` which works on a function of any number of inputs instead of just 2.

Use it to show that the arg min of

    def my_funct(x, y, z):
        return (x-15) ** 2 + (y-20) ** 2 + (z+4) ** 2

for some range of possible input integers (say from -100 to +100) is

    (15, 20, -4)
