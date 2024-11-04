import pygame
import time
import random

# Inizializza Pygame
pygame.init()

# Dimensioni della finestra
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Serpente che Raccoglie Punti")

# Colori
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Configurazioni del gioco
snake_block = 10
snake_speed = 15

# Font per il punteggio
font_style = pygame.font.SysFont("monospace", 35)

# Funzione per mostrare il punteggio
def show_score(score):
    score_display = font_style.render("Punti: " + str(score), True, white)
    screen.blit(score_display, (10, 10))

# Funzione principale del gioco
def game_loop():
    game_over = False
    game_close = False

    # Posizione iniziale del serpente
    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    # Posizione iniziale del punto
    point_x = random.randrange(0, width - snake_block, snake_block)
    point_y = random.randrange(0, height - snake_block, snake_block)

    while not game_over:
        while game_close:
            screen.fill(black)
            message = font_style.render("Hai perso! Premi C per continuare o Q per uscire.", True, red)
            screen.blit(message, (width // 6, height // 3))
            show_score(snake_length - 1)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Controllo i bordi
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(black)

        # Disegna il punto
        pygame.draw.rect(screen, green, [point_x, point_y, snake_block, snake_block])

        # Gestisci il corpo del serpente
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Disegna il serpente
        for segment in snake_list:
            pygame.draw.rect(screen, red, [segment[0], segment[1], snake_block, snake_block])

        show_score(snake_length - 1)  # Mostra il punteggio

        # Controllo se il serpente raccoglie il punto
        if x == point_x and y == point_y:
            point_x = random.randrange(0, width - snake_block, snake_block)
            point_y = random.randrange(0, height - snake_block, snake_block)
            snake_length += 1  # Aumenta la lunghezza del serpente

        pygame.display.update()
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Avvio del gioco
game_loop()






