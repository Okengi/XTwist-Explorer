from Linear_Congruential_Generator import LCG

import tkinter as tk
import customtkinter as ct
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

from statsmodels.graphics.tsaplots import plot_acf
import numpy as np
import scipy.stats
from scipy.stats import norm

def set_up_LCG_tab(tab):

    def update_all_visuals(_=None):
        sam_labell.configure(text=anzahl.get())
        bin_labell.configure(text=binsC.get())
        lcg.reset()
        update_function_label()
        histogram(lcg)
        #autocorelation()
        if dreiD.get():
            scetter3d()
        else:
            scetter()
    
    def scetter(_=None):
        n = anzahl.get()
        fig = Figure(figsize=(6,4))
        plot = fig.add_subplot()
        lcg_werte = [lcg.next() for _ in range(n)]

        for widget in scatter_frame.winfo_children():
            widget.destroy()

        plot.scatter(lcg_werte[:-1], lcg_werte[1:], alpha=0.5, color="blue")
        plot.set_title("LCG Scattertest")
        plot.set_xlabel("x[i]")
        plot.set_ylabel("x[i+1]") 
        canvas = FigureCanvasTkAgg(fig, master=scatter_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def scetter3d(_=None):
        n = anzahl.get()
        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot(111, projection='3d')

        lcg_werte = [lcg.next() for _ in range(n)]

        for widget in scatter_frame.winfo_children():
            widget.destroy()
        
        ax.scatter(lcg_werte[:-2], lcg_werte[1:-1],lcg_werte[2:], alpha=0.5, color="blue")
        ax.set_title("LCG Scattertest")
        canvas = FigureCanvasTkAgg(fig, master=scatter_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    def set_up_LCG_Controls():
        # Configure rows and columns for dynamic resizing
        control_frame.grid_rowconfigure(tuple(range(6)), weight=1)
        control_frame.grid_columnconfigure(tuple(range(5)), weight=1)

        # Entries and labels
        entryM = ct.CTkEntry(control_frame, width=150, textvariable=modules)
        entryM.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        sliderM_label = ct.CTkLabel(control_frame, text="Modulus:")
        sliderM_label.grid(row=0, column=0, padx=10, pady=10)

        entryA = ct.CTkEntry(control_frame, width=150, textvariable=multiplicator)
        entryA.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        sliderA_label = ct.CTkLabel(control_frame, text="Multiplier:")
        sliderA_label.grid(row=1, column=0, padx=10, pady=10)

        # Increment
        sliderC_label = ct.CTkLabel(control_frame, text="Increment:")
        sliderC_label.grid(row=2, column=0, padx=10, pady=10)
        entryC = ct.CTkEntry(control_frame, width=150, textvariable=increment)
        entryC.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        # Seed
        sliderSeed_label = ct.CTkLabel(control_frame, text="Seed:")
        sliderSeed_label.grid(row=3, column=0, padx=10, pady=10)
        entrySeed = ct.CTkEntry(control_frame, width=150, textvariable=seed)
        entrySeed.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        # Sample Size
        samplFr = ct.CTkFrame(control_frame)
        samplFr.grid(row=4, column=1)
        slider_label = ct.CTkLabel(control_frame, text="Sample Size:")
        slider_label.grid(row=4, column=0, padx=10, pady=10)
        sliderN = ct.CTkSlider(samplFr, from_=1, to=5000, variable=anzahl, command=update_all_visuals)
        sliderN.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

            
        # Bins
        binfram = ct.CTkFrame(control_frame)
        binfram.grid(row=5, column=1)
        slider_labell = ct.CTkLabel(control_frame, text="Bins:")
        slider_labell.grid(row=5, column=0, padx=10, pady=10)
        sliderB = ct.CTkSlider(binfram, from_=10, to=50, variable=binsC, command=update_all_visuals)
        sliderB.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        global sam_labell, bin_labell
        sam_labell = ct.CTkLabel(samplFr, text=anzahl.get())
        sam_labell.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        bin_labell = ct.CTkLabel(binfram, text=binsC.get())
        bin_labell.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
 


        # Presets with checkboxes
        global c1, c2, c3
        c1 = ct.CTkCheckBox(control_frame, text="ZX81", onvalue=1, offvalue=0, command=set_preset_ZX81)
        c1.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        c2 = ct.CTkCheckBox(control_frame, text="Borderland", onvalue=1, offvalue=0, command=set_preset_Borderland)
        c2.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        c3 = ct.CTkCheckBox(control_frame, text="RANDU", onvalue=1, offvalue=0, command=set_preset_RANDU)
        c3.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        # Apply button
        b = ct.CTkButton(control_frame, text="Apply", command=update_all_visuals)
        b.grid(row=6, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

    def update_function_label(_=None):
        formula = f"$X_{{n+1}} = ({multiplicator.get()} \\cdot X_n + {increment.get()})_{{mod}} {modules.get()}$"
        
        for widget in formula_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(5, 1), facecolor="#2b2b2b")
        ax = fig.add_subplot()
        ax.set_facecolor("#2b2b2b") 
        ax.set_alpha(0.0)
        #ax.text(0.5, 0.5, formula, fontsize=12, ha="center", va="center", transform=ax.transAxes)
        ax.text(
                0.5, 0.5, formula, fontsize=14, ha="center", va="center",
                transform=ax.transAxes, color="white"
            )
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
        
        n = anzahl.get()
        bins = binsC.get()

        lcg_werte = [lcg.next() for _ in range(n)]

        for widget in histogram_frame.winfo_children():
            widget.destroy()
            

        fig = Figure(figsize=(6,4))
        plot = fig.add_subplot()
        plot.hist(lcg_werte, alpha=0.5, bins=bins, density=True, label="LCG", color="blue", edgecolor="black")
        plot.set_title("Histogram LCG")
        plot.set_xlabel("Werte")
        plot.set_ylabel("Dichte")

        canvas = FigureCanvasTkAgg(fig, master=histogram_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

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
        
    def switche(_=None):
        d = dreiD.get()
        if d:
            dreiD.set(False)
            b3d.configure(text="3d")
        else:
            dreiD.set(True)
            b3d.configure(text="2d")
        update_all_visuals()

    lcg = LCG()
    
    modules = tk.IntVar(value=lcg.m)
    multiplicator = tk.IntVar(value=lcg.a)
    increment = tk.IntVar(value=lcg.c)
    seed = tk.IntVar(value=lcg.X_0)
    anzahl = tk.IntVar(value=1000)
    binsC = tk.IntVar(value=10)
    dreiD = tk.BooleanVar(value=False)

    # Frames
    control_frame = ct.CTkFrame(tab)
    control_frame.grid(row=1, column=1, padx=10, pady=10)
    set_up_LCG_Controls()
    formula_frame = ct.CTkFrame(tab)
    formula_frame.grid(row=0, column=1, columnspan=2)
    lab = ct.CTkLabel(tab, text="Linear Congruential Generator", font=("Roboto", 30))
    lab.grid(row=0, column=0)

    histogram_frame = ct.CTkFrame(tab)
    histogram_frame.grid(row=1, column=0, padx=10, pady=10)

    scatter_frame = ct.CTkFrame(tab)
    scatter_frame.grid(row=2, column=0, padx=10, pady=10)

    b3d = ct.CTkButton(control_frame, text="3d", command=switche)
    b3d.grid(row=6, column=3, padx=10, pady=20, sticky="ew")

    update_all_visuals()
