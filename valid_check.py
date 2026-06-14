import regex as re


# 1: convert the 81-char number to 3 lists of 9 lists of 9 values, changing zeroes to np.nan
    # NONANTS
    # ROWS
    # COLS
# 2: for each list, check if there is a repeat number in any inner list

def valid_check(board):
    #Board is 81 characters
    board = str(board)
    nonant_starts = [0, 3, 6, 27, 30, 33, 54, 57, 60]

    rows = [board[i:i+9] for i in range(0, 81, 9)]
    columns = [board[i::9] for i in range(9)]
    nonants = [board[i:i+3] + board[i+9:i+12] + board[i+18:i+21] for i in nonant_starts]

    for pos, value in enumerate(rows):
        if bool(re.search(r'([^0]).*\1', value)):
            print(f'Issue at row {pos + 1}')
            return False
            
    for pos, value in enumerate(columns):
        if bool(re.search(r'([^0]).*\1', value)):
            print(f'Issue at col {pos + 1}')
            return False

    for pos, value in enumerate(nonants):
        if bool(re.search(r'([^0]).*\1', value)):
            print(f'Issue at nonant {pos + 1}')
            return False
    
    return True


if __name__ == '__main__':
    sample_1 = '900508007080302905054000080070680032100004008500219060000906001726001040001470056'
    
    print(valid_check(sample_1))
