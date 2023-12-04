from utils.parse import parse_day
from typing import TypedDict
import re

Bag = TypedDict('Game', {'red': int, 'green': int, 'blue': int})
GAME_REGEX = 'Game \d'

def get_cubes(cube_set: str):
    cubes = cube_set.split(', ')    
    bag: Bag = {'red': 0, 'green': 0, 'blue': 0}

    for cube in cubes:
        parsed_cube = cube.split(' ')
        bag[parsed_cube[1]] += int(parsed_cube[0])

    return bag

def get_bag(line: str):
    parsed_line = line.split(': ')
    game_id = parsed_line[0].split(' ')[1]

    sets = parsed_line[1].split('; ')

    bags = [get_cubes(x) for x in sets]

    return int(game_id), bags

def check_bag_validity(bags: list[Bag]):
    MAX_IN_BAG: Bag = {'red': 12, 'green': 13, 'blue': 14}

    for bag in bags:
        for color, count in bag.items():
            if MAX_IN_BAG[color] < count:
                print(f'Invalid {color} count: {count}')
                return False
    
    return True

def get_max_cubes(bags: list[Bag]):
    max_in_bag: Bag = {'red': 0, 'green': 0, 'blue': 0}

    for bag in bags:
        for color, count in bag.items():
            if max_in_bag[color] < count:
                max_in_bag[color] = count

    return max_in_bag

def solve_part_1(input_data: list[str]):
    total_ids = 0

    for game_line in input_data:
        game_id, bags = get_bag(game_line)
        print(f'Checking game id: {game_id}')
        print(bags)

        is_valid = check_bag_validity(bags)

        if is_valid:
            temp_sum = total_ids + game_id
            print(f'{total_ids} + {game_id} = {temp_sum}')
            total_ids += game_id
        print()
    return total_ids

def solve_part_2(input_data: list[str]):
    total_power = 0

    for game_line in input_data:
        game_id, bags = get_bag(game_line)
        print(f'Checking game id: {game_id}')
        print(bags)

        max_cubes = get_max_cubes(bags)
        print(max_cubes)
        power = 1

        for count in max_cubes.values():
            power *= count
        print(power)
        total_power += power
        
        print()

    return total_power


if __name__ == '__main__':
    input_data = parse_day(day=2, is_example=False)

    print(solve_part_1(input_data['input']))

    input_data = parse_day(day=2, is_example=False)

    print(solve_part_2(input_data['input']))