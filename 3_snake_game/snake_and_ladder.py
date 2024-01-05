import random

class SquareType:
    REGULAR = "Regular"
    SNAKE = "Snake"
    LADDER = "Ladder"

class Square:
    def __init__(self, square_type, position):
        self.type = square_type
        self.position = position

class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Die:
    def roll(self):
        return random.randint(1, 6)

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

class Board:
    def __init__(self, size):
        self.size = size
        self.squares = [Square(SquareType.REGULAR, i) for i in range(1, size + 1)]
        self.snakes = []
        self.ladders = []

    def add_snake(self, snake):
        self.snakes.append(snake)

    def add_ladder(self, ladder):
        self.ladders.append(ladder)

class GameController:
    def __init__(self, players, board_size):
        self.players = players
        self.board = Board(board_size)
        self.die = Die()

    def setup_board(self, snakes, ladders):
        for snake in snakes:
            self.board.add_snake(snake)
        for ladder in ladders:
            self.board.add_ladder(ladder)

    def move_player(self, player, steps):
        current_position = player.position
        new_position = min(current_position + steps, self.board.size)
        for ladder in self.board.ladders:
            if ladder.start == new_position:
                new_position = ladder.end
        for snake in self.board.snakes:
            if snake.start == new_position:
                new_position = snake.end
        player.position = new_position

    def play_turn(self, player):
        roll = self.die.roll()
        print(f"{player.name} rolled a {roll}")
        self.move_player(player, roll)
        print(f"{player.name} is now at position {player.position}")

    def  play_game(self, num_turns):
        for _ in range(num_turns):
            for player in self.players:
                self.play_turn(player)

# Example usage
if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    players = [player1, player2]

    snakes = [Snake(16, 6), Snake(47, 26), Snake(49, 11)]  # Define snakes
    ladders = [Ladder(3, 22), Ladder(5, 8), Ladder(11, 26)]  # Define ladders

    game_controller = GameController(players, board_size=50)
    game_controller.setup_board(snakes, ladders)
    game_controller.play_game(num_turns=10)
