import pygame
import pygame_menu

from random import randint
from copy import deepcopy


RES = WIDTH, HEIGHT = 1600, 900
Cell = 25
W, H = WIDTH // Cell, HEIGHT // Cell
FPS = 1
FPS1 = 100




pygame.init()


surface = pygame.display.set_mode(RES)
pygame.display.set_caption("Game of Life")
pygame.display.set_icon(pygame.image.load("gvz.png"))
clock = pygame.time.Clock()





def random_field():

    next_field = [[0 for i in range(W)] for j in range(H)]
    current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]

    def check_cell(current_field, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field[j][i]:
                    count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0

    while True:

        surface.fill(pygame.Color('black'))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.mainloop(surface)
                    return


        [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, Cell)]
        [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, Cell)]

        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(surface, pygame.Color('forestgreen'),
                                     (x * Cell + 2, y * Cell + 2, Cell - 2, Cell - 2))
                next_field[y][x] = check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

        print(clock.get_fps())
        pygame.display.update()
        clock.tick(FPS)
    pass

def custom_field1():
    next_field = [[0 for i in range(W)] for j in range(H)]
    current_field = [[1 if not i % 9 else 0 for i in range(W)] for j in range(H)]


    def check_cell(current_field, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field[j][i]:
                    count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0

    while True:

        surface.fill(pygame.Color('black'))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    men
                    return

        [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, Cell)]
        [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, Cell)]

        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(surface, pygame.Color('forestgreen'),
                                     (x * Cell + 2, y * Cell + 2, Cell - 2, Cell - 2))
                next_field[y][x] = check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

        print(clock.get_fps())
        pygame.display.update()
        clock.tick(FPS)
    pass

def custom_field2():
    next_field = [[0 for i in range(W)] for j in range(H)]
    current_field = [[1 if not (2 * i + j) % 4 else 0 for i in range(W)] for j in range(H)]


    def check_cell(current_field, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field[j][i]:
                    count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0

    while True:

        surface.fill(pygame.Color('black'))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    men
                    return

        [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, Cell)]
        [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, Cell)]

        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(surface, pygame.Color('forestgreen'),
                                     (x * Cell + 2, y * Cell + 2, Cell - 2, Cell - 2))
                next_field[y][x] = check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

        print(clock.get_fps())
        pygame.display.update()
        clock.tick(FPS)
    pass

def custom_field3():
    next_field = [[0 for i in range(W)] for j in range(H)]
    current_field = [[1 if not (i * j) % 22 else 0 for i in range(W)] for j in range(H)]

    def check_cell(current_field, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field[j][i]:
                    count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0

    while True:

        surface.fill(pygame.Color('black'))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    men
                    return

        [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, Cell)]
        [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, Cell)]

        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(surface, pygame.Color('forestgreen'),
                                     (x * Cell + 2, y * Cell + 2, Cell - 2, Cell - 2))
                next_field[y][x] = check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

        print(clock.get_fps())
        pygame.display.update()
        clock.tick(FPS)
    pass


