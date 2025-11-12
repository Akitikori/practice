
# Online Python - IDE, Editor, Compiler, Interpreter
import sys, random
print('ROCK, PAPER, SCISSORS')

#store the number of wins, losses, and ties
wins = 0
losses = 0
ties = 0
while True:
    print('Enter your move: (r)ock, (paper), (s)cissors or (q)uit')
    response = input('>')
    # translate the users choice into a rock, paper, scissors, or quit option
    if response =='q':
        sys.exit()
    elif response == 'p':
        full_response = 'PAPER'
    elif response == 's':
        full_response = 'SCISSORS'
    elif response == 'r':
        full_response = 'ROCK'
    else:
        print("Invalid move!")
        continue
    print(full_response + ' versus ...')
    # decide what the computer's response is
    computer_response = random.randint(0,2)
    if computer_response == 0:
        computer_response = 'PAPER'
    elif computer_response == 1:
        computer_response = 'SCISSORS'
    elif computer_response == 2:
        computer_response = 'ROCK'
    
    print(computer_response)
    
    # decide whether it's a win, tie or loss
    # PAPER
    if full_response == 'PAPER' and computer_response == 'PAPER':
        decision = 'tie'
    elif full_response == 'PAPER' and computer_response == 'ROCK':
        decision = 'win'
    elif full_response == 'PAPER' and computer_response == 'SCISSORS':
        decision = 'loss'
        
    # SCISSORS
    if full_response == 'SCISSORS' and computer_response == 'PAPER':
        decision = 'win'
    elif full_response == 'SCISSORS' and computer_response == 'ROCK':
        decision = 'loss'
    elif full_response == 'SCISSORS' and computer_response == 'SCISSORS':
        decision = 'tie'
        
    # ROCK
    if full_response == 'ROCK' and computer_response == 'PAPER':
        decision = 'loss'
    elif full_response == 'ROCK' and computer_response == 'ROCK':
        decision = 'tie'
    elif full_response == 'ROCK' and computer_response == 'SCISSORS':
        decision = 'win'
    
    # calculate score and print result
    if decision == 'loss':
        losses += 1
    elif decision == 'win':
        wins += 1
    elif decision == 'tie':
        ties += 1
    
    print('You ' + decision + ' ')
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + " Ties")