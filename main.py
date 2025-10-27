import customtkinter as ct
from LCG_tab_setup import set_up_LCG_tab
from mt_tab import set_up_mt_tab
from xor_tab import setup_xor_shift_tab

ct.set_appearance_mode("Dark") 
ct.set_default_color_theme("green")

window = ct.CTk()
window.title("XTwist Explorer")
window.geometry("1500x800")

tab_view = ct.CTkTabview(window, segmented_button_selected_color="#e35b52", segmented_button_selected_hover_color="#783e3a")
tab_view.pack(fill='both', expand=True)
#tab_view.add("Mersenne Twister")
#tab_view.add("LCG")
tab_view.add("XOR Shift")

try: 
    tab_view.tab("LCG")
    lcg = True
except:
    print("No LCG Tab")
    lcg = False

if lcg:
    LCG_tab = ct.CTkFrame(tab_view.tab("LCG"))
    LCG_tab.pack()
    set_up_LCG_tab(LCG_tab)  

try:
    tab_view.tab("Mersenne Twister")
    mt = True
except Exception as e:
    print("No Mersenne Twister Tab:", e)
    mt = False

if mt:
    MT_tab = ct.CTkFrame(tab_view.tab("Mersenne Twister"))
    MT_tab.pack()
    set_up_mt_tab(MT_tab)



try:
    tab_view.tab("XOR Shift")
    xor = True
except Exception as e:
    print("No XOR Shift Tab:", e)
    xor = False

if xor:
    XOR_tab = ct.CTkFrame(tab_view.tab("XOR Shift"))
    XOR_tab.pack()
    setup_xor_shift_tab(XOR_tab)

window.mainloop()