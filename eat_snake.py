import pygame as pg
from random import randint
import sys


def start_game():
    pg.init()
    pg.event.clear()
    windows = pg.display.set_mode((800, 500))
    pg.display.set_caption('贪吃蛇')
    ticks = 4
    clock = pg.time.Clock()
    color = (200, 200, 240)
    windows.fill(color)
    icon = pg.image.load('icon.bmp')
    pg.display.set_icon(icon)

    body = pg.image.load('snake_body.bmp')
    head = pg.image.load('snake.bmp')
    sx = 281
    sy = 221
    windows.blit(head, (281, 221))
    windows.blit(body, (261, 221))
    look = 'right'
    snake_list = [[281, 221], [261, 221]]
    look_list = ['right', 'right']

    p_times = 0
    x, y = randint(21, 781), randint(21, 481)
    x = x // 20 * 20 + 1
    y = y // 20 * 20 + 1
    while [x, y] in snake_list:
        x1 = randint(20, 100)
        y1 = randint(20, 100)
        x1 = x1 // 20 * 20
        y1 = y1 // 20 * 20
        x += x1
        y += y1
    food = pg.image.load('food.bmp')
    windows.blit(food, (x, y))
    p_times += 1

    pg.event.set_blocked([
        pg.MOUSEMOTION,
        pg.MOUSEBUTTONUP,
        pg.MOUSEBUTTONDOWN,
        pg.MOUSEWHEEL,
        pg.KEYUP,
        pg.WINDOWEVENT,
        pg.TEXTEDITING,
        pg.ACTIVEEVENT])

    eat = False
    run = True
    win = False

    while run:
        allow_f = True
        f_t = 1
        for click in pg.event.get():
            if click.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif click.type == pg.KEYDOWN and allow_f:
                if (click.key == pg.K_RIGHT or click.key == pg.K_d) and look != 'left':
                    look = 'right'
                    allow_f = False
                elif (click.key == pg.K_LEFT or click.key == pg.K_a) and look != 'right':
                    look = 'left'
                    allow_f = False
                elif (click.key == pg.K_DOWN or click.key == pg.K_s) and look != 'upper':
                    look = 'lower'
                    allow_f = False
                elif (click.key == pg.K_UP or click.key == pg.K_w) and look != 'lower':
                    look = 'upper'
                    allow_f = False
                if click.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if f_t > 124:
                break
            f_t += 1

        l = -1
        for nmsl in look_list:
            if -l < len(look_list):
                look_list[l] = look_list[l - 1][:]
            l -= 1
        look_list[0] = look[:]
        l = -1
        for gan in snake_list:
            if -l < len(snake_list):
                snake_list[l] = snake_list[l - 1][:]
            l -= 1

        if look == 'right':
            sx += 20
        elif look == 'left':
            sx -= 20
        elif look == 'lower':
            sy += 20
        elif look == 'upper':
            sy -= 20
        snake_list[0] = [sx, sy][:]

        d_a = 0
        for draw in snake_list:
            if d_a == 0:
                windows.blit(head, draw)
            else:
                windows.blit(body, draw)
            d_a += 1

        if (x == sx) and (y == sy):
            eat = True

        if eat:
            pt = 0
            x, y = randint(21, 781), randint(21, 481)
            x = x // 20 * 20 + 1
            y = y // 20 * 20 + 1
            while [x, y] in snake_list:
                x1 = randint(20, 100)
                y1 = randint(20, 100)
                x1 = x1 // 20 * 20
                y1 = y1 // 20 * 20
                x += x1
                y += y1
                if pt > 992:
                    win = True
                    run = False
                    break
                pt += 1
            windows.blit(food, (x, y))

            p_times += 1
            nx = snake_list[-1]
            look_key = look_list[-1]
            if look_key == 'right':
                n_x = nx[0] - 20
                n_y = nx[1]
            elif look_key == 'left':
                n_x = nx[0] + 20
                n_y = nx[1]
            elif look_key == 'lower':
                n_x = nx[0]
                n_y = nx[1] - 20
            elif look_key == 'upper':
                n_x = nx[0]
                n_y = nx[1] + 20
            n_xy = [n_x, n_y]
            snake_list.append(n_xy[:])

            look_list.append(look_key[:])

            print('-----------------------------NEXT---TICK-----------------------------')
            print('生成食物总次数为:', p_times)
            print('吃掉了', p_times - 1, '个食物')
            print('长度为:', len(snake_list))
            print('吃后坐标为：', snake_list)
            print('吃后朝向为：', look_list)

            eat = False
        else:
            windows.blit(food, (x, y))

        if snake_list[0][0] < 1 or snake_list[0][1] < 1:
            run = False
        elif snake_list[0][0] > 781 or snake_list[0][1] > 481:
            run = False
        elif snake_list[0] in snake_list[1:]:
            run = False

        clock.tick(ticks)
        pg.display.update()
        windows.fill(color)

    if win:
        print('你赢了！')

    exits = int(input('输入任意退出，输1重开：'))
    if exits == 1:
        start_game()
    else:
        pg.quit()
        sys.exit()


start_game()
