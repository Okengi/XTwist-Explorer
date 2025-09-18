from MersenneTwister import MersenneTwister
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter as ct
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def set_up_mt_tab(tab):

    def canvas_update():
        canvas.delete("all")

        if hasattr(canvas, "table_frame") and canvas.table_frame is not None:
            canvas.table_frame.destroy()

        canvas.table_frame = ct.CTkFrame(canvas, corner_radius=10, fg_color="transparent")
        canvas.create_window((0, 0), window=canvas.table_frame, anchor="nw")
        
        num_values_to_show = 50 # len(mt.MT_Seeds)
        
        stop = False

        for row in range(round(num_values_to_show / 4)):
            if stop:
                break
            for col in range(4):
                index = row * 4 + col
                if index >= num_values_to_show:
                    stop = True
                    break
                cell_frame = ct.CTkFrame(canvas.table_frame, corner_radius=5, fg_color="#2b2b2b", border_width=1, border_color="black")
                cell_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

                value_label = ct.CTkLabel(cell_frame, text=f"{mt.MT_Seeds[index]}", font=("Roboto", 12), anchor="center", text_color="#e35b52")
                value_label.pack(padx=5, pady=5)

        
        canvas.table_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        value_label.pack(padx=5, pady=5)

    def setup_seed_frame():
        for widget in MT_State_Frame.winfo_children():
            widget.destroy()

        stats_label = ct.CTkLabel(MT_State_Frame, text="Seeds", font=("Roboto", 20))
        stats_label.pack(pady=10)

        scrollable_frame = ct.CTkFrame(MT_State_Frame, corner_radius=10, fg_color="transparent")
        scrollable_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        global canvas
        canvas = tk.Canvas(scrollable_frame, bg="#333333", highlightthickness=0) 
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        scrollbar = ct.CTkScrollbar(scrollable_frame, command=canvas.yview, button_color="#e35b52",  button_hover_color="#f6756b")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas_update()
        

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
        for widget in mt_histogram_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot()
        ax.hist(values_for_diagrams, bins=binsC.get(), density=True, color="red", alpha=0.5, edgecolor="black")
        ax.set_title("Histogram")
        ax.set_xlabel("werte")
        ax.set_ylabel("Dichte")

        canvas = FigureCanvasTkAgg(fig, master=mt_histogram_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        counts, bin_edges = np.histogram(values_for_diagrams, bins=binsC.get(), density=True)
        bin_widths = np.diff(bin_edges)

        fläche = np.sum(counts * bin_widths)
        print("Gesamtfläche:", fläche)

    
    def mersenne_twister_scatter(_=None):
        if not dreiD.get():
            for widget in mt_scatter_frame.winfo_children():
                widget.destroy()

            fig = Figure(figsize=(6, 4))
            ax = fig.add_subplot()
            ax.scatter(values_for_diagrams[:-1], values_for_diagrams[1:], alpha=0.5, color="red")
            ax.set_title("Scatter Plot 2D")
            ax.set_xlabel("x[i]")
            ax.set_ylabel("x[i+1]")

            canvas = FigureCanvasTkAgg(fig, master=mt_scatter_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            for widget in mt_scatter_frame.winfo_children():
                widget.destroy()

            fig = Figure(figsize=(6, 4))
            ax = fig.add_subplot(projection="3d")
            ax.scatter(values_for_diagrams[:-2],values_for_diagrams[1:-1], values_for_diagrams[2:], alpha=0.5, color="red")
            ax.set_title("Scatter Plot 3D")

            canvas = FigureCanvasTkAgg(fig, master=mt_scatter_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    
    def sample_size_change(_=None):
        n = anzahl.get()
        sample_size_value_label.configure(text=n)
        global values_for_diagrams
        values_for_diagrams = np.array(mt_values[:n])
        mersenne_twister_histogram()
        mersenne_twister_scatter()
    
    def bins_value_change(_=None):
        bins_value_label.configure(text=binsC.get())
        mersenne_twister_histogram()

 

    def switch(_=None):
        d = dreiD.get()
        if d:
            dreiD.set(False)
            switch_button.configure(text="3D Scatter Plot")
        else:
            dreiD.set(True)
            switch_button.configure(text="2D Scatter Plot")
        mersenne_twister_scatter()
        

    def set_up_mt_controls(_=None):
        control_frame.grid_rowconfigure(tuple(range(5)), weight=1)
        control_frame.grid_columnconfigure(tuple(range(2)), weight=1)

        control_label = ct.CTkLabel(control_frame, text="Controls", font=("Roboto", 20))
        control_label.grid(row=0, column=0, columnspan=2)

        # Sample Slider
        sample_size_frame = ct.CTkFrame(control_frame)
        sample_size_frame.grid(row=1,column=1, padx=5)
        sample_size_slider_label = ct.CTkLabel(control_frame, text="Sample Size", font=("Roboto", 12))
        sample_size_slider_label.grid(row=1, column=0, padx=10)
        sample_size_slider = ct.CTkSlider(sample_size_frame, from_=100, to=5000,variable=anzahl, command=sample_size_change, fg_color="#e35b52", progress_color="#783e3a", button_color="#991717", button_hover_color="#991717")
        sample_size_slider.grid(row=0, column=0, sticky="ew")
        global sample_size_value_label
        sample_size_value_label = ct.CTkLabel(sample_size_frame, text=anzahl.get())
        sample_size_value_label.grid(row=0, column=1, padx=10)
        # Bins Slider
        bins_frame = ct.CTkFrame(control_frame)
        bins_frame.grid(row=2, column=1)
        bins_slider_label = ct.CTkLabel(control_frame, text="Bins", font=("Roboto", 12))
        bins_slider_label.grid(row=2,column=0)
        bins_slider = ct.CTkSlider(bins_frame, from_=10, to=50,variable=binsC, command=bins_value_change, fg_color="#e35b52", progress_color="#783e3a", button_color="#991717", button_hover_color="#991717")
        bins_slider.grid(row=0, column=0, sticky="ew")
        global bins_value_label
        bins_value_label = ct.CTkLabel(bins_frame, text=binsC.get())
        bins_value_label.grid(row=0, column=1, padx=10)
        # Seed Changes Entry and Button
        seed_label = ct.CTkLabel(control_frame, text="Seed", font=("Roboto", 12))
        seed_label.grid(row=3, column=0)
        seed_frame = ct.CTkFrame(control_frame, fg_color="transparent")
        seed_frame.grid(row=3, column=1, sticky="ew")
        seed_frame.grid_columnconfigure(0, weight=1)
        global seed_entry
        seed_entry = ct.CTkEntry(seed_frame,width=150, textvariable=seed, border_color="#e35b52")
        seed_entry.grid(row=0, column=0)
        seed_apply_button = ct.CTkButton(seed_frame, text="Apply", font=("Roboto", 12), command=seed_change, width=50, fg_color="#e35b52", hover_color="#f6756b")
        seed_apply_button.grid(row=0, column=1, padx=10)
        # Switch between 2d and 3d
        global switch_button
        switch_button = ct.CTkButton(control_frame, text="3D Scatter Plot", command=switch, fg_color="#e35b52", hover_color="#f6756b")
        switch_button.grid(row=4, column=0, columnspan=2)

    def seed_change(_=None):
        seed=seed_entry.get()
        
        global mt, mt_values , values_for_diagrams
        mt = MersenneTwister(int(seed))
        mt_values = np.array([mt.random() for _ in range(5000)])
        values_for_diagrams = np.array(mt_values[:anzahl.get()])
        mersenne_twister_histogram()
        mersenne_twister_scatter()
        setup_seed_frame()
        show_twisted()

    anzahl = tk.IntVar(value=1000)
    binsC = tk.IntVar(value=10)
    dreiD = tk.BooleanVar(value=False)
    seed = tk.StringVar(value="0")

    global mt
    mt = MersenneTwister(0)
    mt_values = np.array([mt.random() for _ in range(5000)])

    #show = np.empty(anzahl)
    #for i in range(anzahl):
    #    show[i] = mt_values[i]
    global values_for_diagrams
    values_for_diagrams = np.array(mt_values[:anzahl.get()])

   
    # Mersenne Twister Label
    label = ct.CTkLabel(tab, text="Mersenne Twister", font=("Roboto", 30))
    label.grid(row=0, column=0, columnspan=3, pady=20)
    # Frame for MT Stats
    MT_State_Frame = ct.CTkFrame(tab, corner_radius=10)
    MT_State_Frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
    # Frame for Histogram
    mt_histogram_frame = ct.CTkFrame(tab, corner_radius=10)
    mt_histogram_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
    # Frame for Scatter Plot
    mt_scatter_frame = ct.CTkFrame(tab, corner_radius=10)
    mt_scatter_frame.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")
    # Frame Twisted
    MT_Twisted_Frame = ct.CTkFrame(tab, corner_radius=10)
    MT_Twisted_Frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
    # Frame Controls
    control_frame = ct.CTkFrame(tab, corner_radius=10)
    control_frame.grid(row=1, column=2, padx=20, pady=20, sticky="nsew")

    

    # Initial Render
    
    setup_seed_frame()
    show_twisted()
    mersenne_twister_histogram()
    mersenne_twister_scatter()
    
    set_up_mt_controls()
    