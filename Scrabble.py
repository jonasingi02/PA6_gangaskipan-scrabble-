# veit ekki alveg hvar ég á að byrja í þessu verkefni enn þetta gæti alveg verið ágætis borð
# svo væri hægt að hafa bara if slikirði í innstu for lykkjunni til þess að um það hvort einhver bókstafur ætti að koma þar.git
class Board:
    def __init__(self) -> None:
        pass
    def __str__(self) -> None:
        ret_str= ""
        for i in range(15):
           ret_str = ret_str + " _"
        ret_str = ret_str + "\n"
        for i in range(15):
            for j in range(15):
                ret_str = ret_str + "|_"
            ret_str = ret_str + "|\n"
        return ret_str





a = Board()
print(a)









# Basic game
#     ● 5% Two players enter their names before the game starts
class Player:
    def __init__(self) -> None:
        pass

#     ● 5% Define a full bag of letters and map the letters to the correct values
class Bag:
    def __init__(self) -> None:
        pass

#     ● 5% Display which letters players have access to
#     ● 5% Display which players turn it is
#     ● 10% Display a 15x15 grid
def print_display():
    pass

#     ● 10% Players can choose three options on their turn.
#         ○ Play a word with letters they have drawn
#             ■ Players can add words vertically and horizontally on the grid
#         ○ Swap any number of letters with the same number of letters from the bag
#         ○ Pass their turn
def make_play():
    pass

#     ● 10% Display the words played on the grid
def update_display():
    pass

#     ● 10% Calculate score for a word played
def calulate_score():
    pass

# Advanced game
#     ● 5% When a player plays a word using all 7 of their letters that player gets an extra 50 points added to their total score
def check_for_extra_points():
    pass

#     ● 5% Add modifiers to certain tiles on the grid
#         ○ For example:
#             ■ Double letter
#             ■ Triple word
#             ■ See wikipedia link for the modifier setup on the grid
class modifier:
    def __init__(self) -> None:
        pass

#     ● 5% Letter modifiers get calculated into players score when word is created on these tiles
#     ● 5% Word modifiers get calculated into players score when word is created on these tiles
def update_score():
    pass

#     ● 10% Detect when the game should end ○ The game ends when all letters have been drawn from the bag and one player has finished all their letters ○ Or when all players pass twice in a row
def end_game():
    pass

#     ● 10% Allow more than 2 players to play (official scrabble rules state it can be played with 2-4 people)
#     ● 10% Checking words (see assignment page for a dictionary file)
#         ○ Check the word played with a dictionary
#             ■ If the word played is invalid the current player forfeits their turn
#         ○ Check all words connected to the played word with a dictionary
#             ■ If any words connected to the played word are invalid the current player forfeits their turn