
import wx
import mazecreator
class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("Colours")
        self.Centre()



    def OnPaint(self, e):
        dc = wx.PaintDC(self)

        xAxis = 0;
        yAxis = 0;

        array = mazecreator.mazecreator(10)

        for i in array:
            minor = i
            for x in minor:
                print(x)
                if x == 1:
                    dc.SetBrush(wx.Brush('#FFFFFF'))
                else:
                    dc.SetBrush(wx.Brush('#000000'))


                dc.DrawRectangle(xAxis, yAxis, 10, 10)
                xAxis += 10
                yAxis += 10





def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()



if __name__ == '__main__':
    main()