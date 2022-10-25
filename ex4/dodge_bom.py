from random import randint
import pygame as pg
import sys



key_delta = {pg.K_UP:[0, -1],
            pg.K_DOWN:[0, +1],
            pg.K_LEFT:[-1, 0],
            pg.K_RIGHT:[+1, 0]}

def main():
    #ウインドウ作成・背景貼り付け
    clock = pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")      #ウインドウの名前
    scrn_sfc = pg.display.set_mode((1600, 900))     #画面用surface
    sc_rect = scrn_sfc.get_rect()                   #画面用rect
    bg_sfc= pg.image.load("fig/pg_bg.jpg")          #背景画像用のsurface
    bg_rect = bg_sfc.get_rect()                     #背景画像用のrect
    scrn_sfc.blit(bg_sfc, bg_rect)                  #背景用surfaceを画面用surfaceに張り付ける
   
    
    tori_img = pg.image.load("fig/6.png")            #こうかとんの画像の読み込み
    tori_img = pg.transform.rotozoom(tori_img, 0, 2) #こうかとん画像の拡大
    tori_rect = tori_img.get_rect()                  #こうかとん画像用のrect
    tori_rect.center = 900, 400                      #こうかとんの中心を指定
    scrn_sfc.blit(tori_img, tori_rect)               #こうかとん用surfaceを画面用surfaceに張り付ける
    
    
    bomb = pg.Surface((30, 30))                           #爆弾用のsurface
    bomb.set_colorkey((0, 0, 0))                          #透過処理
    pg.draw.circle(bomb, (255, 0, 0), (10,10), 10)        #爆弾用surfaceに円をかく
    bomb_rect = bomb.get_rect()                           #爆弾用rect
    bomb_rect.centerx = randint(0, sc_rect.width)         #爆弾のx座標をランダムに指定
    bomb_rect.centery = randint(0, sc_rect.height)        #爆弾のy座標をランダムに指定
    scrn_sfc.blit(bomb, bomb_rect)                        #爆弾用のsurfaceを画面用surfaceに張り付ける
    vx, vy = +3, +3                                       #爆弾の速さ"
    
    

    
    while True:
        scrn_sfc.blit(bg_sfc, bg_rect)                     #背景用surfaceを画面用surfaceに貼り付ける

        #爆弾の色をランダムで表示させ続ける
        r = randint(0, 255) 
        g = randint(0, 255) 
        b = randint(0, 255) 
        pg.draw.circle(bomb, (r, g, b), (10, 10), 10)      #爆弾の色の更新,ここで前述したr,g,bを使うことでカラフルな爆弾を作る




        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return                                     #×が押されたらmain関数からreturnする処理

        
        key_states = pg.key.get_pressed()                  #どのキーが押されているか記録した辞書を作成
        for key, delta in key_delta.items(): 
            if key_states[key] == True:                    #キーが押されたら
                tori_rect.centerx += delta[0]              #横方向の変化
                tori_rect.centery += delta[1]              #縦方向の変化
                if check_bound(sc_rect, tori_rect)!=(1,1): #移動後に画面内か
                    tori_rect.centerx -= delta[0] 
                    tori_rect.centery -= delta[1]

        scrn_sfc.blit(tori_img, tori_rect)

        
        #爆弾の移動
        bomb_rect.move_ip(vx, vy)              #爆弾用rectを移動する
        scrn_sfc.blit(bomb, bomb_rect)         #爆弾の画像を貼り付ける
        ret  = check_bound(sc_rect, bomb_rect) #check_bound関数で画面外にいるか判定
        vx *= ret[0]                           #横方向に画面外なら、横方向速度の符号反転
        vy *= ret[1]                           #縦方向に画面外なら、横方向速度の符号反転

        
        if tori_rect.colliderect(bomb_rect):                 #鳥と爆弾が当たったかどうかの判定
            
            #爆発用画像の追加
            hibana_img = pg.image.load("fig/HIBANA1.png")       #火花画像の読み込み
            hibana_img = pg.transform.rotozoom(hibana_img,0,1)  #火花画像の拡大
            hibana_rect = hibana_img.get_rect()                 #火花用rectの作成
            hibana_rect.centerx = tori_rect.centerx + 10        #火花のx座標をこうかとんより右に10ずらす
            hibana_rect.centery = tori_rect.centery + 10        #火花のy座標をこうかとんより上に10ずらす
            scrn_sfc.blit(hibana_img,hibana_rect)               #火花用surfaceを画面用sarfaceに貼り付ける
            baku_img = pg.image.load("fig/bakudan.png")      #爆発画像の読み込み
            baku_img = pg.transform.rotozoom(baku_img, 0, 3) #爆発画像の拡大
            baku_rect = baku_img.get_rect()                  #爆発用rectの作成
            baku_rect.centerx = tori_rect.centerx            #爆発のx座標をこうかとんに合わせる
            baku_rect.centery = tori_rect.centery            #爆発のy座標をこうかとんに合わせる
            scrn_sfc.blit(baku_img, baku_rect)               #爆発用surfaceを画面用surfaceに貼り付ける

            pg.display.update()                              #画面の更新
            pg.time.wait(1000)                               #時間を停止
            return
            
        pg.display.update()                                  #画面の更新
        clock.tick(1000)


def check_bound(sc_r, obj_r):                                #(こうかとん、爆弾)
    #画面内+1 / 画面内-1を返す
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x = -1 
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y = -1
    return x, y

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()