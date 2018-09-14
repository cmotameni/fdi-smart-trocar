import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg # implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys
import numpy as np
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

c1 = ['#6DDAF8','#40C8F5','#25BEF3','#0CAFF1','#4DA9F6','#5EA7F8','#A1A1FD','#B59FFF','#BE90F8','#C483F2','#CB74EA','#D264E3','#DF46D4','#D954DB','#DF46D4','#ED27C6','#F416BE','#FA09B7','#FC04A8','#FD037B','#FD0266','#FE0253','#FF0003','#FF0003']  
c2 = ['#04B150','#1CB650','#28B950','#4FC150','#59C350','#72C950','#98D34B','#A6D941','#B2DE38','#CAE827','#F0F90B','#FEFE01','#FFF900','#FFED00','#FFDA00','#FFCE00','#FFC200','#FFC200','#FFB300','#FF9B00','#FF8500','#FF5B00','#FF4000','#FF2B00']

def graph_deflection():
    root = Tk.Tk()
    root.wm_title("Embedding in TK")
    root.attributes("-fullscreen", True)
    root.tk.call('tk', 'scaling', 133.0/72.0 )

    data = np.genfromtxt('deflection.csv', delimiter=',', names=['time','def'])

    f = Figure(figsize=(5, 4), dpi=100)
    a = f.add_subplot(111)

    degree_sign= u'\N{DEGREE SIGN}'

    t = data['def']
    s = data['time']

    a.plot(t, s, color = c1[1], label='deflection data')
    a.patch.set_facecolor('#262626')
    a.spines['bottom'].set_color('white')
    a.spines['top'].set_color('white')
    a.spines['right'].set_color('white')
    a.spines['left'].set_color('white')
    a.tick_params(axis='x', colors='white')
    a.tick_params(axis='y', colors='white')
    a.set_title("DEFLECTION DATA")
    a.set_xlabel("time (s)")
    a.set_ylabel("deviation (degrees)")
    a.yaxis.label.set_color('white')
    a.xaxis.label.set_color('white')
    a.title.set_color('white')
    f.patch.set_facecolor('#262626')

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def on_key_event(event):
        print('you pressed %s' % event.key)
        key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect('key_press_event', on_key_event)



    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    button = Tk.Button(master=root, text='Quit', command=_quit)
    button.pack(side=Tk.BOTTOM)

    Tk.mainloop()
    # If you put root.destroy() here, it will cause an error if
    # the window is closed with the window manager.

def graph_force():
    root = Tk.Tk()
    root.wm_title("Embedding in TK")
    root.attributes("-fullscreen", True)

    data = np.genfromtxt('force.csv', delimiter=',', names=['time','force'])


    f = Figure(figsize=(5, 4), dpi=100)
    a = f.add_subplot(111)


    t = data['force']
    s = data['time']

    a.plot(t, s, color = c2[1], label='deflection data')
    a.patch.set_facecolor('#262626')
    a.spines['bottom'].set_color('white')
    a.spines['top'].set_color('white') 
    a.spines['right'].set_color('white')
    a.spines['left'].set_color('white')
    a.tick_params(axis='x', colors='white')
    a.tick_params(axis='y', colors='white')
    a.yaxis.label.set_color('white')
    a.xaxis.label.set_color('white')
    a.set_title("FORCE DATA")
    a.set_xlabel("time (s)")
    a.set_ylabel("Force (lbs)")
    a.title.set_color('white')
    f.patch.set_facecolor('#262626')


    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def on_key_event(event):
        print('you pressed %s' % event.key)
        key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect('key_press_event', on_key_event)



    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    button = Tk.Button(master=root, text='Quit', command=_quit)
    button.pack(side=Tk.BOTTOM)

    Tk.mainloop()
    # If you put root.destroy() here, it will cause an error if
    # the window is closed with the window manager.

def graph_impedance():
    root = Tk.Tk()
    root.wm_title("Embedding in TK")
    root.attributes("-fullscreen", True)

    data = np.genfromtxt('impedance.csv', delimiter=',', names=['time','imp'])


    f = Figure(figsize=(5, 4), dpi=100)
   
    a = f.add_subplot(111)

    t = data['imp']
    s = data['time']

    a.plot(t, s, color = 'white', label='deflection data')
    a.patch.set_facecolor('#262626')
    a.spines['bottom'].set_color('white')
    a.spines['top'].set_color('white') 
    a.spines['right'].set_color('white')
    a.spines['left'].set_color('white')
    a.tick_params(axis='x', colors='white')
    a.tick_params(axis='y', colors='white')
    a.set_title("IMPEDANCE DATA")
    a.set_xlabel("time (s)")
    a.set_ylabel("impedance (kOhm)")
    a.yaxis.label.set_color('white')
    a.xaxis.label.set_color('white')
    a.title.set_color('white')
    f.patch.set_facecolor('#262626')

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def on_key_event(event):
        print('you pressed %s' % event.key)
        key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect('key_press_event', on_key_event)



    def _quit():
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    button = Tk.Button(master=root, text='Quit', command=_quit)
    button.pack(side=Tk.BOTTOM)

    Tk.mainloop()
    # If you put root.destroy() here, it will cause an error if
    # the window is closed with the window manager.