from Tkinter import *
from ListImage import *
from PIL import ImageTk
from sys import argv
import Image


class Appli(Tk):
    def __init__(self, master=None, title="Undefined"):
        Tk.__init__(self, master)
        self.title(title)
        
        self.minsize(520, 480)
        
        self.hadOneJob = ListImage(len(argv) > 1) #Yes, I'm very lazy
        
        self.initialize()
        
    def initialize(self):
        button = Button(self, text="Next", command=self.onPush)
        button.pack()
        
        tmp = Image.open(self.hadOneJob.getRandomImg())
        self.img = ImageTk.PhotoImage(self._resize(tmp))
        
        self.canvas = Canvas(self)
        
        self.canvas.create_image(240, 0, image=self.img, anchor=N)
        self.canvas.pack(fill=BOTH, expand=True)

        
    def onPush(self):
        tmp = Image.open(self.hadOneJob.getRandomImg())
        self.img = ImageTk.PhotoImage(self._resize(tmp))
        
        self.canvas.create_image(240, 0, image=self.img, anchor=N)
    
    def _resize(self, img):
        W, H = img.size
        print W, H
        if W > H:
            H = int(H*(480./W))
            W = 480
            print W, H
            return img.resize((W, H))
        else:
            W = int(W*(480./H))
            H = 480
            print W, H
            return img.resize((W, H))

if __name__ == "__main__":
    a = Appli(title="Hello")
    a.mainloop()
