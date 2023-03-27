import random as rd

class BagEmptyError(Exception):
    pass

def main():
    test_game()
    # test_board()
    # test_bag()
    pass


# veit ekki alveg hvar ég á að byrja í þessu verkefni enn þetta gæti alveg verið ágætis borð
# svo væri hægt að hafa bara if slikirði í innstu for lykkjunni til þess að um það hvort einhver bókstafur ætti að koma þar.git


class Board:
    def __init__(self) -> None:
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        ''' Returns an initialized grid for the given dimension '''
        DIM = 15
        EMPTY = '|_'
        grid = []

        for i in range(DIM):
            sublist = []
            for j in range(DIM):

                # Bæta við "special tiles"
                # if any([
                #     i == 0 and j == self.alphabet.index('A'),
                #     i == 0 and j == self.alphabet.index('H'),
                #     i == 0 and j == self.alphabet.index('O'),
                # ]):
                #     sublist.append('|&')
                # else:

                sublist.append(EMPTY)
            grid.append(sublist)

        return grid


    def update(self, input_list, pos, alignment):
        char_list = []
        for tile in input_list:
            char_list.append(tile.letter)

        score = 0

        if alignment == 'vertical':
            x = self.alphabet.index(pos[0].upper())
            y = int(pos[1])-1
            for char in char_list:
                placement = (x,y)
                self._update_grid(placement=placement, letter=char)
                # score += ?
                y += 1
        elif alignment == 'horizontal':
            x = self.alphabet.index(pos[1].upper())
            y = int(pos[0])-1
            for char in char_list:
                placement = (x,y)
                self._update_grid(placement=placement, letter=char)
                x += 1

        return score


    def _update_grid(self, placement:tuple, letter:str):
        y_pos = placement[1]
        x_pos = placement[0]

        self.grid[y_pos][x_pos] = f'|{letter}'

    def __str__(self) -> None:
        ret_str= "    A B C D E F G H I J K L M N O\n   "

        # ret_str = ""

        for i in range(15):
           ret_str = ret_str + " _"
        ret_str = ret_str + "\n"
        for i in range(15):

            if i <= 8:
                ret_str += str(i+1) + '  '
            else:
                ret_str += str(i+1) + ' '


            for j in range(15):
                ret_str = ret_str + self.grid[i][j]
            ret_str = ret_str + "|\n"
        return ret_str








# Basic game
class Game:
    def __init__(self) -> None:
        self.players = []
        self.initialize_players()
        self.board = Board()
        self.board.score_list = [0] * len(self.players)
        self.bag = Bag()
        self.turn_counter = 0
        self.turn = self.players[0]

    def start_game(self):
        pass

    def initialize_players(self):
        more_players = True
        counter = 1
        print('Before you play Scrable, you must choose player names.')
        while more_players == True:
            player = Player(input(f'Please input the name for player {counter}: '))
            counter += 1
            self.players.append(player)

            if counter > 2 and counter < 5:
                more_player_input = input('Would you like to add another player? (y/n) ')

                if more_player_input.lower() == 'n':
                    more_players = False

            elif counter > 4:
                more_players = False
        print()

    def draw_from_bag(self):
        for player in self.players:
            for i in range(7):
                rand_num = rd.randint(0, self.bag.size-1)
                # letter = self.bag.alphabet[rand_num]
                player_letter = self.bag.draw(draw_number=rand_num)
                player.tiles.append(player_letter)

    def print_game(self):
        print(f'Next turn: {self.turn.name}\n')
        self.print_available_letters()
        print(self.board)

    def choose(self):
        choice = input('(1) Play word\n(2) Swap\n(3) Pass\nWhat you like to do?: ')

        if choice == '1':
            self.play_word()
        elif choice == '2':
            # self.swap()
            pass
        elif choice == '3':
            # self.pass_turn
            pass



    def print_available_letters(self):

        for player in self.players:
            ret_str = ''
            # print(f'{player.name}\'s tiles: {[tile.letter for tile in player.tiles]}')
            ret_str += f'{player}: '
            for tile in player.tiles:
                ret_str += f'{tile.letter}({tile.points}), '

            print(ret_str[:-2], end='\n\n')

    def next_turn(self):
        self.turn_counter += 1
        self.turn = self.players[self.turn_counter%2]

    def play_word(self):
        player = self.turn
        word = input('Which word would you like to play?: ')
        char_list = list(word.upper())
        input_list = []

        for char in char_list:
            found = False
            counter = 0

            while not found:
                tile = player.tiles[counter]

                if tile.letter == char:
                    input_tile = player.pop(index=counter)
                    found = True
                    input_list.append(input_tile)
                else:
                    counter += 1
        alignment = None
        pos = list(input('Where would you like to place the word?: '))

        if pos[0].isdigit() is False and pos[1].isdigit() is True:
            alignment = 'vertical'
        elif pos[0].isdigit() is True and pos[1].isdigit() is False:
            alignment = 'horizontal'

        self.board.update(input_list=input_list, pos=pos, alignment=alignment)




