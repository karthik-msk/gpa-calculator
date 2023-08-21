from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.properties import StringProperty
#commment at last
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '900')
#
data = [

[['HS5151','Technical English',4],['MA5158','Engineering Maths - 1',4],['PH5151','Engineering Physics',3],['CY5151','Engineering Chemistry',3],['GE5153','Python Programming',3],['BS5161','Basic Sciences lab',2],['GE5161','Python Lab',2],['','',''],['','',''],21,7],

[['HS5251','Prof Communication',4],['MA5252','Engineering Maths - 2',4],['IT5201','IT Essentials',3],['EE5251','Basics of EEE',3],['GE5151','Engineering Graphics',3],['IT5211','IT Essentials lab',2],['EE5261','BEEE Lab',2],['','',''],['','',''],21,7],

[['MA5302','Discrete Maths',4],['IT5301','Digital Logic & Design',3],['IT5352','Programming & DS',3],['IT5351','DBMS',3],['IT5302','Software Engineering',3],['HUxxxx','Humanities Elective - 1',3],['IT5311','PDS Lab',2],['IT5312','DBMS Lab',2],['','',''],23,8],

[['GE5251','Environmental Sciences',3],['IT5401','OOPs & Advanced DS',3],['IT5402','Design of Algorithms',3],['IT5403','Operating Systems',3],['IT5451','Computer Architecture',3],['HUxxxx','Humanities Elective - 2',3],['IT5411','Operating Systems Lab',2],['IT5412','Advanced DS Lab','2'],['','',''],22,8],

[['IT5502','Compiler Engineering',3],['IT5551','Computer Networks',3],['IT5501','Web Technologies',3],['HUxxxx','Humanities Elective - 1',3],['ITxxxx','Professional Elective-1',3],['IT5511','Computer Networks Lab',2],['IT5512','Web Technologies Lab',2],['IT5513','Internship/Project',2],['','',''],21,8],

[['IT5601','Embedded Systems & IOT',3],['IT5602','Data Science & Analytics',3],['IT5603','Dist&Cloud Computing',3],['ITxxxx','Professional Elective - 2',3],['ITxxxx','Professional Elective - 3',3],['xxxxxx','Open Elective - 1',3],['IT5611','Emb.Systems & IOT Lab',2],['IT5613','Social Relevant Project','1'],['IT5612','Data Analytics&Cloud Comp. Lab',2],23,9],

[['IT5701','Artificial Intelligence',3],['IT5702','Mobile Computing',3],['IT5703','Cryptography & Security',3],['ITxxxx','Professional Elective - 4',3],['ITxxxx','Professional Elective - 5',3],['xxxxxx','Open Elective - 2',3],['IT5711','Mobile & Security Lab',2],['IT5712','Project - 1',2],['','',''],22,8],

[['ITxxxx','Professional Elective - 6',3],['ITxxxx','Professional Elective - 7',3],['IT5811','Project - 2',8],['','',''],['','',''],['','',''],['','',''],['','',''],['','',''],14,3]

]

dims = ['diffimg1.jpeg','diffimg2.jpg','diffimg3.jpg','diffimg4.jpg','diffimg5.jpg']

grd = {"O":10,"A+":9,"A":8,"B+":7,"B":6,"C":5,"U":0}

class MainMenu(Screen):
    pass

