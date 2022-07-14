import tkinter as tk
import controls_menu as clm
import controls_game_long_functions as clglf

"""Основной код"""
win = tk.Tk()
win.geometry('550x550')  
win.title('tic-tac-toe')
clm.image_output()
clglf.inserting_a_language()
clglf.checking_the_language()
clm.start_menu(win)



tk.mainloop()