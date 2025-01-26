from MersenneTwister import MersenneTwister
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter as ct
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def set_up_mt_tab(tab):
   
    mt = MersenneTwister(0)

    def show_stats():
        for widget in MT_State_Frame.winfo_children():
            widget.destroy()

        stats_label = ct.CTkLabel(MT_State_Frame, text="MT Seeds", font=("Roboto", 16))
        stats_label.pack(pady=10)

        scrollable_frame = ct.CTkFrame(MT_State_Frame, corner_radius=10, fg_color="transparent")
        scrollable_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        canvas = tk.Canvas(scrollable_frame, bg="white", highlightthickness=0) 
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ct.CTkScrollbar(scrollable_frame, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame inside canvas to hold the table
        table_frame = ct.CTkFrame(canvas, corner_radius=10, fg_color="transparent")
        canvas.create_window((0, 0), window=table_frame, anchor="nw")

        # Generate table data
        num_values_to_show = 50
        values_per_column = num_values_to_show // 4

        for col in range(4):
            start_index = col * values_per_column
            end_index = start_index + values_per_column

            for row, i in enumerate(range(start_index, end_index)):
                cell_frame = ct.CTkFrame(table_frame, corner_radius=0, fg_color="transparent", border_width=1, border_color="black")
                cell_frame.grid(row=row, column=col, padx=5, pady=5)

                value_label = ct.CTkLabel(cell_frame, text=f"{mt.MT_Seeds[i]}", font=("Roboto", 12), anchor="center", text_color="black")
                value_label.pack(padx=5, pady=5)

        table_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        value_label.pack(padx=5, pady=5)

    def show_twisted():
        for widget in MT_Twisted_Frame.winfo_children():
            widget.destroy()

        stats_label = ct.CTkLabel(MT_Twisted_Frame, text="MT Twisted", font=("Roboto", 16))
        stats_label.pack(pady=10)

        scrollable_frame = ct.CTkFrame(MT_Twisted_Frame, corner_radius=10, fg_color="transparent")
        scrollable_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        canvas = tk.Canvas(scrollable_frame, bg="white", highlightthickness=0) 
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ct.CTkScrollbar(scrollable_frame, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame inside canvas to hold the table
        table_frame = ct.CTkFrame(canvas, corner_radius=10, fg_color="transparent")
        canvas.create_window((0, 0), window=table_frame, anchor="nw")

        # Generate table data
        num_values_to_show = 50
        values_per_column = num_values_to_show // 4

        for col in range(4):
            start_index = col * values_per_column
            end_index = start_index + values_per_column

            for row, i in enumerate(range(start_index, end_index)):
                cell_frame = ct.CTkFrame(table_frame, corner_radius=0, fg_color="transparent", border_width=1, border_color="black")
                cell_frame.grid(row=row, column=col, padx=5, pady=5)

                value_label = ct.CTkLabel(cell_frame, text=f"{mt.MT[i]}", font=("Roboto", 12), anchor="center", text_color="black")
                value_label.pack(padx=5, pady=5)

        table_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        value_label.pack(padx=5, pady=5)


    def mersenne_twister_histogram(_=None):
        n = anzahl.get()
        bins = binsC.get()
        mt_values = [mt.random() for _ in range(n)]

        
        for widget in mt_histogram_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot()
        ax.hist(mt_values, bins=bins, density=True, color="red", alpha=0.5, edgecolor="black")
        ax.set_title("Histogram")
        ax.set_xlabel("werte")
        ax.set_ylabel("Dichte")

        canvas = FigureCanvasTkAgg(fig, master=mt_histogram_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    
    def mersenne_twister_scatter(_=None):
        n = anzahl.get()

        mt_werte = [mt.random() for _ in range(n)]

        for widget in mt_scatter_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot()
        ax.scatter(mt_werte[:-1], mt_werte[1:], alpha=0.5, color="red")
        ax.set_title("Scatter Plot 2D")
        ax.set_xlabel("x[i]")
        ax.set_ylabel("x[i+1]")

        canvas = FigureCanvasTkAgg(fig, master=mt_scatter_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def update_graphs(_=None):
        mt.reset()
        mersenne_twister_histogram()
        mersenne_twister_scatter()
    

    def controls(_=None):
        sliderN = ct.CTkSlider(anzahlBinFrame, from_=1, to=10000,variable=anzahl, command=update_graphs)
        sliderN.grid(row=0, column=1)

        slider_label = ct.CTkLabel(anzahlBinFrame, text="Sample Size")
        slider_label.grid(row=0, column=0)

        sliderB = ct.CTkSlider(anzahlBinFrame, from_=10, to=50,variable=binsC, command=mersenne_twister_histogram)
        sliderB.grid(row=1, column=1)

        slider_labell = ct.CTkLabel(anzahlBinFrame, text="Bins")
        slider_labell.grid(row=1, column=0)
    

    anzahl = tk.IntVar(value=1000)
    binsC = tk.IntVar(value=10)
    dreiD = tk.BooleanVar(value=False)

    # Top Label
    label = ct.CTkLabel(tab, text="Mersenne Twister", font=("Roboto", 30))
    label.grid(row=0, column=0, columnspan=3, pady=20)

    # Frame for MT Stats and Controls
    MT_State_Frame = ct.CTkFrame(tab, corner_radius=10)
    MT_State_Frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    # Frame for Histogram
    mt_histogram_frame = ct.CTkFrame(tab, corner_radius=10)
    mt_histogram_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

    # Frame for Scatter Plot
    mt_scatter_frame = ct.CTkFrame(tab, corner_radius=10)
    mt_scatter_frame.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    # Add Buttons and Callbacks
    MT_Twisted_Frame = ct.CTkFrame(tab, corner_radius=10)
    MT_Twisted_Frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

    anzahlBinFrame = ct.CTkFrame(tab, corner_radius=10)
    anzahlBinFrame.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

    

    # Initial Render
    
    show_stats()
    mersenne_twister_histogram()
    mersenne_twister_scatter()
    show_twisted()
    controls()
