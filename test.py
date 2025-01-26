from Linear_Congruential_Generator import LCG
from MersenneTwister import MersenneTwister
import matplotlib.pyplot as plt
import random

import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

def set_up_LCG_Controls():
    global sliderA, sliderC, sliderSeed, entryM

    entryM = tk.Entry(control_frame, width=15, textvariable=modules)
    entryM.grid(row=0, column=1)
    sliderM_label = tk.Label(control_frame, text="Moduls")
    sliderM_label.grid(row=0, column=0)


    entryA = tk.Entry(control_frame, width=15, textvariabl=multiplicator)
    entryA.grid(row=1, column=1)
    
    sliderA_label = tk.Label(control_frame, text="Multiplikator")
    sliderA_label.grid(row=1, column=0)
    
    entryC = tk.Entry(control_frame, width=15, textvariable=increment)
    entryC.grid(row=0, column=3)
    
    sliderC_label = tk.Label(control_frame, text="Inkrement")
    sliderC_label.grid(row=0, column=2)
    
    entrySeed = tk.Entry(control_frame, width=15, textvariable=seed)
    entrySeed.grid(row=1, column=3)
    
    sliderSeed_label = tk.Label(control_frame, text="Seed")
    sliderSeed_label.grid(row=1, column=2)

    sliderN = tk.Scale(control_frame, from_=1, to=1000,variable=anzahlLCG, command=update_all_visuals, width=10, length=100, orient="horizontal" )
    sliderN.grid(row=2, column=1)
    slider_label = tk.Label(control_frame, text="Sample Size")
    slider_label.grid(row=2, column=0)
    sliderB = tk.Scale(control_frame, from_=10, to=50,variable=binsC, command=update_all_visuals, width=10, length=100, orient="horizontal" )
    sliderB.grid(row=2, column=3)
    slider_labell = tk.Label(control_frame, text="Bins")
    slider_labell.grid(row=2, column=2)
    global c1, c2, c3
    c1 = tk.Checkbutton(control_frame, text="ZX81", onvalue=1, offvalue=0, command=set_preset_ZX81)
    c1.grid(row=0, column=4)
    c2 = tk.Checkbutton(control_frame, text="Borderland", onvalue=1, offvalue=0, command=set_preset_Borderland)
    c2.grid(row=1, column=4)
    c3 = tk.Checkbutton(control_frame, text="RANDU", onvalue=1, offvalue=0, command=set_preset_RANDU)
    c3.grid(row=2, column=4)

def set_preset_RANDU(_=None):
    modules.set(2**31)
    multiplicator.set(65539)
    increment.set(0)
    c2.deselect()
    c1.deselect()
    update_all_visuals() 
def set_preset_ZX81(_=None):
    modules.set(2**16 + 1)
    multiplicator.set(75)
    increment.set(74)
    c2.deselect()
    c3.deselect()
    update_all_visuals()
def set_preset_Borderland(_=None):
    modules.set(2**31)
    multiplicator.set(22695477)
    increment.set(1)
    c1.deselect()
    c3.deselect()
    update_all_visuals()

