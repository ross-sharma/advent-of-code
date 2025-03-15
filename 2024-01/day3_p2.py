_input_small = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("day3_in.txt") as f:
	_input_large = f.read()

regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

import re

matches = re.findall(regex, _input_large)
total = 0
enabled = True

for expr in matches:
	print(expr)
	if expr == "do()":
		enabled = True
	elif expr == "don't()":
		enabled = False
	elif enabled:
		left, right = expr.split(",")
		a = int(left[4:])
		b = int(right[:-1])
		print(a,b)
		total += a * b
print(total)
