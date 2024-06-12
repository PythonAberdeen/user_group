import re
import os
import collections

class UI:
	def __init__(self):
		self.ui_active = True

	def clear_terminal(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def print_chose_difficulty(self):
		print("Which set of solutions do you wish to use?")
		print("0) Quit")
		print("1) Beginner")
		print("2) Intermediate")
		print("3) Advanced")

	def get_main_menu_choice(self):
		choice = input("Type menu number here: ")
		match choice:
			case "0":
				return "quit"
			case "1":
				return "beginner"
			case "2":
				return "intermediate"
			case "3":
				return "advanced"
			case _:
				self.clear_terminal()
				print("Invalid choice. Try again.")
				self.print_chose_difficulty()
				self.get_main_menu_choice()

	def print_beginner_menu(self):
		print("Which solution do you wish to use?")
		print("0) Back to Difficulty Choice")
		print("1) FizzBuzz")
		print("2) Palindrome Checker")
		print("3) Sum of Even Numbers")

	def get_beginner_choice(self):
		choice = input("Type menu number here: ")
		match choice:
			case "0":
				return "back"
			case "1":
				return "fizzbuzz"
			case "2":
				return "palindrome"
			case "3":
				return "evens"
			case _:
				self.clear_terminal()
				print("Invalid choice. Try again.")
				self.print_beginner_menu()
				self.get_beginner_choice()

	def print_intermediate_menu(self):
		print("Which solution do you wish to use?")
		print("0) Back to Difficulty Choice")
		print("1) Anagram Checker")
		print("2) Prime Factorization")

	def get_intermediate_choice(self):
		choice = input("Type menu number here: ")
		match choice:
			case "0":
				return "back"
			case "1":
				return "anagram"
			case "2":
				return "primes"
			case _:
				self.clear_terminal()
				print("Invalid choice. Try again.")
				self.print_intermediate_menu()
				self.get_intermediate_choice()

	def get_user_input(self):
		print("Type in your input.")
		print("Leave blank to use default values.")
		print("Whole numbers will be treated as integers.")
		print("Comma separated values within square brackets will be treated as a list. Trailing and leading whitespace will be removed.")
		raw_input = input("Type here: ")

		if raw_input == "":
			return None

		if raw_input[0] == "[" and raw_input[-1] == "]":
			raw_input = raw_input[1:-1]
			user_input = raw_input.split(",")
			if len(user_input) == 1 and user_input[0] == "":
				user_input.pop()
		else:
			user_input = raw_input

		if isinstance(user_input, list):
			user_input = [n.strip() for n in user_input]
			user_input = [int(n) if n.isnumeric() else n for n in user_input]
		else:
			if user_input.isnumeric():
				user_input = int(user_input)

		return user_input

	def print_solution(self, solution: dict):
		print(f"The solution to {solution['title']} with input:")
		print(f"\t {solution['input']}")
		print("is:")
		print(f"\t {solution['output']}")


class Beginner:
	def __init__(self):
		self.default_values = {
			"fizzbuzz": 100,
			"palindrome": ["Madam", "Goody", "I am Mai"],
			"evens": [11,12,33,19,82,101]
		}

	def fizz_buzz(self, n: int = None):
		if not n:
			n = self.default_values["fizzbuzz"]
		output = []
		for i in range(1, n+1):
			if i % 3 == 0:
				if i % 5 == 0:
					output.append("FizzBuzz")
				else:
					output.append("Fizz")
			elif i % 5 == 0:
				output.append("Buzz")
			else:
				output.append(i)

		return {
			"title": "FizzBuzz",
			"input": n,
			"output": output
		}

	def check_palindromes(self, user_input: str|list[str] = None) -> dict:
		if not user_input:
			user_input = self.default_values["palindrome"]
		elif isinstance(user_input, str):
			user_input = [user_input]

		output = []
		for word in user_input:
			lower_str = word.lower()
			cleaned_str = re.sub(r'[^a-z]', '', lower_str)
			reverse = cleaned_str[::-1]
			result = (word, cleaned_str == reverse)
			output.append(result)

		return {
			"title": "Palindrome Checker",
			"input": user_input,
			"output": output
		}

	def sum_evens(self, user_input:list[int] = None) -> dict:
		if not user_input:
			user_input = self.default_values["evens"]

		if not isinstance(user_input, list):
			return {
				"title": "Sum of Even Numbers",
				"input": user_input,
				"output": "Invalid input. Must be list of integers."
			}
		for value in user_input:
			if not isinstance(value, int):
				return {
					"title": "Sum of Even Numbers",
					"input": user_input,
					"output": "Invalid input. Must be list of integers."
				}

		evens = [n for n in user_input if n % 2 == 0]
		return {
			"title": "Sum of Even Numbers",
			"input": user_input,
			"output": sum(evens)
		}


class Intermediate:
	def __init__(self):
		self.default_values = {
			"anagram": ["elints", "enlist", "inlets", "listen", "silent", "tinsel"],
			"primes": 56
		}

	def anagram_checker(self, user_input: list[str] = None) -> dict:
		if not user_input:
			user_input = self.default_values["anagram"]

		if not len(user_input) >= 2:
			return {
				"title": "Anagram Checker",
				"input": user_input,
				"output": "Invalid input. Must be a list of at least 2 strings."
			}

		counter_representations = []
		for word in user_input:
			lower_str = word.lower()
			cleaned_str = re.sub(r'[^a-z]', '', lower_str)
			unsorted_counter = collections.Counter(cleaned_str)
			counter_representations.append(str(sorted(unsorted_counter.items(), key=lambda i: i[0])))

		anagrams_present = len(set(counter_representations))

		output = anagrams_present <= 1

		return {
			"title": "Anagram Checker",
			"input": user_input,
			"output": output
		}

	def get_prime_factors(self, user_input: int = None) -> dict:
		if not user_input:
			user_input = self.default_values["primes"]

		if not isinstance(user_input, int):
			return {
				"title": "Prime Factorization",
				"input": user_input,
				"output": "Invalid input. Must be a single integer."
			}
		def factorize(n, f):
			if n < f:
				return []
			if n % f == 0:
				return [f] + factorize(n / f, 2)
			return factorize(n, f + 1)

		return {
			"title": "Prime Factorization",
			"input": user_input,
			"output": factorize(user_input, 2)
		}


class Sudoku:
	def __init__(self):
		self.grid = [
			[5, 3, 0, 0, 7, 0, 0, 0, 0],
			[6, 0, 0, 1, 9, 5, 0, 0, 0],
			[0, 9, 8, 0, 0, 0, 0, 6, 0],
			[8, 0, 0, 0, 6, 0, 0, 0, 3],
			[4, 0, 0, 8, 0, 3, 0, 0, 1],
			[7, 0, 0, 0, 2, 0, 0, 0, 6],
			[0, 6, 0, 0, 0, 0, 2, 8, 0],
			[0, 0, 0, 4, 1, 9, 0, 0, 5],
			[0, 0, 0, 0, 8, 0, 0, 7, 9]
		]

		self.solving = []

	def generate_solving_grid(self):
		for row in self.grid:
			new_row = []
			for cell in row:
				if cell == 0:
					new_row.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
				else:
					new_row.append([cell])
			self.solving.append(new_row)

	def print_grid(self, grid):
		print("╔" + "═" * 11 + "╗")
		for i, row in enumerate(grid):
			if i == 3 or i == 6:
				print("╟" + "─" * 3 + "┼" + "─" * 3 + "┼" + "─" * 3 + "╢")
			row_str = "║"
			for j, cell in enumerate(row):
				row_str += f"{cell}"
				if j == 2 or j == 5:
					row_str += "│"
			row_str += "║"

			print(row_str)

		print("╚" + "═" * 11 + "╝")

	def get_confirmed_numbers(self, nums: list[list[int]]):
		confirmed_nums = []
		for cell in nums:
			if len(cell) == 1:
				confirmed_nums.append(cell[0])

		return confirmed_nums

	def check_cell(self, pos_x, pos_y, grid):
		cell_row = grid[pos_x]
		cell_col = []
		for row in grid:
			cell_col.append(row[pos_y])

		cell_box = []


if __name__ == "__main__":
	ui = UI()
	beginner = Beginner()
	intermediate = Intermediate()
	sudoku = Sudoku()
	sudoku.print_grid()
	input()
	while ui.ui_active:
		ui.clear_terminal()
		ui.print_chose_difficulty()
		difficulty = ui.get_main_menu_choice()
		ui.clear_terminal()
		match difficulty:
			case "quit":
				ui.ui_active = False
			case "beginner":
				ui.print_beginner_menu()
				beginner_choice = ui.get_beginner_choice()
				ui.clear_terminal()
				match beginner_choice:
					case "back":
						pass
					case "fizzbuzz":
						user_input = ui.get_user_input()
						ui.print_solution(beginner.fizz_buzz(user_input))
						input("Press Enter to continue...")
					case "palindrome":
						user_input = ui.get_user_input()
						ui.print_solution(beginner.check_palindromes(user_input))
						input("Press Enter to continue...")
					case "evens":
						user_input = ui.get_user_input()
						ui.print_solution(beginner.sum_evens(user_input))
						input("Press Enter to continue...")
			case "intermediate":
				ui.print_intermediate_menu()
				intermediate_choice = ui.get_intermediate_choice()
				ui.clear_terminal()
				match intermediate_choice:
					case "back":
						pass
					case "anagram":
						user_input = ui.get_user_input()
						ui.print_solution(intermediate.anagram_checker(user_input))
						input("Press Enter to continue...")
					case "primes":
						user_input = ui.get_user_input()
						ui.print_solution(intermediate.get_prime_factors(user_input))
						input("Press Enter to continue...")
