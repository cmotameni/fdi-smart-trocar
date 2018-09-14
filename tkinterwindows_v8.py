import Tkinter as tk


#####################################
######## OTHER IMPORTS ##############
import serial #import libraries
#from visual import *
import time
import numpy
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
'''
from drawnow import *
'''
import csv
'''
import plotly as py
'''
import pandas as pd
import graph1_v2
import tkFont
# import tkfont
import InitializeGUI_v8
from InitializeGUI_v8 import deflectionStatus, forceStatus, impedanceStatus




#### Screen width and Height ####
screen_width = 800
screen_height = 480


### Initialize Trocar Application #####

class TrocarApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.tk.call('tk', 'scaling', 133.0/72.0 )
        self.attributes("-fullscreen", False)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (StartPage, ExportPage, AboutPageOne, AboutPageTwo, AboutPageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
       
        frame = self.frames[cont]
        frame.tkraise()



##### START PAGE #######################
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent)     
        canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="#262626", highlightthickness=0)
        canvas.pack()

        ##### TITLE TEXT ####

	color = "#00FF40"

        Title1 = canvas.create_text(screen_width/2,screen_height/3-60-20, fill="white", font=("Helvetica",40), text="FDI", anchor=tk.CENTER)
        Title3 = canvas.create_text(screen_width/2,screen_height/3-20, fill="white", font=("Helvetica",40), text="SMART", anchor=tk.CENTER)
        Title2 = canvas.create_text(screen_width/2,screen_height/3+60-20, fill="white", font=("Helvetica",40), text="TROCAR SYSTEM", anchor=tk.CENTER)
        Title2 = canvas.create_text(10,screen_height-41, fill="white", font=("Helvetica",10), text="BMEn Senior Design 4002W", anchor=tk.W)
        Title2 = canvas.create_text(10,screen_height-20, fill="white", font=("Helvetica",10), text="Group 12", anchor=tk.W)

        ##### INITIALIZE BUTTON #####
        movex = 154
        movey = 191
        triangle = canvas.create_polygon([150+movex,75+movey,150+movex,110+movey,225-40+movex,75+(110-75)/2+movey],  outline=color, fill='#262626', width=2)
        triangle = canvas.create_polygon([150+movex,75+10+movey,150+movex,110-10+movey,225-60+movex,75+(110-75)/2+movey],  outline=color, fill=color, width=2)
        button1 = tk.Button(self, text = "COLLECT", font=("Helvetica",22), command = lambda: [InitializeGUI_v8.start()], bg="#262626", fg=color, highlightthickness=0) # button to initialize the GUI program
        button1.configure(width = 9, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button1_window = canvas.create_window(screen_width/2+30, screen_height/3+124, anchor=tk.CENTER, window=button1)    # creates window on canvas for button
    
        ##### GRAPH BUTTON ######
        movex0 = 154
        movey0 = 250
        triangle = canvas.create_polygon([150+movex0,75+movey0,150+movex0,110+movey0,225-40+movex0,75+(110-75)/2+movey0],  outline='white', fill='#262626', width=2)
        triangle = canvas.create_polygon([150+movex0,75+10+movey0,150+movex0,110-10+movey0,225-60+movex0,75+(110-75)/2+movey0],  outline='white', fill='white', width=2)
        button1 = tk.Button(self, text = "GRAPHS", font=("Helvetica",22), command = lambda: [controller.show_frame(ExportPage)], bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button1.configure(width = 9, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button1_window = canvas.create_window(screen_width/2+30, screen_height/3+124+59, anchor=tk.CENTER, window=button1)    # creates window on canvas for button    

        ##### ABOUT BUTTON #####
        movex2=520
        movey2=220+80
        rectangle = canvas.create_rectangle(150+movex2,150+movey2,170+movex2,170+movey2, outline = 'red', fill = "#262626", width=3)
        rectangle = canvas.create_rectangle(150+movex2,160+movey2,162+movex2,170+movey2, outline = 'red', fill = "red", width=3)
        button2 = tk.Button(self, text = "ABOUT", font=("Helvetica",12), command = lambda: controller.show_frame(AboutPageOne), bg="#262626", fg="red", highlightthickness=0) # button to initialize the GUI program
        button2.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button2_window = canvas.create_window(225+movex2,161+movey2, anchor=tk.CENTER, window=button2)    # creates window on canvas for button


##### DATA COLLECTION PAGE ##### (not used anymore)
'''
class CollectionPage(tk.Frame):

    def __init__(self, parent, controller):
       
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="#262626", highlightthickness=0)
        canvas.pack()
        Placeholder = canvas.create_text(screen_width/2,screen_height/3-20, fill="white", font=("Helvetica",10), text="This is where data will be collected", anchor=tk.CENTER)
        
        ##### FINISH BUTTON #####

        movex3 = 520
        movey3 = -60

        finish = canvas.create_polygon([150+movex3,75+movey3,150+movex3,100+movey3,225-50+movex3,75+(100-75)/2+movey3],  outline='white', fill='#262626', width=2)
        finish = canvas.create_polygon([150+movex3,75+7+movey3,150+movex3,100-7+movey3,225-65+movex3,75+(100-75)/2+movey3],  outline='white', fill='white', width=2)   
        button3 = tk.Button(self, text = "FINISH", font=("Helvetica",12), command = lambda: controller.show_frame(ExportPage), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button

        movex3 = -130
        movey3 = -60

        cancelbutton = canvas.create_rectangle(150-2+movex3,150-73+movey3,170-2+movex3,170-73+movey3,  outline='white', fill='#262626', width=2)
        cancelbutton = canvas.create_rectangle(150+movex3,75+7+movey3,157+movex3,100-7+movey3, outline='white', fill='white', width=2)
            
        button3 = tk.Button(self, text = "CANCEL", font=("Helvetica",12), command = lambda: controller.show_frame(StartPage), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button  
'''

##### EXPORT DATA PAGE (PLOTS COLLECTED DATA) #####

class ExportPage(tk.Frame):



    def __init__(self, parent, controller):

        from InitializeGUI_v8 import deflectionStatus, forceStatus, impedanceStatus
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="#262626", highlightthickness=0)
        canvas.pack()

        c1 = ['#6DDAF8','#40C8F5','#25BEF3','#0CAFF1','#4DA9F6','#5EA7F8','#A1A1FD','#B59FFF','#BE90F8','#C483F2','#CB74EA','#D264E3','#DF46D4','#D954DB','#DF46D4','#ED27C6','#F416BE','#FA09B7','#FC04A8','#FD037B','#FD0266','#FE0253','#FF0003','#FF0003']  
        c2 = ['#04B150','#1CB650','#28B950','#4FC150','#59C350','#72C950','#98D34B','#A6D941','#B2DE38','#CAE827','#F0F90B','#FEFE01','#FFF900','#FFED00','#FFDA00','#FFCE00','#FFC200','#FFC200','#FFB300','#FF9B00','#FF8500','#FF5B00','#FF4000','#FF2B00']
        
        #### Graph plot functions #####

        def defView():
            graph1_v2.graph_deflection()

        def forceView():
            graph1_v2.graph_force()

        def impedanceView():
            graph1_v2.graph_impedance()

        def GraphQuit(canvas):
            graph.quit()    # quits graphing program 
            graph.destroy()
   
        Title = canvas.create_text(screen_width/2+170,screen_height/3-40, fill="white", font=("Helvetica",20), text="PLOT DATA", anchor=tk.CENTER)  
        line = canvas.create_line(450+18,145,650+95,145, arrow=tk.LAST, fill = 'white')
        line = canvas.create_line(650+35,155,650+35,90, arrow=tk.LAST, fill = 'white')

        line = canvas.create_line(650+35,110,650+35+10,110, 650+35+30,130,650+35+40,120,650+35+50,120, fill = c1[1])
        line = canvas.create_line(650+35,130,650+35+10,130, 650+35+30,110,650+35+40,140,650+35+50,140, fill = c2[2])
        line = canvas.create_line(650+35,140,650+35+10,140, 650+35+30,120,650+35+40,110,650+35+50,110, fill = 'magenta')
        


        movexa = 154
        moveya = 75
        c = 115
        a = 85

             
        button1 = tk.Button(self, text = "Deflection Data", font=("Helvetica",13), command = lambda: [defView()], bg="#262626", fg=c1[1], highlightthickness=0) # button to initialize the GUI program
        button1.configure(width = 11, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button1_window = canvas.create_window(screen_width/2+30+a, screen_height/3+150-c, anchor=tk.W, window=button1)    # creates window on canvas for button

        if deflectionStatus !=0:
            successIcon = canvas.create_oval(690,190,700,200, fill = 'green')
        if forceStatus !=0:
            successIcon = canvas.create_oval(690-40,265,700-40,275, fill = 'green')
        if impedanceStatus !=0:
            successIcon = canvas.create_oval(690+15,340,700+15,350, fill = 'green')

        ### failure icons ###

        if deflectionStatus == 0:
            failIcon = canvas.create_text(700,193, text = "( ! )", font = ("Helvetica",13), fill = 'red', anchor = tk.W)
            failText = canvas.create_text(20,screen_height-20, text = "( ! ) : Data has failed to export", font = ("Helvetica",8), fill = 'red', anchor = tk.W)
        if forceStatus == 0:
            failIcon = canvas.create_text(655,270, text = "( ! )", font = ("Helvetica",13), fill = 'red', anchor = tk.W)
            failText = canvas.create_text(20,screen_height-20, text = "( ! ) : Data has failed to export", font = ("Helvetica",8), fill = 'red', anchor = tk.W)
        if impedanceStatus == 0:
            failIcon = canvas.create_text(710,345, text = "( ! )", font = ("Helvetica",13), fill = 'red', anchor = tk.W)
            failText = canvas.create_text(20,screen_height-20, text = "( ! ) : Data has failed to export", font = ("Helvetica",8), fill = 'red', anchor = tk.W)
        
        movexb = 370
        moveyb = 100

        
        line = canvas.create_line(100+movexb,100+moveyb,130+movexb,100+moveyb, arrow=tk.LAST, fill = 'white', dash=(3,5))
        line = canvas.create_line(100+movexb,100+moveyb,120+movexb,80+moveyb, arrow=tk.LAST, fill = c1[1])
       
        movexf = 375
        moveyf = 155
        
        line = canvas.create_line(100+movexf,100+moveyf,100+movexf,120+moveyf, arrow=tk.LAST, fill = c2[8])
        line = canvas.create_line(120+movexf,100+moveyf,120+movexf,120+moveyf, arrow=tk.LAST, fill = c2[8])
        line = canvas.create_line(110+movexf,100+moveyf,110+movexf,135+moveyf, arrow=tk.LAST, fill = c2[1])

        button1 = tk.Button(self, text = "Force Data", font=("Helvetica",13), command = lambda: [forceView()], bg="#262626", fg=c2[1], highlightthickness=0) # button to initialize the GUI program
        button1.configure(width = 8, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button1_window = canvas.create_window(screen_width/2+30+a, screen_height/3+150+75-c, anchor=tk.W, window=button1)    # creates window on canvas for button

        movexc = 375
        moveyc = 240

        line = canvas.create_line(100+movexc,100+moveyc,100+movexc,120+moveyc, arrow=tk.LAST, fill = c1[20])
        line = canvas.create_line(120+movexc,100+moveyc,120+movexc,120+moveyc, arrow=tk.LAST, fill = c1[20])
        line = canvas.create_line(110+movexc,100+moveyc,110+movexc,120+moveyc, arrow=tk.LAST, fill = 'magenta')

        line = canvas.create_line(110+movexc,100+moveyc,120+movexc,90+moveyc,  fill = 'magenta')
        line = canvas.create_line(110+movexc,100+moveyc,100+movexc,90+moveyc,  fill = 'magenta')

        button1 = tk.Button(self, text = "Impedance Data", font=("Helvetica",13), command = lambda: [impedanceView()], bg="#262626", fg='magenta', highlightthickness=0) # button to initialize the GUI program
        button1.configure(width = 12, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button1_window = canvas.create_window(screen_width/2+30+a, screen_height/3+150+150-c, anchor=tk.W, window=button1)    # creates window on canvas for button


        movex3 = -130
        movey3 = -60
        cancelbutton = canvas.create_rectangle(150-2+movex3,150-73+movey3,170-2+movex3,170-73+movey3,  outline='white', fill='#262626', width=2)
        cancelbutton = canvas.create_rectangle(150+movex3,75+7+movey3,157+movex3,100-7+movey3, outline='white', fill='white', width=2)     
        button3 = tk.Button(self, text = "BACK", font=("Helvetica",12), command = lambda: controller.show_frame(StartPage), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button



##### ABOUT PAGES ##############

class AboutPageOne(tk.Frame):

    def __init__(self, parent, controller):

        movex3 = -130
        movey3 = -60

        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="#262626", highlightthickness=0)
        canvas.pack()
          
        #Placeholder = canvas.create_text(screen_width/2,screen_height/3-20, fill="white", font=("Helvetica",10), text="This will be the ABOUT Page (1)", anchor=tk.CENTER)

        cancelbutton = canvas.create_rectangle(150-2+movex3,150-73+movey3,170-2+movex3,170-73+movey3,  outline='white', fill='#262626', width=2)
        cancelbutton = canvas.create_rectangle(150+movex3,75+7+movey3,157+movex3,100-7+movey3, outline='white', fill='white', width=2)     
        button3 = tk.Button(self, text = "BACK", font=("Helvetica",12), command = lambda: controller.show_frame(StartPage), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button

        movex3 = 520
        movey3 = -60

        initializebutton = canvas.create_polygon([150+movex3,75+movey3,150+movex3,100+movey3,225-50+movex3,75+(100-75)/2+movey3],  outline='white', fill='#262626', width=2)
        initializebutton = canvas.create_polygon([150+movex3,75+7+movey3,150+movex3,100-7+movey3,225-65+movex3,75+(100-75)/2+movey3],  outline='white', fill='white', width=2)
        button3 = tk.Button(self, text = "NEXT", font=("Helvetica",12), command = lambda: controller.show_frame(AboutPageTwo), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button

        xs = 200
        ys = 5
        xcoord1 =50
        xcoord2 = 300
        xcoord3 = 550
        ycoord = 450

        c1 = ['#6DDAF8','#40C8F5','#25BEF3','#0CAFF1','#4DA9F6','#5EA7F8','#A1A1FD','#B59FFF','#BE90F8','#C483F2','#CB74EA','#D264E3','#DF46D4','#D954DB','#DF46D4','#ED27C6','#F416BE','#FA09B7','#FC04A8','#FD037B','#FD0266','#FE0253','#FF0003','#FF0003']  
        c2 = ['#04B150','#1CB650','#28B950','#4FC150','#59C350','#72C950','#98D34B','#A6D941','#B2DE38','#CAE827','#F0F90B','#FEFE01','#FFF900','#FFED00','#FFDA00','#FFCE00','#FFC200','#FFC200','#FFB300','#FF9B00','#FF8500','#FF5B00','#FF4000','#FF2B00']

        y_values = numpy.zeros(15)

        for i in range(15):
            y_values[i] = screen_height-30-(10*i)

        for x1, y1 in zip(y_values, c1):
            x = xcoord1
            x1 = int(x1)-20 
            x2 = x + xs
            y2 = x1 - ys
            canvas.create_rectangle(x,x1,x2,y2, fill=str(y1), width=0, outline="#262626")


        deflectionValueText = canvas.create_text(xcoord1+100,screen_height-230, fill=c1[15], font=("Helvetica",28), text="3.2 dev", anchor=tk.CENTER)
        deflectionValueText = canvas.create_text(xcoord1+100,screen_height-25, fill=c1[1], font=("Helvetica",14), text="DEFLECTION", anchor=tk.CENTER)

        ### about paragraph ###
        paragraph = canvas.create_text(screen_width/2-130, 120, fill='white', font=("Helvetica",16), text = "Tilting the trocar away from its\nstarting axis will cause an\nincrease in deflection", anchor=tk.W)
        


class AboutPageTwo(tk.Frame):

    def __init__(self, parent, controller):

        movex3 = -130
        movey3 = -60

        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="#262626", highlightthickness=0)
        canvas.pack()
         
        #Placeholder = canvas.create_text(screen_width/2,screen_height/3-20, fill="cyan", font=("Helvetica",10), text="This will be the ABOUT Page (2)", anchor=tk.CENTER)

        cancelbutton = canvas.create_rectangle(150-2+movex3,150-73+movey3,170-2+movex3,170-73+movey3,  outline='white', fill='#262626', width=2)
        cancelbutton = canvas.create_rectangle(150+movex3,75+7+movey3,157+movex3,100-7+movey3, outline='white', fill='white', width=2)
        button3 = tk.Button(self, text = "BACK", font=("Helvetica",12), command = lambda: controller.show_frame(AboutPageOne), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button

        movex3 = 520
        movey3 = -60
        initializebutton = canvas.create_polygon([150+movex3,75+movey3,150+movex3,100+movey3,225-50+movex3,75+(100-75)/2+movey3],  outline='white', fill='#262626', width=2)
        initializebutton = canvas.create_polygon([150+movex3,75+7+movey3,150+movex3,100-7+movey3,225-65+movex3,75+(100-75)/2+movey3],  outline='white', fill='white', width=2)
        button3 = tk.Button(self, text = "NEXT", font=("Helvetica",12), command = lambda: controller.show_frame(AboutPageThree), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button

        xs = 200
        ys = 5
        xcoord1 =50
        xcoord2 = 300
        xcoord3 = 550
        ycoord = 450

        c1 = ['#6DDAF8','#40C8F5','#25BEF3','#0CAFF1','#4DA9F6','#5EA7F8','#A1A1FD','#B59FFF','#BE90F8','#C483F2','#CB74EA','#D264E3','#DF46D4','#D954DB','#DF46D4','#ED27C6','#F416BE','#FA09B7','#FC04A8','#FD037B','#FD0266','#FE0253','#FF0003','#FF0003']  
        c2 = ['#04B150','#1CB650','#28B950','#4FC150','#59C350','#72C950','#98D34B','#A6D941','#B2DE38','#CAE827','#F0F90B','#FEFE01','#FFF900','#FFED00','#FFDA00','#FFCE00','#FFC200','#FFC200','#FFB300','#FF9B00','#FF8500','#FF5B00','#FF4000','#FF2B00']

        y_values = numpy.zeros(20)
        
        for i in range(20):
            y_values[i] = screen_height-30-(10*i)

        for x1, y1 in zip(y_values, c2):
            x = xcoord1
            x1 = int(x1)-20 
            x2 = x + xs
            y2 = x1 - ys
            canvas.create_rectangle(x,x1,x2,y2, fill=str(y1), width=0, outline="#262626")


        deflectionValueText = canvas.create_text(xcoord1+100,screen_height-280, fill=c2[20], font=("Helvetica",28), text="28 lbs", anchor=tk.CENTER)
        deflectionValueText = canvas.create_text(xcoord1+100,screen_height-25, fill=c2[1], font=("Helvetica",14), text="FORCE", anchor=tk.CENTER)

        ### about paragraph ###

        paragraph = canvas.create_text(screen_width/2-130, 120, fill='white', font=("Helvetica",16), text = "Force applied to the trocar is \nmeasured and displayed with the \nFORCE bar in \nreal time.", anchor=tk.W)


class AboutPageThree(tk.Frame):

    def __init__(self, parent, controller):

        movex3 = -130
        movey3 = -60

        tk.Frame.__init__(self, parent)

        
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10


        canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg="#262626", highlightthickness=0)
        canvas.pack()
       
        Placeholder = canvas.create_text(screen_width/2,screen_height/3-20, fill="magenta", font=("Helvetica",10), text="This will be the ABOUT Page (3)", anchor=tk.CENTER)

        cancelbutton = canvas.create_rectangle(150-2+movex3,150-73+movey3,170-2+movex3,170-73+movey3,  outline='white', fill='#262626', width=2)
        cancelbutton = canvas.create_rectangle(150+movex3,75+7+movey3,157+movex3,100-7+movey3, outline='white', fill='white', width=2)
        button3 = tk.Button(self, text = "BACK", font=("Helvetica",12), command = lambda: controller.show_frame(AboutPageTwo), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button

        movex3 = 520
        movey3 = -60
        initializebutton = canvas.create_polygon([150+movex3,75+movey3,150+movex3,100+movey3,225-50+movex3,75+(100-75)/2+movey3],  outline='white', fill='#262626', width=2)
        initializebutton = canvas.create_polygon([150+movex3,75+7+movey3,150+movex3,100-7+movey3,225-65+movex3,75+(100-75)/2+movey3],  outline='white', fill='white', width=2)
        button3 = tk.Button(self, text = "DONE", font=("Helvetica",12), command = lambda: controller.show_frame(StartPage), bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
        button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = tk.FLAT)  # button click visuals 
        button3_window = canvas.create_window(225+movex3,88+movey3, anchor=tk.CENTER, window=button3)    # creates window on canvas for button

        # load the .gif image file
        # put in your own gif file here, may need to add full path
        # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
        

     
     
     
    
app = TrocarApp()
app.mainloop()
