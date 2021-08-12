#文本输入控价、单选按钮、复选框、列表和静态图片控件

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title='wx控件练习',size=(500,500))
        self.Center()
        swindow = wx.SplitterWindow(parent=self,id=-1)      # 创建一个分割窗,parent是frame
        leftpanel = wx.Panel(parent=swindow,style=wx.SUNKEN_BORDER)         #创建左面板
        rightpanel = wx.Panel(parent=swindow,style=wx.SUNKEN_BORDER)        #创建右面板
        # 设置左右布局的分割窗口left和right
        swindow.SplitVertically(leftpanel, rightpanel, 100)
        # 设置最小窗格大小，左右布局指左边窗口大小
        swindow.SetMinimumPaneSize(250)


        textctrl1 = wx.TextCtrl(leftpanel)  #普通文本输入
        textctrl2 = wx.TextCtrl(leftpanel,style=wx.TE_PASSWORD)     #密码输入
        textctrl3 = wx.TextCtrl(leftpanel,style=wx.TE_MULTILINE)    #多行文本输入

        checkbox1 = wx.CheckBox(rightpanel,id=1,label='python')
        checkbox2 = wx.CheckBox(rightpanel,id=2,label='java')
        checkbox3 = wx.CheckBox(rightpanel,id=3,label='c++')
        checkbox1.SetValue(True)    #设置checkbox1初始状态为选中状态

        radiobutton1 = wx.RadioButton(rightpanel,id=4,label='男',style=wx.RB_GROUP)      #设置RB_GROUP的单选按钮，说明是一个组的开始，知道遇到另一个设置rb_group的单选按钮为止都是同一个组。所以radiobutton1和radiobutton2是同一个组，互相排斥
        radiobutton2 = wx.RadioButton(rightpanel,id=5,label='女')

        list1 = ['spring','summer','autumn','winter']
        listbox1 = wx.ListBox(rightpanel,choices=list1,style=wx.LB_SINGLE)
        list2 = ['lemon','apple','cherry','banana']
        listbox2 = wx.ListBox(rightpanel,choices=list2,style=wx.LB_MULTIPLE)

        self.bmps = [wx.Bitmap('/Users/xuebai/Desktop/WechatIMG29260.jpeg',wx.BITMAP_TYPE_JPEG),
                     wx.Bitmap('/Users/xuebai/Desktop/WechatIMG25231.jpeg',wx.BITMAP_TYPE_JPEG),
                     wx.Bitmap('/Users/xuebai/Desktop/WechatIMG25232.jpeg',wx.BITMAP_TYPE_JPEG)]
        self.image = wx.StaticBitmap(leftpanel,bitmap=self.bmps[0])

        self.userid = wx.StaticText(parent=leftpanel,label='用户ID')
        self.password = wx.StaticText(parent=leftpanel,label='密码')
        self.content = wx.StaticText(parent=leftpanel,label='多行文本')
        self.picture = wx.StaticText(parent=leftpanel, label='静态图片显示')
        self.button1 = wx.Button(parent=leftpanel, id=6, label='button1')
        self.button2 = wx.Button(parent=leftpanel, id=7, label='button2')
        self.button3 = wx.Button(parent=leftpanel, id=8, label='button3')

        self.language = wx.StaticText(parent=rightpanel,label='选择你喜欢的编程语言')
        self.gender = wx.StaticText(parent=rightpanel,label="选择性别")
        self.season = wx.StaticText(parent=rightpanel,label='选择你喜欢的季节')
        self.fruit = wx.StaticText(parent=rightpanel,label='选择你喜欢的水果')

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        vbox1.Add(self.userid,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox1.Add(textctrl1,flag=wx.EXPAND|wx.ALL,border=10)
        vbox1.Add(self.password,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox1.Add(textctrl2,flag=wx.EXPAND|wx.ALL,border=10)
        vbox1.Add(self.content,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox1.Add(textctrl3,flag=wx.EXPAND|wx.ALL,border=10)
        vbox1.Add(self.picture,flag=wx.EXPAND|wx.LEFT,border=10)
        vbox1.Add(self.button1,flag=wx.EXPAND)
        vbox1.Add(self.button2,flag=wx.EXPAND)
        vbox1.Add(self.button3,flag=wx.EXPAND)
        vbox1.Add(self.image,flag=wx.EXPAND)


        vbox2 = wx.BoxSizer(wx.VERTICAL)
        vbox2.Add(self.language, flag=wx.EXPAND | wx.RIGHT, border=5)
        vbox2.Add(checkbox1,flag=wx.EXPAND|wx.ALL,border=10)
        vbox2.Add(checkbox2,flag=wx.EXPAND|wx.ALL,border=10)
        vbox2.Add(checkbox3,flag=wx.EXPAND|wx.ALL,border=10)
        vbox2.Add(self.gender, flag=wx.EXPAND | wx.RIGHT, border=5)
        vbox2.Add(radiobutton1,flag=wx.EXPAND|wx.ALL,border=10)
        vbox2.Add(radiobutton2,flag=wx.EXPAND|wx.ALL,border=10)
        vbox2.Add(self.season, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox2.Add(listbox1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox2.Add(self.fruit, flag=wx.EXPAND | wx.LEFT, border=10)
        vbox2.Add(listbox2, flag=wx.EXPAND | wx.ALL, border=10)

        leftpanel.SetSizer(vbox1)
        rightpanel.SetSizer(vbox2)

        self.Bind(wx.EVT_BUTTON,self.on_checkbox_click,id=1,id2=3)    #绑定id1～3的所有控件的事件处理到on_checkbox_click（）方法
        self.Bind(wx.EVT_BUTTON,self.on_radiobutton_click,id=4,id2=5)
        self.Bind(wx.EVT_LISTBOX,self.on_listbox1,listbox1)
        self.Bind(wx.EVT_LISTBOX,self.on_listbox2,listbox2)
        self.Bind(wx.EVT_BUTTON,self.on_click,id=6,id2=8)

    def on_checkbox_click(self,event):
        checkbox = event.GetEventObject()
        print('选择{0},状态{1}'.format(checkbox.GetLabel,checkbox.IsChecked()))

    def on_radiobutton_click(self,event):
        radiobutton = event.GetEventObject()
        print('第一组{0}被选中'.format(radiobutton.GetLabel))

    def on_listbox1(self,event):
        listbox1 = event.GetEventObject()
        print('选择{0}'.format(listbox1.GetSelections()))  #返回多个选中项目的索引序列表

    def on_listbox2(self,event):
        listbox2 = event.GetEventObject()
        print('选择{0}'.format(listbox2.GetSelection()))  #返回单个选中项目的索引序列表

    def on_click(self,event):
        event_id = event.GetId()
        if event_id == 6:
            self.image.SetBitmap(self.bmps[1])  #重新设置图片，实现图片切换
        elif event_id == 7:
            self.image.SetBitmap(self.bmps[2])
        else:
            self.image.SetBitmap(self.bmps[0])
        #self.swindow.Layout()    #重新设置panel布局


app = wx.App()
frm = MyFrame()
frm.Show()
app.MainLoop()