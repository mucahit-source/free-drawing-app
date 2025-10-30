from turtle import *

s = Screen()
s.setup(700,700)
renkler = ['blue', 'green', 'red', 'brown', 'purple', 'black']
pensize(4)
penup()
aktif_renk = 0


def cizim(x, y):
    pendown()
    goto(x, y)

def renk_degistir(x, y):
    global aktif_renk
    aktif_renk = (aktif_renk + 1) % len(renkler)
    color(renkler[aktif_renk])
    print("Renk değişti →", renkler[aktif_renk])

def temizlik(x, y):
    reset()
    pensize(4)
    penup()
    color(renkler[0])

s.onscreenclick(cizim, 1)   # Sol tık: çizim
s.onscreenclick(renk_degistir, 3)  # Sağ tık: renk değiştir
s.onscreenclick(temizlik, 2)  # Orta tık: temizle
s.mainloop()