class Calculate(Screen):
    res  = StringProperty("")
  
    def selectsem(self,cursem):
        if cursem!='select':
            cs = int(cursem)-1
            self.ids.cd1.text = data[cs][0][0]
            self.ids.cd2.text = data[cs][1][0]
            self.ids.cd3.text = data[cs][2][0]
            self.ids.cd4.text = data[cs][3][0]
            self.ids.cd5.text = data[cs][4][0]
            self.ids.cd6.text = data[cs][5][0]
            self.ids.cd7.text = data[cs][6][0]
            self.ids.cd8.text = data[cs][7][0]
            self.ids.cd9.text = data[cs][8][0]

            self.ids.tit1.text = data[cs][0][1]
            self.ids.tit2.text = data[cs][1][1]
            self.ids.tit3.text = data[cs][2][1]
            self.ids.tit4.text = data[cs][3][1]
            self.ids.tit5.text = data[cs][4][1]
            self.ids.tit6.text = data[cs][5][1]
            self.ids.tit7.text = data[cs][6][1]
            self.ids.tit8.text = data[cs][7][1]
            self.ids.tit9.text = data[cs][8][1]

    def gpa(self,sem):
        if (sem=="select"):
            from kivy.uix.label import Label
            from kivy.uix.popup import Popup
            popup = Popup(title='Error',
                            content=Label(text='Select the semester dude !!!'),
                            size_hint=(None, None), size=(800, 800), title_align = 'center')
            popup.open()
        else:
            cs = int(sem)-1
            tot = data[cs][-2]
            gpalist = [self.ids.grd1.text,
            self.ids.grd2.text,
            self.ids.grd3.text,
            self.ids.grd4.text,
            self.ids.grd5.text,
            self.ids.grd6.text,
            self.ids.grd7.text,
            self.ids.grd8.text,
            self.ids.grd9.text]
            while("" in gpalist):
                gpalist.remove("")
            if (len(gpalist)!=data[cs][-1]):
                if(len(gpalist)<data[cs][-1]):
                    from kivy.uix.label import Label
                    from kivy.uix.popup import Popup
                    popup = Popup(title='Error',
                                content=Label(text='DUDE!!!.. Enter grades for all subjects'),
                                size_hint=(None, None), size=(800, 800), title_align = 'center')
                    popup.open()
                else:
                    from kivy.uix.label import Label
                    from kivy.uix.popup import Popup
                    popup = Popup(title='Error',
                                content=Label(text='Press Reset and re-enter grades'),
                                size_hint=(None, None), size=(800, 800), title_align = 'center')
                    popup.open()
            
            else:
                gpa=0
                for i in range(data[cs][-1]):
                    gpa+=(grd[gpalist[i]]*data[cs][i][2])
                    if gpalist[i]=="U":
                        tot-=data[cs][i][2]
                gpa = round(gpa/tot,2)
                self.res = str(gpa)
    def reset(self):
        self.ids.cd1.text = ''
        self.ids.cd2.text = ''
        self.ids.cd3.text = ''
        self.ids.cd4.text = ''
        self.ids.cd5.text = ''
        self.ids.cd6.text = ''
        self.ids.cd7.text = ''
        self.ids.cd8.text = ''
        self.ids.cd9.text = ''

        self.ids.tit1.text = ''
        self.ids.tit2.text = ''
        self.ids.tit3.text = ''
        self.ids.tit4.text = ''
        self.ids.tit5.text = ''
        self.ids.tit6.text = ''
        self.ids.tit7.text = ''
        self.ids.tit8.text = ''
        self.ids.tit9.text = ''

        self.ids.grd1.text = ''
        self.ids.grd2.text = ''
        self.ids.grd3.text = ''
        self.ids.grd4.text = ''
        self.ids.grd5.text = ''
        self.ids.grd6.text = ''
        self.ids.grd7.text = ''
        self.ids.grd8.text = ''
        self.ids.grd9.text = ''

        self.ids.cursem.text = 'select'
        self.res = ''      
                

class About(Screen):
	pass

class Fun(Screen):
	pass

class Proj(Screen):
    pass


