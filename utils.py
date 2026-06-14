def print_board(board):
    '''
    Output the board as text
    '''
    print(board[0:3].replace("0", " "), end="|")
    print(board[3:6].replace("0", " "), end="|")
    print(board[6:9].replace("0", " "))
    
    print(board[9:12].replace("0", " "), end="|")
    print(board[12:15].replace("0", " "), end="|")
    print(board[15:18].replace("0", " "))
    
    print(board[18:21].replace("0", " "), end="|")
    print(board[21:24].replace("0", " "), end="|")
    print(board[24:27].replace("0", " "))

    print("=== === ===")

    print(board[27:30].replace("0", " "), end="|")
    print(board[30:33].replace("0", " "), end="|")
    print(board[33:36].replace("0", " "))

    print(board[36:39].replace("0", " "), end="|")
    print(board[39:42].replace("0", " "), end="|")
    print(board[42:45].replace("0", " "))

    print(board[45:48].replace("0", " "), end="|")
    print(board[48:51].replace("0", " "), end="|")
    print(board[51:54].replace("0", " "))

    print("=== === ===")

    print(board[54:57].replace("0", " "), end="|")
    print(board[57:60].replace("0", " "), end="|")
    print(board[60:63].replace("0", " "))

    print(board[63:66].replace("0", " "), end="|")
    print(board[66:69].replace("0", " "), end="|")
    print(board[69:72].replace("0", " "))

    print(board[72:75].replace("0", " "), end="|")
    print(board[75:78].replace("0", " "), end="|")
    print(board[78:81].replace("0", " "))

    return None

def read_image(image):
    '''
    Take a square PNG and return a board object
    '''
    return None

if __name__ == "__main__":
    sample_board = "900508007080302905054000080070680032100004008500219060000906001726001040001470056"
    print_board(sample_board)