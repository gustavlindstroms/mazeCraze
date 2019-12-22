import csv
import wx
import tkinter
import mazecreator
from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        with open('C:/Users/gusta/OneDrive/Documents/Plenissalen/mazeCraze/maze.csv') as f:
            reader = csv.reader(f)
            your_list = list(reader)

        rowCounter = 0
        xAxis = 0;
        yAxis = 0;
        size = 33;
        array = your_list

        for i in array:
            minor = i
            for x in minor:
                print(x)
                color = ''
                if x == '1':
                    color = '#000'
                else:
                    color = '#fff'

                if rowCounter == size:
                    yAxis += 10
                    rowCounter = 0
                    xAxis=0
                canvas.create_rectangle(xAxis, yAxis, xAxis+10, yAxis+10, outline=color, fill=color, width=2)

                print('printed one with color ' + color)
                color = ''
                xAxis += 10
                rowCounter += 1

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("330x220+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()


