import csv
import wx
import mazecreator
import Tkinter
class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("MazeCraze")
        self.Centre()





    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        wx.P
        top = Tkinter.Tk()
        import csv

        with open('C:/Users/gusta/OneDrive/Documents/Plenissalen/mazeCraze/maze.csv') as f:
            reader = csv.reader(f)
            your_list = list(reader)

        rowCounter = 0
        xAxis = 0;
        yAxis = 0;
        size = 33;
        array = your_list

            #mazecreator.mazecreator(size)

        for i in array:
            minor = i
            for x in minor:
                print(x)
                if x == '1':
                    dc.SetBrush(wx.Brush('#FFFFFF'))
                else:
                    dc.SetBrush(wx.Brush('#000000'))


                if rowCounter == size:
                    yAxis += 10
                    rowCounter = 0
                    xAxis=0
                dc.DrawRectangle(xAxis, yAxis, 10, 10)
                xAxis += 10
                rowCounter += 1
                button = wx.Button(self, -1)






def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()




if __name__ == '__main__':
    main()