import random
import pygame
from enum import Enum

class Misc(Enum):
    screen_length = 1000
    screen_width = 1000

class Snake_Board:
    def __init__(self, **kwargs):
        self.length = kwargs.get("length")
        self.width = kwargs.get("width")
        self.current_state = [[0 for col in range(self.width)] for row in range(self.length)]
        self.SCREEN = kwargs.get("screen")

    def food_on_board(self):
        for i in self.current_state:
            if sum(i) > 0:
                return True
        return False

class Snake:
    def __init__(self, **kwargs):
        self.initial_direction = kwargs.get("initial_direction")
        self.SCREEN = kwargs.get("screen")
        self.snake_body = [(5, 5), (5, 6), (5, 7)]
        self.snake_head_direction = self.initial_direction

    def get_snake_head(self):
        return self.snake_body[0]

    def check_collision(self):
        if self.snake_body[0][0] > 9 or \
            self.snake_body[0][0] < 0 or \
            self.snake_body[0][1] > 9 or \
            self.snake_body[0][1] < 0:
            return True

        for i in range(1, len(self.snake_body)):
            if self.snake_body[i] == self.snake_body[0]:
                return True
        return False

    def update_snake_board(self, snake_board, value = 0):
        for coords in self.snake_body:
            snake_board.current_state[coords[0]][coords[1]] = value

    def move(self, snake_board, next_move):
        self.update_snake_board(snake_board) 
        if self.snake_head_direction == "N":
            new_head = (self.snake_body[0][0] - 1, self.snake_body[0][1])
        elif self.snake_head_direction == "S":
            new_head = (self.snake_body[0][0] + 1, self.snake_body[0][1])
        elif self.snake_head_direction == "E":
            new_head = (self.snake_body[0][0], self.snake_body[0][1] + 1)
        elif self.snake_head_direction == "W":
            new_head = (self.snake_body[0][0], self.snake_body[0][1] - 1)
        if self.valid_new_head(new_head) and snake_board.current_state[new_head[0]][new_head[1]] == 0:
            self.snake_body.pop()
        elif self.valid_new_head(new_head):
            snake_board.current_state[new_head[0]][new_head[1]] = 0
        self.snake_body.insert(0, new_head)
        self.update_snake_board(snake_board, 2)
        is_game_over = self.check_collision()
        return is_game_over

    def valid_new_head(self, new_head):
        if new_head[0] > 9 or new_head[0] < 0 or new_head[1] > 9 or new_head[1] < 0:
            return False
        return True

    def capture_input(self):
        pass

    def draw_board(self):
        self.SCREEN.fill((255, 255, 255))

    def render(self, **kwargs):
        snake_board = kwargs.get("snake_board")
        # for i in snake_board.current_state:
        #     print(i)
        # print()

        pygame.init()
        
        # Set up display
        snake_board.SCREEN = screen.set_caption("Snake-Game")
        
        # Calculate the size of each block
        block_size = 1000 // snake_board.length
        
        # Run until the user closes the window
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Draw the chessboard
            for row in range(num_blocks):
                for col in range(num_blocks):
                    # Alternate colors
                    color = (0, 0, 0) if (row + col) % 2 == 0 else (255, 255, 255)
                    pygame.draw.rect(screen, color, (col * block_size, row * block_size, block_size, block_size))
            
            # Update the display
            pygame.display.flip()
        
        # Quit pygame
        pygame.quit()
        sys.exit()
        # for i in snake_board.current_state:
        #     pygame.draw.rect(self.SCREEN, Colors.MAUVE.value, (j*(self.box_length), i*(self.box_length), (self.box_length), (self.box_length)))
        

class Food:
    def __init__(self):
        pass
    def randomizer(self):
        return(random.randint(0, 9), random.randint(0, 9))
        

class Score:
    def __init__(self):
        pass

class Snake_game:
    def __init__(self):
        snake_board_kwargs = {"length": 10, "width": 10, "screen": pygame.display.set_mode((1000, 1000))}
        self.snake_board = Snake_Board(**snake_board_kwargs)
        self.snake = Snake(initial_direction = "N")
        self.food = Food()
        self.is_game_over = False

    def start_game(self):
        input_direction = 'N'
        while(not self.is_game_over):
            # print("Current state", self.snake_board.current_state)
            if (not self.snake_board.food_on_board()):
                print("generating new food")
                food_location_x, food_location_y = self.food.randomizer()
                print("food location", food_location_x, food_location_y)
                self.snake_board.current_state[food_location_x][food_location_y] = 1
            self.is_game_over = self.snake.move(self.snake_board, input_direction)
            # print("Moved one block")
            self.snake.render(snake_board = self.snake_board)
            # print("snake body", self.snake.snake_body)
            # print("game over", self.is_game_over)


def main():
    snake_game = Snake_game()
    snake_game.start_game()

if __name__ == "__main__":
    main()
