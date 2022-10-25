words= ['cat', 'dog']

def hangman(word):
    board = set_board(word)
    guesses = 6
    while board != word and guesses > 0:
        print(board)
        guess = input('Choose a letter ')
        # go through each letter of the word to see if any of the letters match
        for index in range(len(word)):
            if guess.lower() == word[index].lower():
                new_board = board[:index] + word[index] + board[index+1:]
        if new_board == board: guesses -= 1
        board = new_board
            
    




def set_board(word):
    board= ''
    for letter in word:
        if letter == ' ': board += ' '
        else: board += '#'
    return board


hangman('python')
