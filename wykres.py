import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors
import os
import subprocess as sb
import tkinter as tk 
from tkinter import ttk

def __main__(value: list[str]):

    m = value[0]
    b0 = value[1]
    y0 = value[2]
    h = value[3]
    
    mentry.delete(0, tk.END)
    bentry.delete(0, tk.END)
    yentry.delete(0, tk.END)
    hentry.delete(0, tk.END)

    v0= "0" #input("Wprowadź prękość początkową obiektu: ")

    sb.run("g++ -std=c++20 mmm.cpp -o mmm", shell=True, stdout=sb.PIPE)
    if(os.name == "nt"):
        command="mmm.exe "+m+' '+b0+' '+y0+' '+h+' '+ v0
    elif(os.name == "posix"):
        command = "./mmm "+m+' '+b0+' '+y0+' '+h+' '+ v0
    sb.run(command, shell=True, stdout=sb.PIPE)

    file = open(r"wyniki.csv", "rt")

    file.readline()
    pocz=file.tell()
    lines = len(file.readlines())
    file.seek(pocz)
    y=[]
    v=[]
    t=[]
    a=[]
    #b=[]

    for i in range(lines-1):
        s=file.readline()
        s=s.split(';')
        t.append(float(s[0]))
        y.append(float(s[1]))
        v.append(float(s[2]))
        a.append(float(s[3]))
        #b.append(float(s[3]))

    for widget in plot_frame.winfo_children():
        widget.destroy()

    fig1 = Figure(figsize=(4, 2), dpi=90)
    ax1 = fig1.add_subplot(111)
    l1, = ax1.plot(t, v, color='blue')
    ax1.set_title("Prędkość ciała spadającego")
    ax1.set_xlabel("Czas [s]")
    ax1.set_ylabel("Prędkość [m/s]")
    ax1.grid(True)
    cursor1 = mplcursors.cursor(l1, hover=True)
    @cursor1.connect("add")
    def on_add(sel):
        sel.annotation.set(text=f'Czas: {sel.target[0]:.4f} [s]\n Prędkość ciała: {sel.target[1]:.2f} [m/s]')

    canvas1 = FigureCanvasTkAgg(fig1, master=plot_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH, expand=True)


    fig2 = Figure(figsize=(4, 2), dpi=90)
    ax2 = fig2.add_subplot(111)
    l2, = ax2.plot(t, y, color='green')
    ax2.set_title("Wysokość ciała spadającego")
    ax2.set_xlabel("Czas [s]")
    ax2.set_ylabel("Wysokość [m]")
    ax2.grid(True)
    cursor2 = mplcursors.cursor(l2, hover=True)
    @cursor2.connect("add")
    def on_add(sel):
        sel.annotation.set(text=f'Czas: {sel.target[0]:.4f} [s]\n Wysokość ciała: {sel.target[1]:.2f} [m]')

    canvas2 = FigureCanvasTkAgg(fig2, master=plot_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH, expand=True)


    fig3 = Figure(figsize=(4, 2), dpi=90)
    ax3 = fig3.add_subplot(111)
    l3, = ax3.plot(t, a, color='red')
    ax3.set_title("Przyspieszenie ciała spadającego")
    ax3.set_xlabel("Czas [s]")
    ax3.set_ylabel("Przyspieszenie [m/s^2]")
    ax3.grid(True)
    cursor3 = mplcursors.cursor(l3, hover=True)
    @cursor3.connect("add")
    def on_add(sel):
        sel.annotation.set(text=f'Czas: {sel.target[0]:.4f} [s]\n Przyspieszenie ciała: {sel.target[1]:.2f} [m/s^2]')

    canvas3 = FigureCanvasTkAgg(fig3, master=plot_frame)
    canvas3.draw()
    canvas3.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

def commaCheck():
    m = mentry.get().replace(',', '.')
    b = bentry.get().replace(',', '.')
    h = hentry.get().replace(',', '.')
    y = yentry.get().replace(',', '.')

    return [m, b, y, h]

def validCheck(values: list[str]):
    mOK = bOK = yOK = hOK = True
    try:
        float(values[0])
    except:
        mOK = False
        mentry.delete(0, tk.END)
    try:
        float(values[1])
    except: 
        bOK = False
        bentry.delete(0, tk.END)
    try:
        float(values[2])
    except:
        yOK = False
        yentry.delete(0, tk.END)
    try:
        float(values[3])
    except:
        hOK = False
        hentry.delete(0, tk.END)
    if(mOK and bOK and hOK and yOK):     
        return 1
    else:
        return -1

window = tk.Tk()
window.title("Symulacja spadku")
window.geometry("1000x800")

def buttonPress(event):
    params = commaCheck()
    if(validCheck(params) == 1):
        guzik.config(relief = tk.SUNKEN)
        __main__(params)
        guzik.config(relief = tk.RAISED)
    else:
        return

io = tk.Frame(window)
io.pack(padx=20, pady=20)

mlabel = tk.Label(text= "Wprowadź masę obiektu", master= io)
mentry = tk.Entry(master= io)
blabel = tk.Label(text= "Wprowadź współczynnik oporu powietrza", master= io)
bentry = tk.Entry(master= io)
ylabel = tk.Label(text= "Wprowadź wysokość początkową", master= io)
yentry = tk.Entry(master= io)
hlabel = tk.Label(text = "Wprowadź krok całkowania", master= io)
hentry = tk.Entry(master= io)
guzik = tk.Button(text = "Symuluj", master= io)
#kursory = tk.Button(io, text="Wyczyść kursory", command=lambda: [cursor.remove() for cursor in active_cursors])

mlabel.pack()
mentry.pack(pady=5)
blabel.pack()
bentry.pack(pady=5)
ylabel.pack()
yentry.pack(pady=5)
hlabel.pack()
hentry.pack(pady=5)
guzik.pack(pady=10)
guzik.bind("<Button-1>", buttonPress)

# Plot section
plot_frame = tk.Frame(window, bd=2, relief=tk.SUNKEN)
plot_frame.pack(fill=tk.BOTH, expand=True, padx=10)

window.mainloop()
