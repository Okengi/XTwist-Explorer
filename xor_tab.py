from XOR_Shift_Generator import XOR_Shift_Generator_64Bit
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter as ct
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def setup_xor_shift_tab(tab: ct.CTkFrame):

    def setup_scatter(_=None):
        for widget in scatter_frame.winfo_children():
            widget.destroy()
        
        if not dreiD.get():
            fig = Figure(figsize=(6, 4))
            ax = fig.add_subplot()
            ax.scatter(values_for_diagrams[:-1], values_for_diagrams[1:], alpha=0.5, color="red")
            ax.set_title("Scatter Plot 2D")
            ax.set_xlabel("x[i]")
            ax.set_ylabel("x[i+1]")

            canvas = FigureCanvasTkAgg(fig, master=scatter_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        else:
            fig = Figure(figsize=(6, 4))
            ax = fig.add_subplot(projection="3d")
            ax.scatter(values_for_diagrams[:-2],values_for_diagrams[1:-1], values_for_diagrams[2:], alpha=0.5, color="red")
            ax.set_title("Scatter Plot 3D")

            canvas = FigureCanvasTkAgg(fig, master=scatter_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def setup_histogram(_=None):
        for widget in histogram_frame.winfo_children():
            widget.destroy()

        fig = Figure(figsize=(6, 4))
        ax = fig.add_subplot()
        ax.hist(values_for_diagrams, bins=int(binsC.get()), density=True, color="red", alpha=0.5, edgecolor="black")
        ax.set_title("Histogram")
        ax.set_xlabel("Werte")
        ax.set_ylabel("Dichte")

        canvas = FigureCanvasTkAgg(fig, master=histogram_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def sample_size_change(_=None):
        n = anzahl.get()
        sample_size_value_label.configure(text=n)
        global values_for_diagrams
        values_for_diagrams = np.array(values[:n])
        setup_histogram()
        setup_scatter()
    
    def bins_value_change(_=None):
        bins_value_label.configure(text=binsC.get())
        setup_histogram()

    def seed_change(_=None):
        global XOR_Generator, values_for_diagrams
        XOR_Generator = XOR_Shift_Generator_64Bit(seed=int(seed.get()))
        values = np.array([XOR_Generator.random() for _ in range(5000)])
        values_for_diagrams = np.array(values[:anzahl.get()])
        setup_scatter()
        setup_histogram()
        seed_shift_viusal()

    def show_bit_string_value(frame: ct.CTkFrame, string: str):
        h = ct.CTkLabel(frame, text="-", font=("Roboto", 13))
        h.grid(row=0,column=0, padx=4, pady=4)
        h1 = ct.CTkLabel(frame, text="-", font=("Roboto", 13))
        h1.grid(row=0,column=65, padx=4, pady=4)
        for i, char in enumerate(string):
            if char == "1":
                l = ct.CTkLabel(frame, text=char, font=("Roboto", 13), text_color="#e35b52")#, bg_color="#3242ef")
                
            else: 
                l = ct.CTkLabel(frame, text=char, font=("Roboto", 13))
            
            l.grid(row=0, column=i+1)

    def parameter_change(_=None):
        pass
    
    def seed_shift_viusal(_=None):
        for widget in algo_frame.winfo_children():
            widget.destroy()
        algo_frame.grid_rowconfigure(tuple(range(8)), weight=1)
        algo_frame.grid_columnconfigure(tuple(range(3)), weight=1)
        algo_visual_label = ct.CTkLabel(algo_frame, text="Seed Shift Visualiser", font=("Roboto", 20))
        algo_visual_label.grid(row=0, column=0, columnspan=3)
        value = int(seed.get())
        
        # 1 Shift ----------
        
        bit_string_1 = str(format(value, "064b"))
        bit_text_frame_1 = ct.CTkFrame(algo_frame, fg_color="transparent", border_width=1, border_color="#e3ff52", corner_radius=10)
        bit_text_frame_1.grid(row=1, column=0, columnspan=3, padx=10)
        show_bit_string_value(bit_text_frame_1, bit_string_1)

        value_label_befor_shift_1 = ct.CTkLabel(algo_frame, text="Seed: "+str(value), text_color="#e3ff52")
        value_label_befor_shift_1.grid(row=2, column=0)
        
        shiftby_label_1 = ct.CTkLabel(algo_frame, text=f"Shift a: << {str(XOR_Generator.A)}")
        shiftby_label_1.grid(row=2, column=1)

        value = value ^ (value << XOR_Generator.A ) & ( (1 << 64) - 1)

        value_label_after_shift_1 = ct.CTkLabel(algo_frame, text=str(value), text_color="#49e83e")
        value_label_after_shift_1.grid(row=2, column=2)

        # 2 Shift -------------------------
        bit_string_2 = str(format(value, "064b"))
        bit_text_frame_2 = ct.CTkFrame(algo_frame, fg_color="transparent", border_width=1, border_color="#49e83e", corner_radius=10)
        bit_text_frame_2.grid(row=3, column=0, columnspan=3, padx=10)
        show_bit_string_value(bit_text_frame_2, bit_string_2)

        value_label_befor_shift_2 = ct.CTkLabel(algo_frame, text=str(value), text_color="#49e83e")
        value_label_befor_shift_2.grid(row=4, column=0)
        
        shiftby_label_2 = ct.CTkLabel(algo_frame, text=f"Shift b: >> {str(XOR_Generator.B)}")
        shiftby_label_2.grid(row=4, column=1)

        value = value ^ (value >> XOR_Generator.B ) & ( (1 << 64) - 1)

        value_label_after_shift_2 = ct.CTkLabel(algo_frame, text=str(value), text_color="#4c3ee8")
        value_label_after_shift_2.grid(row=4, column=2)
        # 3 Shift
        bit_string_3 = str(format(value, "064b"))
        bit_text_frame_3 = ct.CTkFrame(algo_frame, fg_color="transparent", border_width=1, border_color="#4c3ee8", corner_radius=10)
        bit_text_frame_3.grid(row=5, column=0, columnspan=3, padx=10)
        show_bit_string_value(bit_text_frame_3, bit_string_3)

        value_label_befor_shift_3 = ct.CTkLabel(algo_frame, text=str(value), text_color="#4c3ee8")
        value_label_befor_shift_3.grid(row=6, column=0)
        
        shiftby_label_3 = ct.CTkLabel(algo_frame, text=f"Shift c: << {str(XOR_Generator.C)}")
        shiftby_label_3.grid(row=6, column=1)

        value = value ^ (value << XOR_Generator.C ) & ( (1 << 64) - 1)

        value_label_after_shift_3 = ct.CTkLabel(algo_frame, text=str(value), text_color="#b5159d")
        value_label_after_shift_3.grid(row=6, column=2)
        # Bits after 3 Shift
        bit_string_4 = str(format(value, "064b"))
        bit_text_frame_4 = ct.CTkFrame(algo_frame, fg_color="transparent", border_width=1, border_color="#b5159d", corner_radius=10)
        bit_text_frame_4.grid(row=7, column=0, columnspan=3, padx=10)
        show_bit_string_value(bit_text_frame_4, bit_string_4)


    def switch(_=None):
        d = dreiD.get()
        if d:
            dreiD.set(False)
            switch_button.configure(text="3D Scatter Plot")
        else:
            dreiD.set(True)
            switch_button.configure(text="2D Scatter Plot")
        setup_scatter()

    def setup_controls(_=None):
        control_frame.grid_rowconfigure(tuple(range(5)), weight=1)
        control_frame.grid_columnconfigure(tuple(range(3)), weight=1)

        controls_label = ct.CTkLabel(control_frame, text="Controls", font=("Roboto", 20))
        controls_label.grid(row=0, column=0, columnspan=3)
        # a b c controls
        a_frame = ct.CTkFrame(control_frame)
        a_frame.grid(row=1, column= 2, padx=5)
        a_text = ct.CTkLabel(a_frame, text="a: ")
        a_text.grid(row=0, column=0)
        a_input = ct.CTkEntry(a_frame,width=50, textvariable=a, border_color="#e35b52")
        a_input.grid(row=0,column=1)

        b_frame = ct.CTkFrame(control_frame)
        b_frame.grid(row=2, column= 2, padx=5)
        b_text = ct.CTkLabel(b_frame, text="b: ")
        b_text.grid(row=0, column=0)
        b_input = ct.CTkEntry(b_frame,width=50, textvariable=b, border_color="#e35b52")
        b_input.grid(row=0,column=1)

        c_frame = ct.CTkFrame(control_frame)
        c_frame.grid(row=3, column= 2, padx=5)
        c_text = ct.CTkLabel(c_frame, text="c: ")
        c_text.grid(row=0, column=0)
        c_input = ct.CTkEntry(c_frame,width=50, textvariable=c, border_color="#e35b52")
        c_input.grid(row=0,column=1)

        var_aplay_button = ct.CTkButton(control_frame, text="Apply", width=50, fg_color="#e35b52", hover_color="#f6756b", command=parameter_change)
        var_aplay_button.grid(row=4, column=2)
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
    
    anzahl = tk.IntVar(value=1000)
    binsC = tk.IntVar(value=10)
    seed = tk.StringVar(value="123")
    dreiD = tk.BooleanVar(value=False)
    a = tk.StringVar(value="0")
    b = tk.StringVar(value="0")
    c = tk.StringVar(value="0")

    tab.grid_rowconfigure(tuple(range(2)), weight=1)
    tab.grid_columnconfigure(tuple(range(2)), weight=1)

    global XOR_Generator
    XOR_Generator = XOR_Shift_Generator_64Bit(int(seed.get()))
    values = np.array([XOR_Generator.random() for _ in range(5000)])
    global values_for_diagrams
    values_for_diagrams = np.array(values[:anzahl.get()])

    titel = ct.CTkLabel(tab, text="XOR Shift Generator 64Bit", font=("Roboto", 30))
    titel.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=20)

    algo_frame = ct.CTkFrame(tab, border_color="#29c429")
    algo_frame.grid(row=2, column=1, sticky="nsew", pady=20)
    seed_shift_viusal()

    histogram_frame = ct.CTkFrame(tab)
    histogram_frame.grid(row=1, column = 0, sticky="nsew", padx=20, pady= 20)
    setup_histogram()

    scatter_frame = ct.CTkFrame(tab)
    scatter_frame.grid(row=2, column = 0, sticky="nsew", padx=20,pady=20)
    setup_scatter()

    control_frame = ct.CTkFrame(tab)
    control_frame.grid(row=1, column=1, sticky="nsew", pady=20)
    setup_controls()
