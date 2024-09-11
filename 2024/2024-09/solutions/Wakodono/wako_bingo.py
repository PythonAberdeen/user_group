import numpy as np

# Labelling the 5 columns B, I, N, G and O:

# Create empty numpy array
# FOR EACH Column
    # Choose numbers according to rules

def generate_bingo_column(
        min_value,
        max_vaue,
        is_middle = False,
):
        options = np.array(range(min_value, max_vaue + 1))

        if is_middle:
                column = np.random.choice(options, size=4)
                column = np.insert(column, 2, 0)
        else:
                column = np.random.choice(options, size=5)

        return column

def generate_bingo_card():
    bingo_card = np.empty(shape=(5,5), dtype=int)

    bingo_card[0] = generate_bingo_column(1, 15)
    bingo_card[1] = generate_bingo_column(16, 30)
    bingo_card[2] = generate_bingo_column(31, 45, is_middle=True)
    bingo_card[3] = generate_bingo_column(46, 60)
    bingo_card[4] = generate_bingo_column(61, 75)

    return bingo_card

def print_bingo_card(card):
       print("B  I  N  G  O")
       for k in range(5):
            for i in range(5):
                  print(f"{card[i][k]:2}", end=" ")
            print("")
    
if __name__ == "__main__":
       x = generate_bingo_card()
       print_bingo_card(x)
