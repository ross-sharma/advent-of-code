input_sm = "2333133121414131402"

with open("day9_in.txt") as f:
	input_lg = f.read().strip()


def expand(s):
	out = []
	for i,n in enumerate(s):	
		n = int(n)
		if i % 2 == 0:
			fid = i // 2
			out += [fid] * n
		else:
			out += ["."] * n
	return out


def pack(exp):
	out = exp.copy()
	tail_p = len(exp) - 1
	head_p = exp.index(".")

	while tail_p > head_p:
		data = out[tail_p]

		if data == ".":
			tail_p -= 1
			continue

		out[head_p] = data
		out[tail_p] = "."
		head_p = out.index(".", head_p)
		tail_p -= 1
	return out


def checksum(packed):
	total = 0
	for i,n in enumerate(packed):
		if n == ".":
			break
		total += n*i
	return total
		


def main(puzzle_input):
	exp = expand(puzzle_input)
	packed = pack(exp)
	#print("".join(str(s) for s in packed))
	print(checksum(packed))


if __name__ == "__main__":
	#main(input_sm)
	main(input_lg)

