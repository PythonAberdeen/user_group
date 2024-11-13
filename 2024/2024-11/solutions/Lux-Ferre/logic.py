import json


class Logic:
	def __init__(self):
		self.configs = {
			"title": "Advent-ish"
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
		elif payload == "11":
			self.ages_part_one(ws)
		elif payload == "12":
			self.ages_part_two(ws)
		elif payload == "21":
			self.chips_part_one(ws)
		elif payload == "22":
			self.chips_part_two(ws)
		elif payload == "31":
			self.presents_part_one(ws)
		else:
			self.send_ws(ws, {"command": "display", "data": payload})

	def ages_part_one(self, ws):
		age_map = {}

		with open("input1.txt", "r") as ages_file:
			for line in ages_file:
				line = line.strip()
				age_map[line] = self.get_age(line)

		max_val = 0
		name = ""

		for key, value in age_map.items():
			if value > max_val:
				name = key
				max_val = value

		answer = f"{name}: {max_val}"

		self.send_ws(ws, {"command": "display", "data": answer})

	@staticmethod
	def get_age(self, name: str) -> int:
		name = name.lower()
		age = 0

		for char in name:
			if char == " ":
				continue
			age += ord(char) - 96

		return age

	def ages_part_two(self, ws):
		star_map = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

		with open("input1.txt", "r") as ages_file:
			for line in ages_file:
				line = line.strip()
				star_map[self.get_star_code(line)].append(line)

		name = ""

		for key, value in star_map.items():
			if len(value) == 1:
				name = value[0]
				break

		answer = f"{name}: {self.get_age(name)}"

		self.send_ws(ws, {"command": "clear", "data": None})
		self.send_ws(ws, {"command": "display", "data": answer})

	@staticmethod
	def get_star_code(self, name: str) -> int:
		code = 1
		pos = 1

		for char in name:
			if char == " ":
				continue

			if ord(char) > 96:  # Is lowercase
				code *= (ord(char) - 96) * (pos ** 2)
			else:
				code *= (ord(char) - 64) * (pos ** 3)

			pos += 1

		sign = str(code)[0]

		print(sign)

		return int(sign)

	def chips_part_one(self, ws):
		cheapest_value = 99999
		cheapest_portion = 0

		with open("input2.txt", "r") as ages_file:
			for line in ages_file:
				line = line.strip()
				price, size = line.split(" ", 1)
				price_per = float(price)/int(size)
				if price_per < cheapest_value:
					cheapest_value = price_per
					cheapest_portion = size

		self.send_ws(ws, {"command": "display", "data": cheapest_portion})

	def chips_part_two(self, ws):
		shops = []
		total = 0

		with open("input2.txt", "r") as ages_file:
			for i, line in enumerate(ages_file):
				line = line.strip()
				price, seagulls = line.split(" ", 1)
				shops.append(
					{
						"price": float(price),
						"seagulls": int(seagulls),
						"skip": False
					}
				)

		for shop in shops:
			cur_price = shop["price"]
			cur_seagulls = shop["seagulls"]

			for other in shops:
				if other["price"] < cur_price and other["seagulls"] <= cur_seagulls:
					shop["skip"] = True
					break
				elif other["price"] == cur_price and other["seagulls"] < cur_seagulls:
					shop["skip"] = True
					break

		for shop in shops:
			if not shop["skip"]:
				total += shop["price"]

		self.send_ws(ws, {"command": "display", "data": f"£{total}"})

	def presents_part_one(self, ws):
		presents = []

		with open("input3.txt", "r") as ages_file:
			for i, line in enumerate(ages_file):
				line = line.strip()
				presents.append({
					"value": float(line),
					"available": True,
					"position": i
				})

		opened = []

		while len(opened) < 8:
			pos = self.get_max_available(presents)
			opened.append(presents[pos])
			presents[pos]["available"] = False
			if pos > 0:
				presents[pos - 1]["available"] = False
			if pos < len(presents) - 1:
				presents[pos + 1]["available"] = False

		total = 0

		for present in opened:
			total += present["value"]

		self.send_ws(ws, {"command": "display", "data": f"£{total}"})

	def get_max_available(self, presents: list[dict]) -> int:
		sorted_presents = sorted(presents, key=lambda d: d['value'], reverse=True)
		for present in sorted_presents:
			if present["available"]:
				return present["position"]
