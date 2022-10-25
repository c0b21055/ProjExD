import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc =  pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_sfc = bg_sfc.get_rect()

    clock = pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc,bg_sfc)
        pg.display.update()
        

        for event in pg.event.get():
            if event.type == pg.Quit:
                return

        clock.time(0.2)



    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()