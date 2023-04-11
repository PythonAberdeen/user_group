import os
from datetime import date

data_set = {}


def load_data():
    data_set["Stephen King"] = date.fromisoformat("1947-09-21")
    data_set["Roger Federer"] = date.fromisoformat("1981-05-08")
    data_set["Lewis Hamilton"] = date.fromisoformat("1985-05-07")
    data_set["Lewis Capaldi"] = date.fromisoformat("1996-10-07")
    data_set["Dame Judy Dench"] = date.fromisoformat("1934-12-09")
    data_set["Baroness Susan Greenfield"] = date.fromisoformat("1950-10-01")


def print_frame():
    print("Welcome to the birthday look-up service. We know the birthdates of: ")
    for name in data_set:
        print(f"- {name}")


def get_input():
    print("Which person's birthday would you like to know? ")
    user_input = input("Type the name or type 'stop' to quit: ")
    return user_input


def main():
    load_data()
    print_frame()
    while True:
        user_input = get_input()
        if user_input.lower() == "stop":
            break
        elif user_input in data_set:
            bd = data_set[user_input].strftime("%d of %B, %Y")
            print(f"{user_input} was born on {bd}")
        else:
            print("That input was not valid. Try again or type 'stop' to quit.")


if __name__ == '__main__':
    main()
