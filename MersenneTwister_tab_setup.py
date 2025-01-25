from MersenneTwister import MersenneTwister
import matplotlib.pyplot as plt


import tkinter as tk
import customtkinter as ct
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

def set_up_mt_tab(tap):
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
    
    mt = MersenneTwister(1956)

    label = ct.CTkLabel(tap, text="Mersenne Twiester",font=('Robo', 50))
    label.grid(row=0, column= 1)

    mt_histogram_frame = ct.CTkFrame(tap)
    mt_histogram_frame.grid(row=1, column=0)

    mt_satter_frame = ct.CTkFrame(tap)
    mt_satter_frame.grid(row=1, column=1)

    mt_controls_frame = ct.CTkFrame(tap)
    mt_controls_frame.grid(row=0, column=0)

    mersenneTwister()
    mersenneTwisterScatter()
