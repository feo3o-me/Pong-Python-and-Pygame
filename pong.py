import pygame

def main():
    pygame.init()

    # ========= #
    # Constants

    FPS = 75
    WIDTH = 800
    HEIGHT = 600
    BACKGROUD_COLOR = "#00335E"
    LINE_COLOR = "#A0DCE4"
    RECT_COLOR = "#FFFFFF"
    BALL_COLOR = "#FF5D5D"

    # ========= #
    # Game Objects

    ball = pygame.Rect((WIDTH / 2 - 15), (HEIGHT / 2 - 15), 30, 30) # x pos, y pos, width, height
    player1 = pygame.Rect(10, (HEIGHT / 2 - 70), 10, 140)
    player2 = pygame.Rect((WIDTH - 20), (HEIGHT / 2 - 70), 10, 140)

    ball_speed_x = 5
    ball_speed_y = 5
    player1_speed = 0
    player2_speed = 0
    
    # ========= #
    # Main Loop

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    run = True

    clock = pygame.time.Clock()

    while run:
        # Check For Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_speed -= 5
                if event.key == pygame.K_s:
                    player1_speed += 5
                if event.key == pygame.K_UP:
                    player2_speed -= 5
                if event.key == pygame.K_DOWN:
                    player2_speed += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1_speed += 5
                if event.key == pygame.K_s:
                    player1_speed -= 5
                if event.key == pygame.K_UP:
                    player2_speed += 5
                if event.key == pygame.K_DOWN:
                    player2_speed -= 5

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Player movement
        player1.y += player1_speed
        player2.y += player2_speed

        # Add collision
        if ball.bottom >= HEIGHT or ball.top <= 0:
            ball_speed_y *= -1
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed_x *= -1

        if player1.top <= 0:
            player1.top = 0
        if player1.bottom >= HEIGHT:
            player1.bottom = HEIGHT

        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= HEIGHT:
            player2.bottom = HEIGHT

        window.fill(BACKGROUD_COLOR)
        pygame.draw.aaline(window, LINE_COLOR, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
        pygame.draw.rect(window, RECT_COLOR, player1)
        pygame.draw.rect(window, RECT_COLOR, player2) 
        pygame.draw.ellipse(window, BALL_COLOR, ball)
    
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()