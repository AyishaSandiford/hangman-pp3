import random

from word_list import hidden_word_list_level_one
from hang_stage import stages
from how_to_play import how_to_play_game


print("""
__        __   _                            _____      
\\ \\      / /__| | ___ ___  _ __ ___   ___  |_   _|__   
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\   | |/ _ \\  
  \\ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) | 
 _ \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|   |_|\\___/  
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __          
| |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\         
|  _  | (_| | | | | (_| | | | | | | (_| | | | |        
|_|_|_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|        
 / ___| __ _ _ __ _|___/___                            
| |  _ / _` | '_ ` _ \\ / _ \\                           
| |_| | (_| | | | | | |  __/                           
 \\____|\\__,_|_| |_| |_|\\___|                           
                                                
""")


# Initialise game state
gameState = {
  "random_word": "",
  "guessed_letters": [],
  "guessed_letter": "",
  "guessed_word": "",
  "bad_guesses_count": 0, 
}

def lines(numberOfLines = 1):
  print('\n' * numberOfLines)

# Line to separate each turn
def turnLine():
  print('-' * 50)

# Print the state of the guessed word. E.g. H _ L L O
def printGuessedWord(gameState):
  print(' '.join(gameState["guessed_word"]))
  lines()
  print('Guessed letters: ' + ', '.join(gameState["guessed_letters"]))

  # Check if the guess is valid. E.g. it is a single letter
def validateGuess(gameState):
  if len(gameState["guessed_letter"]) > 1:
    print('Please enter a single letter')
    return False

  if gameState["guessed_letter"] == ".":
    return False

  if gameState["guessed_letter"].isalpha() is False:
    print('Please enter a letter')
    return False

  if gameState["guessed_letter"] in gameState["guessed_letters"]:
    print('You have already guessed this letter')
    printGuessedWord(gameState)
    return False

  return True

  # Replace each blank with the guessed letter
def updateGuessedWord(gameState):
  indexes = [
    i for i,
    x in enumerate(gameState["random_word"])
    if x == gameState["guessed_letter"]
  ]
  for letterLocation in indexes:
    gameState["guessed_word"][letterLocation] = gameState["guessed_letter"]

# React to correct letter being guessed
def correctLetterGuessed(gameState):
  updateGuessedWord(gameState)
  print(f"You guessed the letter {gameState['guessed_letter']} correctly!")

# React to bad letter being guessed
def incorrectLetterGuessed(gameState):
  print(f"You guessed the letter {gameState['guessed_letter']} incorrectly!")
  lines()

# Print part of hang man correspoding to the number of bad guesses
  print(stages[gameState["bad_guesses_count"]])

  # Increment number of bad guesses
  gameState["bad_guesses_count"] += 1

# Remember that a letter was guessed so we can check and prevent it
# from being guessed again
def noteGuessedLetter(gameState):
  gameState["guessed_letters"] += gameState["guessed_letter"]

# Print the result of a finished game
def printGameResult(gameState):
  lines()

  