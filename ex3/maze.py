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
        cy-= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx +=20
    cx,cy = mx*100+50,my*100+50
    canv.coords("tori",cx,cy)
    root.after(100,main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") 

    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canv,maze_lst)

    tori = tk.PhotoImage(file="fig/5.png") 
    cx, cy = 300, 400
    mx,my=1,1
    canv.create_image(cx, cy, image=tori, tag="tori")


    key = "" # 現在押されているキーを表す

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()