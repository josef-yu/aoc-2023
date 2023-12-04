from utils.parse import parse_day

def is_valid_symbol(char: str, symbol: str = None):
    is_valid = False

    if symbol is None:
        is_valid = not char.isalnum() and char != '.'
    else:
        is_valid = char == symbol
    return is_valid

def get_valid_symbol_coordinates(input_data: list[str], row: int, column: int, symbol: str = None):
    if column > 0 and is_valid_symbol(input_data[row][column - 1], symbol=symbol):
        return row, column - 1
    elif row > 0 and column > 0 and is_valid_symbol(input_data[row - 1][column - 1], symbol=symbol):
        return row - 1, column - 1
    elif row > 0 and is_valid_symbol(input_data[row - 1][column], symbol=symbol):
        return row - 1, column
    elif row > 0 and column + 1 != len(input_data[0]) and is_valid_symbol(input_data[row - 1][column + 1], symbol=symbol):
        return row - 1, column + 1
    elif column + 1 != len(input_data[0]) and is_valid_symbol(input_data[row][column + 1], symbol=symbol):
        return row, column + 1
    elif column + 1 != len(input_data[0]) and row + 1 != len(input_data) and is_valid_symbol(input_data[row + 1][column + 1], symbol=symbol):
        return row + 1, column + 1
    elif row + 1 != len(input_data) and is_valid_symbol(input_data[row + 1][column], symbol=symbol):
        return row + 1, column
    elif row + 1 != len(input_data) and column > 0 and is_valid_symbol(input_data[row + 1][column - 1], symbol=symbol):
        return row + 1, column - 1
    else:
        return None, None

def solve_part_1(input_data: list[str]):
    valid_nums = []
    for row, line in enumerate(input_data):
        current_num = ''
        is_valid_num = False
        
        for column, char in enumerate(line):
            if char.isdigit():
                current_num += char
            elif char == '.' or not char.isalnum():
                if is_valid_num and current_num != '':
                    valid_nums.append(int(current_num))
                
                current_num = ''
                is_valid_num = False
                continue
            
            x, y = get_valid_symbol_coordinates(input_data, row, column)
            if x and y and not is_valid_num:
                is_valid_num = True
        
        if is_valid_num and current_num != '':
            valid_nums.append(int(current_num))

    return sum(valid_nums)

def solve_part_2(input_data: list[str]):
    valid_nums = {}

    for row, line in enumerate(input_data):
        current_num = ''
        is_valid_num = False
        symbol_row, symbol_column = None, None

        for column, char in enumerate(line):
            if char.isdigit():
                current_num += char
            elif char == '.' or not char.isalnum():
                if is_valid_num and current_num != '':
                    symbol_coordinates = f'{symbol_row},{symbol_column}'
                    if symbol_coordinates in valid_nums:
                        valid_nums[symbol_coordinates].append(int(current_num))
                    else:
                        valid_nums[symbol_coordinates] = [int(current_num)]
                
                current_num = ''
                is_valid_num = False
                symbol_row, symbol_column = None, None
                continue
            
            x, y = get_valid_symbol_coordinates(input_data, row, column, '*')
            if x and y and not is_valid_num:
                symbol_row = x
                symbol_column = y
                is_valid_num = True
        
        if is_valid_num and current_num != '':
            symbol_coordinates = f'{symbol_row},{symbol_column}'
            if symbol_coordinates in valid_nums:
                valid_nums[symbol_coordinates].append(int(current_num))
            else:
                valid_nums[symbol_coordinates] = [int(current_num)]

    return sum([x[0] * x[1] for x in valid_nums.values() if len(x) == 2])

if __name__ == '__main__':
    input_data = parse_day(day=3, is_example=False)
    
    print(solve_part_1(input_data['input']))

    input_data = parse_day(day=3, is_example=False)
    
    print(solve_part_2(input_data['input']))