#     ● 5% Two players enter their names before the game starts
class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.tiles = []

    def pop(self, index):
        return self.tiles.pop(index)

    def update_score(self, score):
        pass

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.name

#     ● 5% Define a full bag of letters and map the letters to the correct values
class Bag:
    def __init__(self) -> None:
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*']
        self.tiles = [ [] for _ in range(len(self.alphabet)) ]
        self.size = 0
        self.fill_bag()

    def fill_bag(self):
        number_of_tiles_list = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]
        points_list = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
        for i in range(len(self.alphabet)):
            for _ in range(number_of_tiles_list[i]):
                self._insert(self.alphabet[i], points_list[i])

    def _insert(self, letter, points):
            insert_letter = Tile(letter=letter, points=points)
            index = self.alphabet.index(letter)
            self.tiles[index].append(insert_letter)
            self.size += 1

    def draw(self, draw_number):
        if self.size == 0:
            raise BagEmptyError


        #NOTA ENUMERATE?? Í BÁÐUM FORLYKKJUM
        counter = 0
        for tile_array in self.tiles:
            for tile in tile_array:
                if counter == draw_number:
                    tile_array_index = self.tiles.index(tile_array)
                    tile_index = tile_array.index(tile)
                    ret_tile = self.tiles[tile_array_index].pop(tile_index)
                counter += 1

        self.size -= 1
        return ret_tile

        # Random er ekki nógu gott því ekki sömu líkur á hverju instance af tile
        # index = self.alphabet.index(letter)
        # if self.size == 0:
        #     raise BagEmptyError
        # while self.tiles[index] == []:
        #     index = rd.randint(0,len(self.alphabet)-1)
        # ret_tile = self.tiles[index].pop()

class Tile:
    def __init__(self, letter, points) -> None:
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.letter = letter
        self.points = points

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return self.letter + str(self.points)

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


def test_game():
    game = Game()

    # print(game.players)
    # print(f'Size of bag before draw: {game.bag.size}')

    game.draw_from_bag()

    # for player in game.players:
    #     print(player, player.tiles)
    # print(f'Size of bag after draw: {game.bag.size}')

    game.print_game()

    game.choose()

    game.next_turn()

    game.print_game()

    # game.next_turn()




def test_bag():
    bag = Bag()
    print(bag.tiles)

    print(bag.pop('A'))
    print(bag.pop('A'))
    print(bag.pop('A'))
    print(bag.pop('B'))
    print(bag.pop('Z'))

    print(bag.tiles)

def test_board():
    a = Board()
    print(a)

    a._update_grid((4,'d'), 'A')
    a._update_grid((4,'e'), 'T')
    a._update_grid((4,'f'), 'L')
    a._update_grid((4,'g'), 'I')

    a._update_grid((7,'f'), 'O')
    a._update_grid((7,'g'), 'G')

    a._update_grid((12,'c'), 'J')
    a._update_grid((12,'d'), 'Ó')
    a._update_grid((12,'e'), 'N')
    a._update_grid((12,'f'), 'A')
    a._update_grid((12,'g'), 'S')

    print(a)


if __name__ == "__main__":
    main()
