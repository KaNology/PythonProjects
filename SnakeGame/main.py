import pygame
import sys
import time
import random

BLOCK_SIZE = 40
# Initialize Pygame
pygame.init()
GAME_SMALL_FONT = pygame.font.Font('freesansbold.ttf', 16)
GAME_MEDIUM_FONT = pygame.font.Font('freesansbold.ttf', 32)
GAME_BIG_FONT = pygame.font.Font('freesansbold.ttf', 64)

class Snake:
    def __init__(self, screen, length):
        self.length = length
        self.screen = screen
        self.direction = 'down'
        self.image = pygame.image.load("SnakeGame/resources/block.jpg").convert()
        self.x = [BLOCK_SIZE]*length
        self.y = [BLOCK_SIZE]*length

    # When apple eaten, the snake grows by 1
    def grow(self):
        self.length += 1
        self.x.append(1)
        self.y.append(1)

    def draw(self):
        # Have to fill the screen again to remove the afterimages
        # screen.fill((100, 100, 10)) # No need anymore since we have already had the background
        for i in range(self.length):
            self.screen.blit(self.image, (self.x[i], self.y[i]))

    def move_down(self):
        self.direction = 'down'

    def move_up(self):
        self.direction = 'up'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move(self):
        # The previous block will take place of the current block
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # The head's movement
        if self.direction == 'down':
            self.y[0] += BLOCK_SIZE
        elif self.direction == 'up':
            self.y[0] -= BLOCK_SIZE
        elif self.direction == 'left':
            self.x[0] -= BLOCK_SIZE
        elif self.direction == 'right':
            self.x[0] += BLOCK_SIZE
            
        self.draw()

class Apple:
    def __init__(self, screen):
        self.image = pygame.image.load("SnakeGame/resources/apple.jpg").convert()
        self.x = BLOCK_SIZE * 5
        self.y = BLOCK_SIZE * 6
        self.screen = screen

    def draw(self):
        # screen.fill((100, 100, 10))
        self.screen.blit(self.image, (self.x, self.y))

    def teleport(self):
        # Teleporting apple!!!!
        self.x = BLOCK_SIZE * random.randint(1, 24)
        self.y = BLOCK_SIZE * random.randint(1, 9)

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = self.screen_set_up(screen_width, screen_height)
        self.snake = Snake(self.screen, 1)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()
        self.score = 0
        self.running = True
        self.pause = False

    @staticmethod
    def screen_set_up(screen_width, screen_height):
        # Screen Settings
        screen = pygame.display.set_mode([screen_width, screen_height])
        pygame.display.set_caption("Snake Game")
        
        # Changing background color
        # screen.fill((100, 100, 10))

        return screen

    def apple_eaten(self):
        if self.snake.x[0] == self.apple.x and self.snake.y[0] == self.apple.y:
            self.score += 1
            self.snake.grow()
            self.apple.teleport()

    def render_background(self):
        bg = pygame.image.load("SnakeGame/resources/background.jpg")
        self.screen.blit(bg, (0,0))

    # Check if another snake bites the dust!!
    def snake_bitten(self):
        for i in range(1, self.snake.length):
            if self.snake.x[0] == self.snake.x[i] and self.snake.y[0] == self.snake.y[i]:
                self.running = False

    # There are two ways to deal with when the snake touches the screen
    # - Game ends (easy)
    # - Snake moves through the screen (imma do this)
    def snake_through_screen(self):
        if self.snake.x[0] < 0:
            self.snake.x[0] = self.screen_width
        elif self.snake.x[0] == self.screen_width:
            self.snake.x[0] = -BLOCK_SIZE
        elif self.snake.y[0] < 0:
            self.snake.y[0] = self.screen_height
        elif self.snake.y[0] == self.screen_height:
            self.snake.y[0] = -BLOCK_SIZE

    def display_score(self):
        text = GAME_SMALL_FONT.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(text, (10,10))

    def display_pause(self):
        text = GAME_MEDIUM_FONT.render(f"Game Paused", True, (255, 255, 255))
        self.screen.blit(text, (self.screen_width/2,self.screen_height/2))

    def play(self):
            # Render the background once a loop to remove all after images
            self.render_background()
            self.display_score()
            self.snake.move()
            self.apple.draw()
            self.apple_eaten()
            self.snake_bitten()
            self.snake_through_screen()
            time.sleep(0.2)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

                    if event.key == pygame.K_p:
                        self.pause = not self.pause
                        if self.pause:
                            self.display_pause()

                    if not self.pause:
                        if event.key == pygame.K_UP:
                            if self.snake.direction != 'down':
                                self.snake.move_up()
                        elif event.key == pygame.K_DOWN:
                            if self.snake.direction != 'up':
                                self.snake.move_down()
                        elif event.key == pygame.K_LEFT:
                            if self.snake.direction != 'right':
                                self.snake.move_left()
                        elif event.key == pygame.K_RIGHT:
                            if self.snake.direction != 'left':
                                self.snake.move_right()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if not self.pause:
                self.play()
            
            # Update the screen
            pygame.display.flip()

if __name__ == "__main__":
    game = Game(1000, 800)
    game.run()