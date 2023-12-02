from utils.parse import parse_day
import re

def solve_part_1(input_data: list[str]):
    print('Solving part 1')
    total = 0
    for line in input_data:
        digits = list(filter(lambda x: x.isdigit(), line))
        if len(digits) > 0:
            total += int(digits[0])*10 + int(digits[-1])

    return total

def solve_part_2(input_data: list[str]):
    print('Solving part 2')
    numbers_regex = "(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))"
    total = 0

    DIGITS = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    for line in input_data:
        regex_result = re.findall(numbers_regex, line)
        digits = [x if x.isdigit() else DIGITS[x] for x in regex_result]
        if len(digits) > 0:
            number = int(digits[0])*10 + int(digits[-1])

        total += number

    return total

if __name__ == '__main__':
    input_data = parse_day(day=1, is_example=False)

    print(solve_part_1(input_data['input']))

    input_data = parse_day(day=1, is_example=False)

    print(solve_part_2(input_data['input']))