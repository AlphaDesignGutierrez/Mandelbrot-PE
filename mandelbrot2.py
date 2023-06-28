import time
import pygame
import sys

pygame.font.init()

time1 = time.time()


window_x = 1280
window_y = 720
black = (0, 0, 0)
white = (255, 255, 255)
bailout = 2.0
max_i = 100
size = 720.0
red = 0
green = 0
blue = 0
x = -0.2
y = 0.0
time_a = 0


screen = pygame.display.set_mode((window_x, (window_y + 30)))

textfont = pygame.font.SysFont("monospace", 20)


def m1():
    stop = 0
    timee = time.time() + 0.5
    
    for j in range(int(window_y / 2)):
        if (timee < time.time()):
            timee = (timee + 0.5)
            for k in range(30):
                pygame.draw.lines(screen, (0, 0, 0), False, [(0, k + window_y), (window_x, k + window_y)], 1)
            textTBD = textfont.render("T: ", 2, (255, 255, 255))
            screen.blit(textTBD, (10, window_y + 5))
            textTBD = textfont.render(str(int((time.time() - time_a) * 1000) / 1000), 2, (255, 255, 255))
            screen.blit(textTBD, (40, window_y + 5))
            textTBD = textfont.render("Iterations: ", 2, (255, 255, 255))
            screen.blit(textTBD, (120, window_y + 5))
            textTBD = textfont.render(str(max_i), 2, (255, 255, 255))
            screen.blit(textTBD, (260, window_y + 5))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    stop = 1
            pygame.display.update()
        if (stop == 0):
            for i in range(window_x):
                c = complex(4 * (x * size + i - window_x / 2) / size, 4 * (y * size + (j + window_y / 2) - window_y / 2) /
                            size)
                z = 0j
                n = 0
                if (((c.real+1) * (c.real+1))+(c.imag * c.imag)) < (0.0625):
                    n = max_i 
                while (abs(z) < bailout) and (n < max_i):
                    z = z * z+c
                    n += 1
                if (abs(z) >= bailout):
                    colour = ((red + 10 * n) % 255, (green + 3 * n) % 255, (blue + 7 *
                                                                        n) % 255)
                    pygame.draw.lines(screen, colour, False, [(i, (j + int(window_y / 2))), (i, (j + int(window_y / 2)))], 1)
                elif (n >= max_i):
                    pygame.draw.lines(screen, (0, 0, 0), False, [(i, (j + int(window_y / 2))), (i, (j + int(window_y / 2)))], 1)
            for i in range(window_x):
                c = complex(4 * (x * size + i - window_x / 2) / size, 4 * (y * size + (int(window_y / 2) - j) - window_y / 2) /
                            size)
                z = 0j
                n = 0
                if (((c.real+1) * (c.real+1))+(c.imag * c.imag)) < (0.0625):
                    n = max_i 
                while (abs(z) < bailout) and (n < max_i):
                    z = z * z+c
                    n += 1
                if (abs(z) >= bailout):
                    colour = ((red + 10 * n) % 255, (green + 3 * n) % 255, (blue + 7 *
                                                                        n) % 255)
                    pygame.draw.lines(screen, colour, False, [(i, (int(window_y / 2) - j)), (i, (int(window_y / 2) - j))], 1)
                elif (n >= max_i):
                    pygame.draw.lines(screen, (0, 0, 0), False, [(i, (int(window_y / 2) - j)), (i, (int(window_y / 2) - j))], 1)
                
if (__name__ == '__main__'):
    time_a = time.time()
    m1()
    for k in range(30):
        pygame.draw.lines(screen, (0, 0, 0), False, [(0, k + window_y), (window_x, k + window_y)], 1)
    textTBD = textfont.render("T: ", 2, (255, 255, 255))
    screen.blit(textTBD, (10, window_y + 5))
    textTBD = textfont.render(str(int((time.time() - time_a) * 1000) / 1000), 2, (255, 255, 255))
    screen.blit(textTBD, (40, window_y + 5))
    textTBD = textfont.render("Iterations: ", 2, (255, 255, 255))
    screen.blit(textTBD, (120, window_y + 5))
    textTBD = textfont.render(str(max_i), 2, (255, 255, 255))
    screen.blit(textTBD, (260, window_y + 5))
    while True:
        time.sleep(0.03)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                le, mi,ri = pygame.mouse.get_pressed()
                posx, posy = pygame.mouse.get_pos()
                if (le):
                    
                    x = (((posx - window_x / 2.0) / size))+ x
                    y = (((posy - window_y / 2.0) / size))+ y
                    size = size * 4
                    time_a = time.time()
                    m1()
                    for k in range(30):
                        pygame.draw.lines(screen, (0, 0, 0), False, [(0, k + window_y), (window_x, k + window_y)], 1)
                    textTBD = textfont.render("T: ", 2, (255, 255, 255))
                    screen.blit(textTBD, (10, window_y + 5))
                    textTBD = textfont.render(str(int((time.time() - time_a) * 1000) / 1000), 2, (255, 255, 255))
                    screen.blit(textTBD, (40, window_y + 5))
                    textTBD = textfont.render("Iterations: ", 2, (255, 255, 255))
                    screen.blit(textTBD, (120, window_y + 5))
                    textTBD = textfont.render(str(max_i), 2, (255, 255, 255))
                    screen.blit(textTBD, (260, window_y + 5))
                elif (mi):
                    max_i = posx
                    time_a = time.time()
                    m1()
                    for k in range(30):
                        pygame.draw.lines(screen, (0, 0, 0), False, [(0, k + window_y), (window_x, k + window_y)], 1)
                    textTBD = textfont.render("T: ", 2, (255, 255, 255))
                    screen.blit(textTBD, (10, window_y + 5))
                    textTBD = textfont.render(str(int((time.time() - time_a) * 1000) / 1000), 2, (255, 255, 255))
                    screen.blit(textTBD, (40, window_y + 5))
                    textTBD = textfont.render("Iterations: ", 2, (255, 255, 255))
                    screen.blit(textTBD, (120, window_y + 5))
                    textTBD = textfont.render(str(max_i), 2, (255, 255, 255))
                    screen.blit(textTBD, (260, window_y + 5))
                elif (ri):
                    size = size / 4
                    time_a = time.time()
                    m1()
                    for k in range(30):
                        pygame.draw.lines(screen, (0, 0, 0), False, [(0, k + window_y), (window_x, k + window_y)], 1)
                    textTBD = textfont.render("T: ", 2, (255, 255, 255))
                    screen.blit(textTBD, (10, window_y + 5))
                    textTBD = textfont.render(str(int((time.time() - time_a) * 1000) / 1000), 2, (255, 255, 255))
                    screen.blit(textTBD, (40, window_y + 5))
                    textTBD = textfont.render("Iterations: ", 2, (255, 255, 255))
                    screen.blit(textTBD, (120, window_y + 5))
                    textTBD = textfont.render(str(max_i), 2, (255, 255, 255))
                    screen.blit(textTBD, (260, window_y + 5))
        
                
        pygame.display.update()