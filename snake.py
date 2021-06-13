import pygame
import random
import os
pygame.init()
pygame.mixer.init()



#Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)


screen_width = 900
screen_height = 600

# to display window or creating window
gameWindow = pygame.display.set_mode((screen_width , screen_height))

pygame.display.set_caption("Snake game by Abhay")

#background image
bgimg = pygame.image.load("snakebg.png")
bgimg = pygame.transform.scale(bgimg , (screen_width,screen_height))

pygame.display.update()
clock = pygame.time.Clock()

#Game Specific Variables

# exit_game = False
# game_over = False
# snake_x = 45
# snake_y = 55
# snake_size = 10
# fps = 50
# velocity_x = 0
# velocity_y = 0
# init_velocity = 5
# food_x = random.randint(20, screen_width/2)
# food_y = random.randint(20, screen_height/2)
# score = 0
# clock = pygame.time.Clock()
font = pygame.font.SysFont(None , 55)



def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
     pygame.draw.rect(gameWindow,color, [x, y, snake_size, snake_size])


# snk_list = []
# snk_length = 1

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((232,220,225))
        text_screen("Welcome to Snake Game",black,260 , 250)
        text_screen("Press Enter to Play", black, 260, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

            pygame.mixer.music.load('battle1.mp3')
            pygame.mixer.music.play()

        pygame.display.update()
        clock.tick(50)


# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    fps = 20
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    clock = pygame.time.Clock()
    # font = pygame.font.SysFont(None, 55)
    snk_list = []
    snk_length = 1
    #check if highscore.txt file exists
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f:
            f.write("0")

    with open("highscore.txt") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            gameWindow.fill((233,230,200))
            text_screen("Game Over!",red, 260,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10



            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score += 10
                # pygame.mixer.music.load('Arrow+Swoosh+1.mp3')
                # pygame.mixer.music.play()
                # print(f"score: {score}")

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 3
                if score>int(highscore):
                    highscore= score
                    with open("highscore.txt", "w") as f:
                        f.write(str(highscore))


            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen(f"Score: {score} , Highscore: {highscore}", red, 3, 3)

            pygame.draw.rect(gameWindow, white, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('Explosion+3.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                # print("Game Over")
                pygame.mixer.music.load('Explosion+3.mp3')
                pygame.mixer.music.play()


            plot_snake(gameWindow,black,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
