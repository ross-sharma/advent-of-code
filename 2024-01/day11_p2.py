_input_sm = """
125 17
25
""".strip()

_input_lg = """
1750884 193 866395 7 1158 31 35216 0
75
""".strip()

from pprint import pp  # noqa


def parse(raw) -> tuple[list[int], int]:
    nums, blinks = raw.split("\n")
    return [int(x) for x in nums.split()], int(blinks)


def calc_new_stones(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    new_stones = []
    stone_str = str(stone)
    strlen = len(stone_str)

    if strlen % 2 == 0:
        left = stone_str[: strlen // 2]
        right = stone_str[strlen // 2 :]
        new_stones.append(int(left))
        new_stones.append(int(right))
    else:
        new_stones.append(stone * 2024)
    return new_stones


def blink(stone: int, blinks: int, memo=None) -> int:
    if memo is None:
        memo = {}

    if blinks == 0:
        return 1

    memo_key = (stone, blinks)
    if memo_key in memo:
        return memo[memo_key]

    stones = calc_new_stones(stone)
    blinks -= 1
    total = 0

    for stone in stones:
        memo_key = (stone, blinks)
        num = blink(stone, blinks, memo)
        memo[memo_key] = num
        total += num

    return total


def main(puzzle_input):
    stones, blinks = parse(puzzle_input)
    total = 0
    for stone in stones:
        n_stones = blink(stone, blinks)
        total += n_stones
    print(total)


if __name__ == "__main__":
    #main(_input_sm)
    main(_input_lg)
