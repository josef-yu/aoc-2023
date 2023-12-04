from utils.parse import parse_day

def get_winning_numbers(numbers_string: str):
    numbers_set = numbers_string.split('|')
    winning_numbers = []
    
    left_numbers = numbers_set[0].strip().split(' ')
    right_numbers = numbers_set[1].strip().split(' ')
    for number in left_numbers:
        if number in right_numbers and number != '':
            winning_numbers.append(number)

    return winning_numbers

def get_card_winning_numbers(line: str):
    parsed_line = line.split(': ')
    numbers = parsed_line[1]

    winning_numbers = get_winning_numbers(numbers)

    return winning_numbers

def solve_part_1(input_data: list[str]):
    total_points = 0
    for card_line in input_data:
        points = 0
        winning_numbers = get_card_winning_numbers(card_line)
        if len(winning_numbers) > 0:
            points = 2**(len(winning_numbers)-1)
        
        total_points += points

    return total_points

def solve_part_2(input_data: list[str]):
    total_cards = 0
    cards = {}
    for index, card_line in enumerate(input_data):
        winning_numbers = get_card_winning_numbers(card_line)
        loops = 1
        if index in cards:
            loops += cards[index]
        
        for _ in range(loops):
            for n in range(len(winning_numbers)):
                if index + 1 + n in cards:
                    cards[index + 1 + n] += 1
                else:
                    cards[index + 1 + n] = 1

            total_cards += 1
    return total_cards

if __name__ == '__main__':
    input_data = parse_day(day=4, is_example=False)

    print(solve_part_1(input_data['input']))

    input_data = parse_day(day=4, is_example=False)

    print(solve_part_2(input_data['input']))