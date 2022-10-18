from importlib import machinery
import tkinter as tk
import maze_maker as mm



def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key= ""

def main_proc():
    global mx,my
    global cx,cy
    if key == "Up":
        my-= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] == 0:
        cx,cy = mx*80+50,my*80+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori",cx,cy)

    root.after(100,main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("爆弾迷路") 
    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canv,maze_lst)

    tori = tk.PhotoImage(file="bakudan1.png") 
    cx, cy = 100, 100
    mx,my=1,1
    canv.create_image(cx, cy, image=tori, tag="tori")

    button = tk.Button(root,text="START",font="30",bg="orange")
    #STARTボタンをオレンジ色で設定
    button.place(x=80,y=60)
    #ボタンの位置をx座標80、y座標60にする
    button = tk.Button(root,text="GOAL",font="50",bg="blue")
    #GOALボタンを青で設定
    button.place(x=1040,y=630)
    #ボタンの位置をx座標1040、y座標630にする
    


    key = "" # 現在押されているキーを表す

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()