import pygame
import random

# Inicializar o pygame
pygame.init()

# Define as dimensões da tela
width = 500
height = 500

# Cria a tela
screen = pygame.display.set_mode((width, height))

# Define o título da janela
pygame.display.set_caption("Jogo Snake")

# Define as cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define a velocidade da cobra
x_velocity = 0
y_velocity = 0

# Define a posição inicial da cobra
x_pos = 300
y_pos = 300

# Define a posição inicial da maçã
apple_x = random.randint(0, width - 10)
apple_y = random.randint(0, height - 10)

# Define o tamanho da cobra
snake_block = 10
snake_speed = 10

# Cria um relógio para controlar a velocidade do jogo
clock = pygame.time.Clock()

# Executa o jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_velocity = -snake_speed
                y_velocity = 0
            elif event.key == pygame.K_RIGHT:
                x_velocity = snake_speed
                y_velocity = 0
            elif event.key == pygame.K_UP:
                y_velocity = -snake_speed
                x_velocity = 0
            elif event.key == pygame.K_DOWN:
                y_velocity = snake_speed
                x_velocity = 0

    # Atualiza a posição da cobra
    x_pos += x_velocity
    y_pos += y_velocity

    # Preenche a tela com a cor preta
    screen.fill(black)

    # Desenha a maçã na tela
    pygame.draw.rect(screen, red, (apple_x, apple_y, snake_block, snake_block))

    # Desenha a cobra na tela
    pygame.draw.rect(screen, white, (x_pos, y_pos, snake_block, snake_block))

    # Atualiza a tela
    pygame.display.update()

    # Controla a velocidade do jogo
    clock.tick(30)

# Encerra o pygame
pygame.quit()
