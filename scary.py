import pygame
import random

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 1300
BLACK = (0, 0, 0)
fps = 0
maxframe = 60
FRAME = pygame.image.load("CAMERA_FRAME.png")
BACKGROUND = pygame.image.load("hospital.png")


def mouse_movement(screen, mouseX, mouseY):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    x = (mouseX - 650 + a)/20*-1
    y = (mouseY - 350 + b)/20*-1
    screen.blit(BACKGROUND, [-150 + x, -150 + y])
    screen.blit(FRAME, [0, 0])

def main():
    pygame.init()
    pygame.display.set_caption("HOSPITAL")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.mixer.music.load("cave.wav")
    pygame.mixer.music.play(-1)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.mouse.set_visible(False)
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse_movement(screen, mouseX, mouseY)
        pygame.display.flip()
        clock.tick(maxframe)

if __name__ == '__main__':
    main()
