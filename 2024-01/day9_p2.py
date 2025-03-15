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


def get_free_size(fs, index):
	size = 0	
	while fs[index] == ".":
		size += 1
		index += 1
		if index == len(fs):
			break
	return size


def get_file_size(fs, fid, index):
	size = 0	
	while fs[index] == fid:
		size += 1
		index -= 1
		if index == 0:
			break
	return size


def get_free_block(fs, size):
	idx = fs.index(".")
	limit = len(fs) - size
	
	while idx < limit:
		free_size = get_free_size(fs, idx)	
		if free_size >= size:
			return idx

		try:
			idx = fs.index(".", idx+free_size)
		except ValueError:
			return None
		
	return None
	

def move_file(fs, tail_p, write_idx, size):
	data = fs[tail_p]
	for i in range(size):
		if fs[write_idx + i] != ".":
			raise Exception("overwrite")
		fs[write_idx + i] = data
		fs[tail_p - i] = "."


def pack(exp):
	step = False
	out = exp.copy()
	tail_p = len(exp) - 1

	while tail_p >= 1:
		if step:
			debug_fs(out)
			print( (" " * tail_p) + "^tp" )
			input("enter to continue")

		data = out[tail_p]

		if data == ".":
			tail_p -= 1
			continue

		f_size = get_file_size(out, data, tail_p)
		f_head = tail_p - f_size + 1
		write_idx = get_free_block(out, f_size)
		
		if step:
			print(f"{write_idx=} {f_head=}")

		if write_idx is not None:
			if write_idx < f_head:
				move_file(out, tail_p, write_idx, f_size)

		tail_p -= f_size
			
	return out


def checksum(packed):
	total = 0
	for i,n in enumerate(packed):
		if n != ".":
			total += n*i
	return total


def debug_fs(fs):
	print("".join(str(s) for s in fs))


def main(puzzle_input):
	exp = expand(puzzle_input)
	packed = pack(exp)
	#debug_fs(packed)
	print(checksum(packed))


if __name__ == "__main__":
	main(input_sm)
	#main(input_lg)
	#main("111")
	#main("122")