class Diff(Screen):
	
    def instruction(self):
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup
        from kivy.uix.gridlayout import GridLayout
        ins = GridLayout(cols=1)
        ins.add_widget(TextInput(padding_x=30,text="1.) Find all the differences hidden in these two images within 1 minute\n2.) You can get a hint after 30 seconds\n3.) You can view the final answer after 1 minute",halign="center",disabled=True))
        but1 = Button(text='START',size_hint_y=0.3,background_color= (0/255, 255/255, 0/255, 1))
        ins.add_widget(but1)
        popup = Popup(title='Instructions',
                content=ins,
                size_hint=(None, None), size=(800, 1000), title_align = 'center', auto_dismiss = False)
        but1.bind(on_press=popup.dismiss, on_release=self.start)
        popup.open()

    def start(self,x):
        from kivy.clock import Clock
        from random import randint
        num = abs(randint(1,1000)-randint(1,1000))%5
        self.ids.dim1.source = dims[num]
        self.ids.dim2.source = self.ids.dim1.source
        global sec
        sec = 0
        self.c1 = Clock.schedule_once(self.hint,32)
        self.c2 = Clock.schedule_once(self.answer,62)
        self.c3 = Clock.schedule_interval(self.lab,1)
    def hint(self, *args):
        self.ids.hinbut.disabled = False
    def answer(self, *args):
        self.ids.ansbut.disabled = False
    def lab(self, *args):
        self.ids.timer.text = str(int(self.ids.timer.text)+1)
    def showhint(self):
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup
        from kivy.uix.gridlayout import GridLayout
        ins = GridLayout(cols=1)
        ins.add_widget(TextInput(padding_x=30,text="The hint button is a prank !!\nThere's no hint for this\nFind the answer yourself\nor wait 30 seconds to view the answer",halign="center",disabled= True))
        but1 = Button(text='OK',size_hint_y=0.3,size_hint_x=0.5)
        ins.add_widget(but1)
        popup = Popup(title='HINT',
                content=ins,
                size_hint=(None, None), size=(800, 800), title_align = 'center', auto_dismiss = False)
        but1.bind(on_press=popup.dismiss)
        popup.open()

    def showans(self):
        from kivy.uix.textinput import TextInput
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup
        from kivy.uix.gridlayout import GridLayout
        ins = GridLayout(cols=1)
        ins.add_widget(TextInput(padding_x=30,text="Congratulations !!! you have successfully wasted 1 minute of your life. Both of those images are the same and there's no difference in them",halign="center",disabled= True))
        but1 = Button(text='OK',size_hint_y=0.3,size_hint_x=0.5)
        ins.add_widget(but1)
        popup = Popup(title='ANSWER',
                content=ins,
                size_hint=(None, None), size=(800, 800), title_align = 'center', auto_dismiss = False)
        but1.bind(on_press=popup.dismiss, on_release=self.exit)
        popup.open()

    def exit(self, *args):
        self.c1.cancel()
        self.c2.cancel()
        self.c3.cancel()
        self.ids.timer.text = "0"
        self.ids.hinbut.disabled = True
        self.ids.ansbut.disabled = True
        self.ids.dim1.source = ""
        self.ids.dim1.source = ""

class Flames(Screen):

    def flini(self,n1,n2):
        from kivy.uix.button import Button
        from kivy.uix.popup import Popup
        from kivy.uix.image import Image
        from kivy.uix.gridlayout import GridLayout
        from kivy.core.audio import SoundLoader
        sound = SoundLoader.load('srcpar.wav')
        ins = GridLayout(cols=1)
        ins.add_widget(Image(source="parama.png"))
        but1 = Button(text='OK',size_hint_y=0.3,size_hint_x=0.5)
        ins.add_widget(but1)
        popup = Popup(title='PADIDA',
                content=ins,
                size_hint=(None, None), size=(800, 800), title_align = 'center', auto_dismiss = False)
        but1.bind(on_press=popup.dismiss)
        sound.play()
        popup.open()
        self.ids.resf.text = "Olunga Padida"
        

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("design.kv")

class MyMainApp(App):
    def build(self):
        Window.bind(on_keyboard=self.key_input)
        return kv
    def key_input(self, window, key, scancode, codepoint, modifier):
      if key == 27:
         return True  # override the default behaviour
      else:           # the key now does nothing
         return False

if __name__ == "__main__":
    MyMainApp().run()
