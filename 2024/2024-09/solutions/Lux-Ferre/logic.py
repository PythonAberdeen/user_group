import json
import random


class Logic:
	def __init__(self):
		self.configs = {
			"title": "Bingo"
		}
		self.dispatch_map = {
			"execute": self.execute
		}

	def dispatch(self, ws, message: dict):
		target_method = self.dispatch_map.get(message["command"], None)
		if target_method is None:
			print(f"Invalid method {message['command']}")
			return

		target_method(ws, message["user_input"])

	def send_ws(self, ws, message: dict):
		response = {
			"command": message["command"],
			"data": message["data"]
		}
		ws.send(json.dumps(response))

	def execute(self, ws, payload):
		if payload == "clear":
			self.send_ws(ws, {"command": "clear", "data": None})
		elif payload == "gen":
			card = self.generate_card()
			self.print_card(ws, card)
		else:
			self.send_ws(ws, {"command": "display", "data": payload})

	def generate_card(self):
		breakpoints = [16, 31, 46, 61, 76]

		start_point = 1
		cols = []
		for b_point in breakpoints:
			col = random.sample(range(start_point, b_point), 5)
			cols.append(col)
			start_point = b_point - 1

		return cols

	def print_card(self, ws, card: list[list[int]]):
		outputs = ["|"] * 5
		for j, col in enumerate(card):
			for i in range(5):
				if i == 2 and j == 2:
					val = ("X")
				else:
					val = col[i]
				outputs[i] += f"{val}|"

		self.send_ws(ws, {"command": "clear", "data": None})
		for row in outputs:
			self.send_ws(ws, {"command": "display", "data": row})
