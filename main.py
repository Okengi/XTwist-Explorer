import customtkinter as ct
from LCG_tab_setup import set_up_LCG_tab
from mt_tab import set_up_mt_tab


ct.set_appearance_mode("Dark") 
ct.set_default_color_theme("green")

window = ct.CTk()
window.title("Zufallszahlen")
window.geometry("1500x800")


tab_view = ct.CTkTabview(window)
tab_view.pack(fill='both', expand=True)
tab_view.add("LCG")
tab_view.add("Mersenne Twister")


LCG_tab = ct.CTkFrame(tab_view.tab("LCG"))
LCG_tab.pack()
set_up_LCG_tab(LCG_tab)  

MT_tab = ct.CTkFrame(tab_view.tab("Mersenne Twister"))
MT_tab.pack()
set_up_mt_tab(MT_tab)  

# Vergleich_tab = ttk.Frame(tabs_controller)
# tabs_controller.add(Vergleich_tab, text="Vergleich")
# set_up_Vergleich_tab(Vergleich_tab)  # Import the setup function for Vergleich

window.mainloop()