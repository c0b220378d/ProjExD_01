import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    bg_img1 = pg.image.load("ex01-20230926/fig/3.png")
    bg_img1 = pg.transform.flip(bg_img1, True, False)
    bg_img2 = pg.transform.rotozoom(bg_img1, 10, 1.0)
    imglist = [bg_img1, bg_img2]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img, [1600-tmr, 0])
        num = tmr%2
        if num == 0:
            screen.blit(imglist[num], [300, 200])
        else:
            screen.blit(imglist[num], [300, 200])
        pg.display.update()
        tmr += 1
        if tmr >= 1599:
            tmr = 0        
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()