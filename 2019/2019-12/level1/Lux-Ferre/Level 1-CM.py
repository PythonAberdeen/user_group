from math import sqrt

def recursive_solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 0:
        return recursive_solution(n - 1) + recursive_solution(n - 2)
    else:
        return recursive_solution(n + 2) - recursive_solution(n + 1)

def formulaic_solution(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))

def n_bonacci_solution(n, m):
    l = []
    for i in range(0, m):
        if i < n:
            l.append(1)
        else:
            x = 0
            for j in range(i-1, (i - 1) - n, -1):
                x = x + l[j]
            l.append(x)
    return l[m-1]

def non_rec_solution(n):
    l=[]

    for i in range(0, n):
        if i < 2:
            l.append(1)
        else:
            new_num=l[i - 1] + l[i - 2]
            l.append(new_num)
    return l[n-1]

def main():
    end_point = int(input("Which Fibonacci number do you want? "))

    # output_value=recursive_solution(end_point)
    # output_value=formulaic_solution(end_point)
    # output_value = n_bonacci_solution(3, 7)
    output_value = non_rec_solution(end_point)

    print(output_value)

if __name__ == '__main__':
    main()
