import pickle

def find_divisor_sum(n: int) -> int:
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i

    return divisor_sum


def check_abundance(n: int) -> bool:
    return find_divisor_sum(n) > n


def create_abundant_list():
    abundant_list = []
    for i in range(1, 28123):
        if check_abundance(i):
            abundant_list.append(i)

    with open('abundants.p', 'wb') as file:
        pickle.dump(abundant_list, file)


def fetch_abuntant_list() -> list:
    with open('abundants.p', 'rb') as file:
        abundant_list = pickle.load(file)

    return abundant_list


def generate_all_abundant_sums():
    abundant_list = fetch_abuntant_list()
    all_sums = []
    for i in abundant_list:
        for j in abundant_list:
            all_sums.append(i+j)

    with open('abundant_sums.p', 'wb') as file:
        pickle.dump(all_sums, file)


def fetch_abuntant_sums() -> list:
    with open('abundant_sums.p', 'rb') as file:
        abundant_sums = pickle.load(file)

    return abundant_sums


def get_non_abundant_sums():
    all_numbers = set(range(1, 28123))
    abundant_sums = set(fetch_abuntant_sums())

    non_abundant_sums = all_numbers - abundant_sums

    with open('non_abundant_sums.p', 'wb') as file:
        pickle.dump(non_abundant_sums, file)


def fetch_non_abuntant_sums() -> list:
    with open('non_abundant_sums.p', 'rb') as file:
        non_abundant_sums = pickle.load(file)

    return non_abundant_sums

'''
# Uncomment this section to create files for first run

create_abundant_list()
generate_all_abundant_sums()
get_non_abundant_sums()
'''

print(sum(fetch_non_abuntant_sums()))