from enum import Enum
from random import randint

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    THERE = 5

class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.food = Food()
        self.place_food()

    def place_food(self):
        self.food.generate_position(self.width, self.height)
        while self.food.position in self.snake.body:
            self.food.generate_position(self.width, self.height)

    def update_board(self):
        self.snake.move()
        if self.snake.head == self.food.position:
            self.snake.grow()
            self.place_food()

        if self.is_collision():
            print("Game Over!")
            exit()

    def is_collision(self):
        # Check if Snake collides with itself or hits the walls
        return (
            self.snake.head in self.snake.body[1:] or
            self.snake.head[0] < 0 or self.snake.head[0] >= self.width or
            self.snake.head[1] < 0 or self.snake.head[1] >= self.height
        )

    def display(self):
        for row in range(self.height):
            for col in range(self.width):
                if (col, row) == self.snake.head:
                    print("H", end=" ")
                elif (col, row) in self.snake.body:
                    print("S", end=" ")
                elif (col, row) == self.food.position:
                    print("F", end=" ")
                else:
                    print(".", end=" ")
            print()

class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.direction = Direction.THERE

    @property
    def head(self):
        return self.body[0]

    def move(self):
        x, y = self.head
        if self.direction == Direction.UP:
            y -= 1
        elif self.direction == Direction.DOWN:
            y += 1
        elif self.direction == Direction.LEFT:
            x -= 1
        elif self.direction == Direction.RIGHT:
            x += 1

        self.body.insert(0, (x, y))
        self.body = self.body[:len(self.body) - 1]

    def grow(self):
        x, y = self.head
        if self.direction == Direction.UP:
            y -= 1
        elif self.direction == Direction.DOWN:
            y += 1
        elif self.direction == Direction.LEFT:
            x -= 1
        elif self.direction == Direction.RIGHT:
            x += 1

        self.body.insert(0, (x, y))

class Food:
    def __init__(self):
        self.position = (5, 5)

    def generate_position(self, width, height):
        self.position = (randint(0, width - 2), randint(0, height - 2))

class GameController:
    def __init__(self, width, height):
        self.game_board = GameBoard(width, height)

    def run_game(self):
        while True:
            self.game_board.update_board()
            self.game_board.display()
            self.handle_user_input()

    def handle_user_input(self):
        user_input = input("Enter direction (W/A/S/D): ").upper()
        if user_input == "W":
            self.game_board.snake.direction = Direction.UP
        elif user_input == "A":
            self.game_board.snake.direction = Direction.LEFT
        elif user_input == "S":
            self.game_board.snake.direction = Direction.DOWN
        elif user_input == "D":
            self.game_board.snake.direction = Direction.RIGHT

# Example usage
if __name__ == "__main__":
    game_controller = GameController(width=10, height=10)
    game_controller.run_game()
