import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Runner")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
PURPLE = (128, 0, 128)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

def mensaje_perdida():
    texto = font.render("¡Has perdido!", True, RED)
    screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(2000)  



colores_personaje = [PURPLE, RED, GREEN, YELLOW, CYAN]
indice_color = 0
color_personaje = colores_personaje[indice_color]

tamañojugador = 50
posicionjugador = [WIDTH // 2, HEIGHT - tamañojugador - 10]
velocidadjugador = 5

tamañomalos = 50
velocidadmalos = 5
malos = []

def crear_malos():
    x_pos = random.randint(0, WIDTH - tamañomalos)
    y_pos = 0
    malos.append(pygame.Rect(x_pos, y_pos, tamañomalos, tamañomalos))

def movimientomalos():
    for malo in malos:
        malo.y += velocidadmalos

def dibujomalos():
    for malo in malos:
        pygame.draw.rect(screen, BLUE, malo)

def choque(jugador_rect):
    for malo in malos:
        if jugador_rect.colliderect(malo):
            return True
    return False


font = pygame.font.SysFont("Arial", 30)

def menu_opciones():
    global color_personaje, indice_color
    opciones = ["Iniciar Juego", "Cambiar Color", "Salir"]
    seleccion = 0
    en_menu = True
    cambiando_color = False

    while en_menu:
        screen.fill(BLACK)
        for i, opcion in enumerate(opciones):
            color = WHITE
            if i == seleccion:
                color = YELLOW
            texto = font.render(opcion, True, color)
            screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 200 + i * 50))

        if cambiando_color:
            color_preview = colores_personaje[indice_color]
            preview = pygame.Rect(WIDTH // 2 - 25, 400, 50, 50)
            pygame.draw.rect(screen, color_preview, preview)
            info = font.render("← / → para cambiar color, ENTER para confirmar", True, WHITE)
            screen.blit(info, (WIDTH // 2 - info.get_width() // 2, 470))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if cambiando_color:
                    if event.key == pygame.K_LEFT:
                        indice_color = (indice_color - 1) % len(colores_personaje)
                    elif event.key == pygame.K_RIGHT:
                        indice_color = (indice_color + 1) % len(colores_personaje)
                    elif event.key == pygame.K_RETURN:
                        color_personaje = colores_personaje[indice_color]
                        cambiando_color = False
                else:
                    if event.key == pygame.K_UP:
                        seleccion = (seleccion - 1) % len(opciones)
                    elif event.key == pygame.K_DOWN:
                        seleccion = (seleccion + 1) % len(opciones)
                    elif event.key == pygame.K_RETURN:
                        if opciones[seleccion] == "Iniciar Juego":
                            en_menu = False
                        elif opciones[seleccion] == "Cambiar Color":
                            cambiando_color = True
                        elif opciones[seleccion] == "Salir":
                            pygame.quit()
                            sys.exit()

def game_loop():
    jugador = pygame.Rect(posicionjugador[0], posicionjugador[1], tamañojugador, tamañojugador)
    tiempo = 0
    corre = True
    reloj = pygame.time.Clock()

    while corre:
        reloj.tick(60)
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and jugador.left > 0:
            jugador.x -= velocidadjugador
        if keys[pygame.K_RIGHT] and jugador.right < WIDTH:
            jugador.x += velocidadjugador

        if tiempo <= 0:
            crear_malos()
            tiempo = 30
        else:
            tiempo -= 1

        movimientomalos()
        dibujomalos()
        pygame.draw.rect(screen, color_personaje, jugador)

        if choque(jugador):
            mensaje_perdida()
            corre = False

        pygame.display.update()


while True:
    menu_opciones()
    game_loop()


                