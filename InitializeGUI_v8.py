############ IMPORTS ################

import serial #import libraries
from visual import *
from Tkinter import *
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


try: 
    deflectionStatus = []
    forceStatus = []
    impedanceStatus = []
except collect:
    pass

def start():

    def collect():
        collect = 1
        arduinoData.close()

        sample_rate = 10 # [samples/s]

        start = 0

        numDeflection = len(deflection_filtered)
        numForce = len(y_list)
        numImpedance = len(z_list)

        stopDeflection = numDeflection/sample_rate
        stopForce = numForce/sample_rate
        stopImpedance = numImpedance/sample_rate


        time_listDeflection = numpy.linspace(start,stopDeflection,num = numDeflection, endpoint = True)
        time_listForce = numpy.linspace(start,stopForce,num = numForce, endpoint = True)
        time_listImpedance = numpy.linspace(start,stopImpedance,num = numImpedance, endpoint = True)

        try:
            dx = pd.DataFrame({"time": time_listDeflection,"def": x_list})
            dx.to_csv("deflection.csv", index=False)
            print "successfully exported Deflection data"
            deflectionStatus = 1

        except:
            print "failed to export deflection data"
            deflectionStatus = 0
        try:
            dy = pd.DataFrame({"time": time_listForce,"force": y_list})
            dy.to_csv("force.csv", index=False)
            print "successfully exported force data"
            forceStatus = 1
        except: 
            print "failed to export force data"
            forceStatus = 0
        try:
            dz = pd.DataFrame({"time": time_listImpedance,"imp": z_list})
            dz.to_csv("impedance.csv", index=False)
            print "successfully exported impedance data"
            impedanceStatus = 1
        except:
            print "failed to export impedance data"
            impedanceStatus = 0

        
        root.destroy()
    
    root = Tk()
    root.attributes("-fullscreen", False) 
    root.tk.call('tk', 'scaling', 133.0/72.0 )

    screen_width = 800 
    color = "#00FF40"
    screen_height = 460

    button3 = Button(root, text = "FINISH COLLECTION", font=("Helvetica",13), command = collect, bg="#262626", fg="white", highlightthickness=0) # button to initialize the GUI program
    button3.configure(width = 6, activebackground = "#262626", activeforeground = "white", relief = FLAT)  # button click visuals 
    button3.pack(side = TOP,expand = 1, fill  = BOTH, anchor = E)


    canvas = Canvas(root, width=screen_width, height=screen_height, bg="#262626", highlightthickness=0) # Creates and packs canvas
    canvas.pack(side = BOTTOM)

    y_values = numpy.zeros(24)

    for i in range(24):
        
        y_values[i] = screen_height-30-(10*i)
        

    c1 = ['#6DDAF8','#40C8F5','#25BEF3','#0CAFF1','#4DA9F6','#5EA7F8','#A1A1FD','#B59FFF','#BE90F8','#C483F2','#CB74EA','#D264E3','#DF46D4','#D954DB','#DF46D4','#ED27C6','#F416BE','#FA09B7','#FC04A8','#FD037B','#FD0266','#FE0253','#FF0003','#FF0003']  
    c2 = ['#04B150','#1CB650','#28B950','#4FC150','#59C350','#72C950','#98D34B','#A6D941','#B2DE38','#CAE827','#F0F90B','#FEFE01','#FFF900','#FFED00','#FFDA00','#FFCE00','#FFC200','#FFC200','#FFB300','#FF9B00','#FF8500','#FF5B00','#FF4000','#FF2B00']

    xs = 200
    ys = 5
    xcoord1 =50
    xcoord2 = 300
    xcoord3 = 550
    ycoord = 450

    c_list = []
    x_list = []
    y_list = []
    z_list = []

    deflection_raw = []
    deflection_filtered = []



    deflection = 0
    deflectionRound = 0
    force = 0
    impedance = 0
    cnt = 0

    baudrate = 115200

    try: 
        arduinoData = serial.Serial('com4', baudrate) # COM3 Port Option
        print "connected to serial port"
            #canvas.create_text(screen_width-5,15, fill="green", font=("Helvetica",8), text="Connected to Serial Port! [COM3]", anchor=E)
    except:
        try:  
            arduinoData = serial.Serial('/dev/ttyACM0', baudrate) # TTYACM0 Option
            print "connected to serial port"
                #canvas.create_text(screen_width-5,15, fill="green", font=("Helvetica",8), text="Connected to Serial Port! [ttyACM0]", anchor=E)
        except:
            try:  
                arduinoData = serial.Serial('/dev/ttyACM1', baudrate) # TTYACM1 Option
                print "connected to serial port"
                    #canvas.create_text(screen_width-5,15, fill="green", font=("Helvetica",8), text="Connected to Serial Port! [ttyACM1]", anchor=E)
            except:
                print "failed to connect to serial port" # Failure Screen
                    #serialFailureText=canvas.create_text(screen_width-5,15, fill="red", font=("Helvetica",8), text="Failed to connect to serial port!", anchor=E)
    
    arduinoData.write('1')

    movex3 = 520
    movey3 = -60

    '''
    #initializing/defining
    deflection_raw = [0,0,0,0,0] #list of raw values
    deflection_filtered = [0,0,0,0,0] #list of filtered values
     
    #Below should be in a loop and accepts the new value for (force, deflection, or impedance) each iteration
    #deflection=        # deflection is whatever new measurement is this sampling

    deflection_raw.append(deflection) 
    CountSG=len(deflection_raw) 
   
    deflection_new = 0.5381*deflection_raw[CountSG-0] +0.38095*deflection_raw[CountSG-1] \
                           +0.2381*deflection_raw[CountSG-2] +0.09524*deflection_raw[CountSG-3] \
                           -0.04762*deflection_raw[CountSG-4] -0.19048*deflection_raw[CountSG-5]
    #deflection_new is  now the corresponding filtered value of deflection
    deflection_filtered.append(deflection_new) 

    #At the moment the filter is good because the coefficients are independent of the measurement we are taking
    #deflection_raw, deflection_filtered, deflection, OutputNew need to be renamed if used for many measurement types i.e. deflection_rawF for force and deflection_rawD for deflection, etc. 


    '''

  

    while True:

        while (arduinoData.inWaiting()==0): #if there's no data, do nothing
             pass
        arduinoString = arduinoData.readline()
        dataArray = arduinoString.split(',') #splits data 
        
        # try:
        #      print float(dataArray[0]),float(dataArray[1]),float(dataArray[2]) # time , deflection , force , impedance
        # except:
        #     pass
        
        for x1, y1 in zip(y_values, c1):
            x = xcoord1
            x1 = int(x1) -20 #ADDED MINUS 20
            x2 = x + xs
            y2 = x1 - ys
            canvas.create_rectangle(x,x1,x2,y2, fill=str(y1), width=0, outline="#262626")

        deflectionHeader = canvas.create_text(xcoord1+100,screen_height-30, fill=c1[1], font=("Helvetica",14), text="DEFLECTION", anchor=CENTER)

        for x1, y1 in zip(y_values, c2):
            x = xcoord2
            x1 = int(x1) -20
            x2 = x + xs
            y2 = x1 - ys
            canvas.create_rectangle(x,x1,x2,y2, fill=str(y1), width=0, outline="#262626")

        forceHeader = canvas.create_text(xcoord2+100,screen_height-30, fill=c2[1], font=("Helvetica",14), text="FORCE", anchor=CENTER)


        # for x1, y1 in zip(y_values, c1):
        #     x = xcoord3
        #     x1 = int(x1) -20
        #     x2 = x + xs
        #     y2 = x1 - ys
        #     canvas.create_rectangle(x,x1,x2,y2, fill=str(y1), width=0, outline="#262626")

        impHeader = canvas.create_text(xcoord3+100,screen_height-30, fill='red', font=("Helvetica",14), text="IMPEDANCE", anchor=CENTER)

        degree_sign= u'\N{DEGREE SIGN}'

            # converts strings from SerialRead to floating data points
        try:

            try: 
                deflection = float(dataArray[0])
                deflection_raw.append(deflection)
                CountSG = int(len(deflection_raw))-1
                deflection_new = 0.5381*deflection_raw[CountSG] +0.38095*deflection_raw[CountSG-1] +0.2381*deflection_raw[CountSG-2] +0.09524*deflection_raw[CountSG-3] -0.04762*deflection_raw[CountSG-4] -0.19048*deflection_raw[CountSG-5]
                deflection_filtered.append(deflection_new)

                print deflection, deflection_new
                

            except: 
                deflection_new = float(dataArray[0]) 
                

            try: 
                force = round(float(dataArray[1]))
		forceg = float(dataArray[1])
            except:
                force = force

            try: 
                impedance = float(dataArray[2])
                #impedanceBar = canvas.create_rectangle(xcoord3, screen_height-30-(15*24)-20, xcoord3+200, screen_height-30-(impedance*15), fill="#262626", width=0)
                #impedanceValueText = canvas.create_text(xcoord3+100,screen_height-85-(impedance*15), fill="cyan", font=("Helvetica",15), text=(str(impedance), "kO"), anchor=CENTER)

            except:
                impedance = impedance
            

            level1 = 0
            level2 = 3
            level3 = 6


            if impedance < level1:

                canvas.create_rectangle(xcoord3, 250, xcoord3 + 200, 190, fill = color, width = 0)
                canvas.create_rectangle(xcoord3, 350, xcoord3 + 200, 260, fill = 'gray', width = 0)
                canvas.create_rectangle(xcoord3, 410, xcoord3 + 200, 360, fill = 'gray', width = 0)

            if level1 <= impedance <= level2:

                canvas.create_rectangle(xcoord3, 250, xcoord3 + 200, 190, fill = color, width = 0)
                canvas.create_rectangle(xcoord3, 350, xcoord3 + 200, 260, fill = 'gray', width = 0)
                canvas.create_rectangle(xcoord3, 410, xcoord3 + 200, 360, fill = 'gray', width = 0)

            if level2 < impedance <= level3:

                canvas.create_rectangle(xcoord3, 250, xcoord3 + 200, 190, fill = 'gray', width = 0)
                canvas.create_rectangle(xcoord3, 350, xcoord3 + 200, 260, fill = 'yellow', width = 0)
                canvas.create_rectangle(xcoord3, 410, xcoord3 + 200, 360, fill = 'gray', width = 0)

            if impedance > level3:

                canvas.create_rectangle(xcoord3, 250, xcoord3 + 200, 190, fill = 'gray', width = 0)
                canvas.create_rectangle(xcoord3, 350, xcoord3 + 200, 260, fill = 'gray', width = 0)
                canvas.create_rectangle(xcoord3, 410, xcoord3 + 200, 360, fill = 'red', width = 0)

            for i in range(24):
                if 0.416666667*(i-1) < deflection_new <= 0.416666667*i:
                    deflection_bar = 0.416666667*i
                    deflectionBar = canvas.create_rectangle(xcoord1, 200-20-ys, xcoord1+xs, 430-20-(deflection_bar*24), fill="#262626", width=0)
                    deflectionValueText = canvas.create_text(xcoord1+100,430-50-ys-(deflection_bar*24), fill=c1[i], font=("Helvetica",28), text=(str(round(deflection_new,1)),degree_sign), anchor=CENTER)
                
                if 1.5*(i-1) < force <= 1.5*i:
                    force = 1.5*i
                    forceBar = canvas.create_rectangle(xcoord2, 200-20-ys, xcoord2+xs, 430-20-(force*6.6666667), fill="#262626", width=0)
                    forceValueText = canvas.create_text(xcoord2+100,430-50-ys-(force*6.666667), fill=c2[i], font=("Helvetica",28), text=(str(force),"lb"), anchor=CENTER)
                
                if force >= 34.5:
                    force_max = 34.5
                    force2 = round(float(dataArray[1]))
                    forceBar = canvas.create_rectangle(xcoord2, 200-20-ys, xcoord2+200, 430-20-(force_max*6.6666667), fill="#262626", width=0)
                    forceValueText = canvas.create_text(xcoord2+100,430-70-ys-(force_max*6.6666667), fill="red", font=("Helvetica",33), text=(str(force2),"lbs"), anchor=CENTER)
                    

                if deflection_new >= 9.58:
                    deflection_max = 9.58
                    deflection2 = round(float(dataArray[0]),1)
                    deflectionBar = canvas.create_rectangle(xcoord1, 200-20-ys, xcoord1+xs, 430-20-(deflection_max*24), fill="#262626", width=0)
                    deflectionValueText = canvas.create_text(xcoord1+100,430-70-ys-(deflection_max*24), fill="red", font=("Helvetica",33), text=(str(deflection2),degree_sign), anchor=CENTER)

                
            
 
                try: 

                    x_list = deflection_filtered
                    y_list.append(dataArray[1])
                    z_list.append(dataArray[2])

                except:
                    pass
            
        except:
            pass
        
      


        root.update()



        canvas.delete("all")
        
