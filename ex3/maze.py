import tkinter as tk
from xml.etree.ElementTree import tostring

if __name__ == "__main__"
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv= tk.Canvas(root,width=1500,heigth=900,bg="black")
    canv.pack()

    tori = tk.PhotoImage(file = "fig/5.png")
    cx,cy = 300, 400
    canv.create_image(cx,cy,inage = tori, tag = "tori")

    key = ""#現在押されているキーを表す

    root.mainloop()