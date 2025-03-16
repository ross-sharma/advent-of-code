_input_sm = """
125 17
6
""".strip()

_input_lg = """
1750884 193 866395 7 1158 31 35216 0
25
""".strip()

from pprint import pp  # noqa


def parse(raw) -> tuple[list[int], int]:
    nums, blinks = raw.split("\n")
    return [int(x) for x in nums.split()], int(blinks)


def blink(stones: list[int]):
    i = 0
    while i < len(stones):
        stone = stones[i]

        if stone == 0:
            stones[i] = 1
            i += 1
            continue

        stone_str = str(stone)
        strlen = len(stone_str)

        if strlen % 2 == 0:
            left = stone_str[: strlen // 2]
            right = stone_str[strlen // 2 :]
            stones[i] = int(left)
            stones.insert(i + 1, int(right))
            i += 2
        else:
            stones[i] *= 2024
            i += 1


def main(puzzle_input):
    stones, blinks = parse(puzzle_input)
    for _ in range(blinks):
        blink(stones)
    print(len(stones))


if __name__ == "__main__":
    #main(_input_sm)
    main(_input_lg)
