Solutions to Cats in Hats challenge

We have four suggested solutions (of varying complexity and readability)

## Solution One

    # Create a dictionary of cats {cat1:"False", cat2:"False" }  
    cats_in_hats = {}
    for x in range(1,101):
        cat_name = "cat"+str(x)
        cats_in_hats[cat_name] = False
    # Loop through them 1 at a time, 2 at a time, flipping hats
    for step in range (1,101):
        cat_counter = 0
        while cat_counter + step <=100 :
            cat_counter += step
            #print (f"Step: {step} and cat_counter: {cat_counter}")
            cat_id = "cat"+str(cat_counter)
            cats_in_hats[cat_id] = not cats_in_hats[cat_id]
            #print("Flipped "+ cat_id)
    #Print out which is wearing a hat        
    for x in range(1,101):
        cat_name = "cat"+str(x)
        if cats_in_hats[cat_name]:
            print (f"Cat {x} is wearing a hat")

## Solution Two

    cats_in_hats = [False]*100
    for step in range(1, 101):
        for cat in range(step-1, 100, step):
            cats_in_hats[cat] = not cats_in_hats[cat]
    for cat in range(100):
        if cats_in_hats[cat]:
            print(f"Cat {cat+1} is wearing a hat")

## Solution Three

    import functools
    cats = 100
    _=[print(f"Cat {cat + 1} is wearing a hat") for cat in range(cats) if [functools.reduce(lambda x, y: x * y, [(-1) ** int((cat+1) % step == 0) for step in range(1, cats + 1)], 1) for cat in range(cats)][cat] == -1]

## Solution Four
    [print(f"Cat {c+1} is wearing a hat") for c, d in enumerate(
        [len([i for i in range(1, x+1) if x % i == 0]) for x in range(1, 101)]) if d%2==1]

## Solution Four

    import functools
    cats = 100
    _=[print(f"Cat {cat + 1} is wearing a hat") for cat in range(cats) if [functools.reduce(lambda x, y: x * y, [(-1) ** int((cat+1) % step == 0) for step in range(1, cats + 1)], 1) for cat in range(cats)][cat] == -1]

## See Also

There are also some suggested solutions [here](https://github.com/realpython/python-basics-exercises/tree/master/ch09-lists-tuples-and-dictionaries) as solutions to the Python Basics book chellenge exercises. We highly recommend that book! 
