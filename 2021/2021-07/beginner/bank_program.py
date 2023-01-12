users = {
    'Alice' : 400,
    'Bob' : 1500,
    'Carol' : 21000
}


def read_integer(prompt):
    while True:
        try:
            text = input(prompt)
            integer = int(text)
            if integer <= 0:
                print('Error: Positive Integer Required')
            else:
                return integer
        except ValueError:
            print('Error: Positive Integer Required')


def read_option(prompt, num_options):
    while True:
        value = read_integer(prompt)
        if value <= num_options:
            return value
        print(f'Error: options are 1 to {num_options}')


def check_balance():
    name = input('Input Name:')
    if name in users:
        balance = users[name]
        print(f'Balance of {name} is {balance}')
    else:
        print(f'Error: User "{name}" was not found')


def main():
    try:
        exit = False
        print('Welcome to the bank system')
        while not exit:
            print()
            print('1 - Check Balance')
            print('2 - Exit')
            option = read_option("Select Option:", 2)
            if option == 1:
                check_balance()
            if option == 2:
                exit = True
    except KeyboardInterrupt:
        pass
    print()
    print('Goodbye!')


main()
