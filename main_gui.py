import wx
import re
import spell_checker
import auto_complete
import grammar_validator

root = auto_complete.Node('',0)
Path_to_dict = "english_words.txt"
auto_complete.fileparse(Path_to_dict,root)
        

class ExampleFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.panel = wx.Panel(self)     
        self.quote = wx.StaticText(self.panel, label="Did you mean:")
        self.result = wx.StaticText(self.panel, label="")
        self.result.SetForegroundColour(wx.RED)
        self.button = wx.Button(self.panel, label="Predict word")
        self.lblname = wx.StaticText(self.panel, label="Type word:")
        self.editname = wx.TextCtrl(self.panel, size=(140, -1))

        self.button1 = wx.Button(self.panel, label="Auto-Complete")
        self.lblname1 = wx.StaticText(self.panel, label="Type word:")
        self.editname1 = wx.TextCtrl(self.panel, size=(140, -1))

        self.button2 = wx.Button(self.panel, label="Check Spelling")
        self.lblname2 = wx.StaticText(self.panel, label="Type word:")
        self.result2 = wx.StaticText(self.panel, label="")
        self.editname2 = wx.TextCtrl(self.panel, size=(140, -1))
        self.result2.SetForegroundColour(wx.RED)


        self.button3 = wx.Button(self.panel, label="Validate Grammar")
        self.lblname3 = wx.StaticText(self.panel, label="Type sentence:")
        self.editname3 = wx.TextCtrl(self.panel, size=(340, -1))
        self.lblname4 = wx.StaticText(self.panel, label="Chart Parser:")
        self.parse_chart1 = wx.StaticText(self.panel, label="")
        self.parse_chart2 = wx.StaticText(self.panel, label="")
        self.parse_chart3 = wx.StaticText(self.panel, label="")
        self.parse_chart4 = wx.StaticText(self.panel, label="")
        self.parse_chart5 = wx.StaticText(self.panel, label="")
        self.parse_chart6 = wx.StaticText(self.panel, label="")
        self.parse_chart7 = wx.StaticText(self.panel, label="")
        self.parse_chart8 = wx.StaticText(self.panel, label="")
        
        self.result4 = wx.StaticText(self.panel, label="")
        self.result4.SetForegroundColour(wx.RED)

        
        # Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)        

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(30, 20)
        
        #predict_word
        self.sizer.Add(self.quote, (0, 0))
        self.sizer.Add(self.result, (0, 1))
        self.sizer.Add(self.lblname, (1, 0))
        self.sizer.Add(self.editname, (1, 1))
        self.sizer.Add(self.button, (2, 0), (1, 2))

        #auto_complete
        self.sizer.Add(self.lblname1, (4, 0))
        self.sizer.Add(self.editname1, (4, 1))
        self.sizer.Add(self.button1, (5, 0), (1, 2))
        self.cb = wx.ComboBox(self.panel,size=wx.DefaultSize)
        self.sizer.Add(self.cb,(6,0))
        
        #spell_checker
        self.sizer.Add(self.lblname2, (8, 0))
        self.sizer.Add(self.editname2, (8, 1))
        self.sizer.Add(self.button2, (9, 0), (1, 2))
        self.sizer.Add(self.result2, (10, 0))
        
        #validate_grammar
        self.sizer.Add(self.result4, (1, 5))
        self.sizer.Add(self.lblname3, (2, 5))
        self.sizer.Add(self.editname3, (2, 6))
        self.sizer.Add(self.button3, (3, 5), (1, 2))
        self.sizer.Add(self.lblname4,(4,5))
        self.sizer.Add(self.parse_chart1,(5,5))
        self.sizer.Add(self.parse_chart2,(6,5))
        self.sizer.Add(self.parse_chart3,(7,5))
        self.sizer.Add(self.parse_chart4,(8,5))
        self.sizer.Add(self.parse_chart5,(9,5))
        self.sizer.Add(self.parse_chart6,(10,5))
        self.sizer.Add(self.parse_chart7,(11,5))
        self.sizer.Add(self.parse_chart8,(12,5))

         
       
        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)  
        self.SetSizerAndFit(self.windowSizer)  

        # Set event handlers
        self.button.Bind(wx.EVT_BUTTON, self.predict)
        self.button1.Bind(wx.EVT_BUTTON, self.auto_complete)
        self.button2.Bind(wx.EVT_BUTTON, self.check_spelling)
        self.button3.Bind(wx.EVT_BUTTON, self.validate)

    def validate(self,e):
        chart=[]
        p=self.editname3.GetValue()
        p=len(p.split(' '))
        res=grammar_validator.validate(self.editname3.GetValue(),chart)
        self.result4.SetLabel(res)
        s=' '.join([("%s" % i) for i in chart])
        count = 0
        store = []
        temp=s.split(' ')
        h=''
        for w in temp:
            print(w)
            count = count + 1
            h=h+w+'              ';
            diff=3-len(w)
            for k in range(0,diff+1):
                h=h+' '
            if (count == p+1):
                count=0
                store.append(h)
                print(h)
                h=''
        p=p+1
        if(p>=8):
            self.parse_chart8.SetLabel(store[7])
        if(p>=7):
            self.parse_chart7.SetLabel(store[6])
        if(p>=6):
            self.parse_chart6.SetLabel(store[5])
        if(p>=5):
            self.parse_chart5.SetLabel(store[4])
        if(p>=4):
            self.parse_chart4.SetLabel(store[3])
        if(p>=3):
            self.parse_chart3.SetLabel(store[2])
        if(p>=2):
            self.parse_chart2.SetLabel(store[1])
        if(p>=1):
            self.parse_chart1.SetLabel(store[0])
        
        self.sizer.Layout()
        
        
    def check_spelling(self,e):
        result=[]
        root.search(self.editname2.GetValue(),'',result)
        if(len(result)==0):
            self.result2.SetLabel("Incorrect")
        else:
            self.result2.SetLabel("Correct")

    def predict(self, e):
        s=spell_checker.correct(self.editname.GetValue())
        self.result.SetLabel(s)

    def auto_complete(self, e):
        result = []
        root.search(self.editname1.GetValue(),'',result) 
        self.cb.SetItems(result)

app = wx.App(False)
frame = ExampleFrame(None)
frame.Show()
app.MainLoop()