def custom_field4():
    next_field = [[0 for i in range(W)] for j in range(H)]
    current_field = [[1 if i == W // 2 or j == H // 2 else 0 for i in range(W)] for j in range(H)]

    def check_cell(current_field, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field[j][i]:
                    count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0

    while True:

        surface.fill(pygame.Color('black'))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    men
                    return

        [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, Cell)]
        [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, Cell)]

        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(surface, pygame.Color('forestgreen'),
                                     (x * Cell + 2, y * Cell + 2, Cell - 2, Cell - 2))
                next_field[y][x] = check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

        print(clock.get_fps())
        pygame.display.update()
        clock.tick(FPS)
    pass

def urself_field():
    next_field = [[0 for i in range(W)] for j in range(H)]
    current_field = [[0 for i in range(W)] for j in range(H)]


    def check_cell(current_field, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if current_field[j][i]:
                    count += 1

        if current_field[y][x]:
            count -= 1
            if count == 2 or count == 3:
                return 1
            return 0
        else:
            if count == 3:
                return 1
            return 0



    while True:

        surface.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            pressed = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu.mainloop(surface)
                    return
            if pressed[0]:
                if pos[0] in range(0,1590) and pos[1] in range(0,890):
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    column = (x_mouse+2) // Cell
                    row = (y_mouse+2) // Cell
                    current_field[row][column] = 1
            if pressed[2]:
                if pos[0] in range(0, 1590) and pos[1] in range(0, 890):
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    column = (x_mouse+2) // Cell
                    row = (y_mouse+2) // Cell
                    current_field[row][column] = 0

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    while True:
                        surface.fill(pygame.Color('black'))
                        for event in pygame.event.get():

                            if event.type == pygame.QUIT:
                                exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    menu.mainloop(surface)
                                    return


                        [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in
                         range(0, WIDTH, Cell)]
                        [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in
                         range(0, HEIGHT, Cell)]

                        for x in range(1, W -1):
                            for y in range(1, H -1):
                                if current_field[y][x]:
                                    pygame.draw.rect(surface, pygame.Color('forestgreen'),
                                                     (x * Cell + 2, y * Cell + 2, Cell - 2, Cell - 2))
                                next_field[y][x] = check_cell(current_field, x, y)

                        current_field = deepcopy(next_field)

                        print(clock.get_fps())
                        pygame.display.update()
                        clock.tick(FPS)

        [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, Cell)]
        [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, Cell)]

        for x in range(1, W-1):
            for y in range(1, H-1):
                if current_field[y][x]:
                    color = "forestgreen"
                else:
                    color = "black"
                pygame.draw.rect(surface, color, (x * Cell + 2, y * Cell + 2, Cell - 2, Cell - 2))


        print(clock.get_fps())
        pygame.display.flip()
        clock.tick(FPS1)
    pass


def men():
    menu2=pygame_menu.Menu(900,1600, "Game of Life", theme=pygame_menu.themes.THEME_DARK, mouse_motion_selection = True)
    menu2.add_button("Custom field1", custom_field1)
    menu2.add_button("Custom field2", custom_field2)
    menu2.add_button("Custom field3", custom_field3)
    menu2.add_button("Custom field4", custom_field4)
    menu2.add_button('Back', menu)
    menu2.mainloop(surface)
    pass

def menu3():
    menu3=pygame_menu.Menu(900,1600, "Game of Life", theme=pygame_menu.themes.THEME_DARK, mouse_motion_selection = True)
    menu3.add_label('Left click to make cell alive')
    menu3.add_label('Right click to make cell dead')
    menu3.add_label('Enter to start')
    menu3.add_label('Escape to return to menu')
    menu3.add_button("Okay", urself_field)
    menu3.mainloop(surface)
    pass

menu = pygame_menu.Menu(900,1600, "Game of Life", theme=pygame_menu.themes.THEME_DARK, mouse_motion_selection = True)

def FPS_change(selected):
    value_tuple, index = selected
    print('Change widget fps to', value_tuple[0])
    print(selected[0])
    global FPS
    FPS = int(selected[0])
    print(type(FPS))

volume = 1
def volume_change(selected,koki,**kwargs):
    global volume
    volume = float(selected[0][1])
    print(selected[0][1])
    print(selected)
    print(volume)
    pygame.mixer.music.set_volume(volume)


items= [
    ('10', 1),
    ('7', 0.7),
    ('4', 0.4),
    ('1', 0.1)]
selector2 = menu.add_selector('Volume  ', items=items, onchange=volume_change,onreturn=volume_change)


pygame.mixer.music.load("Aphex Twin - Stone In Focus.mp3")
pygame.mixer.music.play(-1)

selector = menu.add_selector('Change speed ', [
    ('1'),
    ('3'),
    ('5'),
    ('9')], onchange=FPS_change)
menu.add_button('Random field', random_field)
menu.add_button('Custom field', men)
menu.add_button("Create yourself field", menu3)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)






