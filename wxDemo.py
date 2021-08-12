import wx

#自定义窗口类MyFrame

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='第一个wx程序',size=(400,300),pos=(100,100))
        #窗口中的控件，在这里添加
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel,label='请单击按钮',pos=(100,10))
        #button1 = wx.Button(parent=panel,label='OK',pos=(100,50))      #事件源
        button1 = wx.Button(parent=panel,id=10,label='button1')
        button2 = wx.Button(parent=panel,id=11,label='button2')

        #创建hbox布局管理器
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(button1,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)
        hbox.Add(button2,proportion=1,flag=wx.EXPAND|wx.ALL,border=10)

        #创建vbox布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.statictext,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL|wx.FIXED_MINSIZE|wx.TOP,border=30)
        #vbox.Add(button,proportion=1,flag=wx.EXPAND|wx.BOTTOM,border=10)
        vbox.Add(hbox,proportion=1,flag=wx.CENTRE)
        #设置panel采用vbox布局
        panel.SetSizer(vbox)

        #self.Bind(wx.EVT_BUTTON, self.on_click, button)  # 事件
        self.Bind(wx.EVT_BUTTON,self.on_click,id=10,id2=20)   #两个按钮的单击事件绑定在on_click方法，参数id是开始按钮的id，参数id2是结束按钮的id

    #事件处理程序
    def on_click(self,event):
        #self.statictext.SetLabelText('Hello World!')
        event_id = event.GetId()        #获取绑定按钮的id
        print(event_id)
        #根据id判断单击了哪个按钮
        if event_id==10:
            self.statictext.SetLabelText("button1单击")
        else:
            self.statictext.SetLabelText("button2单击")


app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()