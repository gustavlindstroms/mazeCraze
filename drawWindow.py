import csv
from tkinter import Tk, Canvas, Frame, BOTH, Button
arr = []

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("MazeCraze")
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
                if x == '1':
                    color = 'gray15'
                elif x == '3':
                    color = 'red'
                else:
                    color = 'white'
                if rowCounter == size:
                    yAxis += 10
                    rowCounter = 0
                    xAxis=0
                rectangle = canvas.create_rectangle(xAxis, yAxis, xAxis+10, yAxis+10, outline=color, fill=color, width=2)
                arr.append(rectangle)
                xAxis += 10
                rowCounter += 1

        canvas.pack(fill=BOTH, expand=1)
        button = Button(self, text='Solve', command=printHello)
        button.pack(fill=BOTH, expand=1)

def printHello():
    print('Hello')

def main():
    root = Tk()
    ex = Example()
    root.geometry("330x220+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()