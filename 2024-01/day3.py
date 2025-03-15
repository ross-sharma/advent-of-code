_input_small = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("day3_in.txt") as f:
	_input_large = f.read()

regex = r"mul\(\d{1,3},\d{1,3}\)"

import re

matches = re.findall(regex, _input_large)
total = 0
for expr in matches:
	left, right = expr.split(",")
	a = int(left[4:])
	b = int(right[:-1])
	print(a,b)
	total += a * b
print(total)