def mersenneTwister(_=None):   
    n = 500
    bins = 10
    

    lcg_werte = [mt.random() for _ in range(n)]

    for widget in mt_histogram_frame.winfo_children():
        widget.destroy()
        
   
    fig = Figure(figsize=(6,4))
    plot = fig.add_subplot()
    plot.hist(lcg_werte, alpha=0.5, bins=bins, density=True, label="LCG", color="red", edgecolor="black")
    plot.set_title("Histogram Mersenne Twister")
    plot.set_xlabel("Werte")
    plot.set_ylabel("Dichte")

    # Matplotlib-Canvas in Tkinter einbetten
    canvas = FigureCanvasTkAgg(fig, master=mt_histogram_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def mersenneTwisterScatter():
    fig = Figure(figsize=(6,4))
    plot = fig.add_subplot()
    n = 5000

    

    lcg_werte = [mt.random() for _ in range(n)]

    for widget in mt_satter_frame.winfo_children():
        widget.destroy()

    plot.scatter(lcg_werte[:-1], lcg_werte[1:], alpha=0.5, color="red")
    plot.set_title("MT Scatter Test")
    plot.set_xlabel("x[i]")
    plot.set_ylabel("x[i+1]") 
    canvas = FigureCanvasTkAgg(fig, master=mt_satter_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def update_function_label(_=None):
    formula = f"$X_{{n+1}} = ({multiplicator.get()} \\cdot X_n + {increment.get()})_{{mod}} {modules.get()}$"
    
    for widget in formula_frame.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(6, 1))
    ax = fig.add_subplot()
    ax.text(0.5, 0.5, formula, fontsize=12, ha="center", va="center", transform=ax.transAxes)
    ax.axis("off")

    canvas = FigureCanvasTkAgg(fig, master=formula_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def histogram(_=None):
    lcg.m = modules.get()
    lcg.a = multiplicator.get()
    lcg.c = increment.get()
    lcg.X_0 = seed.get()
    lcg.X = seed.get()
    
    n = anzahlLCG.get()
    bins = binsC.get()

    lcg_werte = [lcg.next() for _ in range(n)]

    for widget in plot_frame.winfo_children():
        widget.destroy()
        
   
    fig = Figure(figsize=(6,4))
    plot = fig.add_subplot()
    plot.hist(lcg_werte, alpha=0.5, bins=bins, density=True, label="LCG", color="blue", edgecolor="black")
    plot.set_title("Histogram LCG")
    plot.set_xlabel("Werte")
    plot.set_ylabel("Dichte")

    # Matplotlib-Canvas in Tkinter einbetten
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def scetter(_=None):
    # LCG Scatterplot
    n = anzahlLCG.get()
    fig = Figure(figsize=(6,4))
    plot = fig.add_subplot()
    lcg_werte = [lcg.next() for _ in range(n)]

    for widget in plot_frame_scatter.winfo_children():
        widget.destroy()

    #normierte_lcg_werte = [x / lcg.m for x in lcg_werte]
    #plot.scatter(normierte_lcg_werte[:-1], normierte_lcg_werte[1:], alpha=0.5)

    plot.scatter(lcg_werte[:-1], lcg_werte[1:], alpha=0.5, color="blue")
    plot.set_title("LCG: Wertepaare")
    plot.set_xlabel("x[i]")
    plot.set_ylabel("x[i+1]") 
    canvas = FigureCanvasTkAgg(fig, master=plot_frame_scatter)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def scetter3d():
    n = anzahlLCG.get()
    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111, projection='3d')

    lcg_werte = [lcg.next() for _ in range(n)]

    for widget in plot_frame_scatter.winfo_children():
        widget.destroy()
    
    ax.scatter(lcg_werte[:-2], lcg_werte[1:-1],lcg_werte[2:], alpha=0.5, color="blue")
    ax.set_title("LCG: Wertepaare")
    canvas = FigureCanvasTkAgg(fig, master=plot_frame_scatter)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def switche(_=None):
    d = dreiD.get()
    if d:
        dreiD.set(False)
        b3d.config(text="3d")
    else:
        dreiD.set(True)
        b3d.config(text="2d")
    update_all_visuals()

def update_all_visuals(_=None):
    update_function_label()
    histogram()
    if(dreiD.get()):
        scetter3d()
    else:
        scetter()

lcg = LCG()
mt = MersenneTwister(1956)

window = tk.Tk()
window.title("Zufallszahlen")
window.geometry("1200x600")

modules = tk.IntVar(value=lcg.m)
multiplicator = tk.IntVar(value=lcg.a)
increment = tk.IntVar(value=lcg.c)
seed = tk.IntVar(value=lcg.X_0)
anzahlLCG = tk.IntVar(value=1000)
binsC = tk.IntVar(value=10)
dreiD = tk.BooleanVar(value=False)

tapsController = ttk.Notebook(window)
tapsController.pack(fill='both', expand=True)

LCG_Tap_Screen = ttk.Frame(tapsController)
tapsController.add(LCG_Tap_Screen, text="LCG")


MT_Tap_Screen = ttk.Frame(tapsController)
tapsController.add(MT_Tap_Screen, text="Mersenne Twister")

mt_histogram_frame = tk.Frame(MT_Tap_Screen)
mt_histogram_frame.grid(row=1, column=0)

mt_satter_frame = tk.Frame(MT_Tap_Screen)
mt_satter_frame.grid(row=1, column=1)

mt_controls_frame = tk.Frame(MT_Tap_Screen)
mt_controls_frame.grid(row=0, column=0)

Vergleich_Tap_Screen = ttk.Frame(tapsController)
tapsController.add(Vergleich_Tap_Screen, text="Vergleich")

control_frame = tk.Frame(LCG_Tap_Screen)
control_frame.grid(row=	0, column=0)

set_up_LCG_Controls()
formula_frame = tk.Frame(LCG_Tap_Screen)
formula_frame.grid(row=0,column=1)
b = tk.Button(control_frame, text="Apply", command=update_all_visuals)
b.grid(row=4, column=0)
b3d = tk.Button(control_frame, text="3d", command=switche)
b3d.grid(row=4, column=1)


plot_frame = tk.Frame(LCG_Tap_Screen)
plot_frame.grid(row=1, column=0)

plot_frame_scatter = tk.Frame(LCG_Tap_Screen)
plot_frame_scatter.grid(row=1, column=1)


update_all_visuals()
mersenneTwister()
mersenneTwisterScatter()
window.mainloop()