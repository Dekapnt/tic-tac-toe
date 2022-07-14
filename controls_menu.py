import tkinter as tk
import variables as vb
from controls_game import start_game
from controls_game_long_functions import checking_the_language, save_language, round_and_seconds, inserting_a_language
from controls_game_long_functions import MyThread
import time

#ПЕРЕВДЕНО

"""функции из меню"""

def save(root): #дополнение screen_resolution
    for i in vb.listbox.curselection():
        vb.selected_screen_resolution = vb.listbox.get(i)

    if vb.selected_screen_resolution == '':
        file = open('C:\Работы программирование\не законченые работы\X_0\данные.txt', 'r')
        vb.selected_screen_resolution = file.read(7)
        file.close()
        

    if vb.selected_screen_resolution == 'Русский' or 'English':
        vb.language = vb.selected_screen_resolution 
    
    checking_the_language()
    vb.lbl_listbox.destroy()
    vb.btn_back.destroy()
    vb.btn_save_listbox.destroy()
    vb.lbl_text_max_round.destroy()
    vb.lbl_text_round.destroy()
    vb.btn_min_number_round.destroy()
    vb.btn_max_number_round.destroy()
    vb.lbl_text_seconds.destroy() 
    vb.lbl_text_max_seconds.destroy()
    vb.btn_min_number_seconds.destroy()
    vb.btn_max_number_seconds.destroy()

    vb.btn_back = tk.Button(root, text=vb.back_language, font=('Helvetica', 12), command = lambda : back(root), bg='#87cefa')
    vb.btn_back.place(x=5, y=5)#кнопка выйти

    vb.lbl_listbox = tk.Label(root, text=vb.text_language, font=('Helvetica', 12), bg='#87cefa')
    vb.lbl_listbox.place(x=vb.listbox_lbl_x, y=vb.listbox_lbl_y, width=125)#текст

    vb.btn_save_listbox = tk.Button(root, text=vb.save_language, bg='#87cefa', font=('Helvetica', 12), command= lambda : save(root))
    vb.btn_save_listbox.place(x=vb.listbox_save_x, y=vb.listbox_save_y)#кнопка сохранить

    round_and_seconds(root)

    save_language()


def delete(win):
    vb.lbl_fon_menu.destroy()
    start_menu(win)
    vb.listbox.destroy()
    vb.lbl_listbox.destroy()
    vb.btn_save_listbox.destroy()
    vb.btn_back.destroy()
    vb.lbl_text_max_round.destroy()
    vb.lbl_text_round.destroy()
    vb.btn_min_number_round.destroy()
    vb.btn_max_number_round.destroy()
    vb.lbl_text_seconds.destroy() 
    vb.lbl_text_max_seconds.destroy()
    vb.btn_min_number_seconds.destroy()
    vb.btn_max_number_seconds.destroy()
    

    
    
    


def back(win): #дополнение screen_resolution
    MyThread('Potok', lambda : delete(win)).start()
    
    

    



def screen_resolution(root):
    inserting_a_language()
    vb.listbox = tk.Listbox(root, height=2, selectmode= tk.SINGLE, font=('Helvetica', 13), bg='#87cefa')
    vb.listbox.insert(1, 'English')
    vb.listbox.insert(2, 'Русский')
    vb.listbox.place(x=vb.listbox_x, y=vb.listbox_y, width=vb.listbox_width)

    vb.lbl_listbox = tk.Label(root, text=vb.text_language, font=('Helvetica', 12), bg='#87cefa')
    vb.lbl_listbox.place(x=vb.listbox_lbl_x, y=vb.listbox_lbl_y, width=125)#текст

    vb.btn_save_listbox = tk.Button(root, text=vb.save_language, bg='#87cefa', font=('Helvetica', 12), command= lambda : save(root))
    vb.btn_save_listbox.place(x=vb.listbox_save_x, y=vb.listbox_save_y)#кнопка сохранить

    vb.btn_back = tk.Button(root, text=vb.back_language, font=('Helvetica', 12), command = lambda : back(root), bg='#87cefa')
    vb.btn_back.place(x=5, y=5)#кнопка выйти

    round_and_seconds(root)

    vb.btn_menu_start.destroy()
    vb.btn_menu_options.destroy()
    vb.btn_menu_exit.destroy()

def test(win):
    btn_ff = tk.Button(win, text='fff', command= lambda : vb.lbl_fon_menu.destroy())
    btn_ff.place(x=400, y= 100)


def start_menu(win):
    vb.lbl_fon_menu = tk.Label(win, image=vb.fon_menu)
    vb.lbl_fon_menu.place(x=0, y=0)

    vb.btn_menu_start = tk.Button(win, text=vb.start_game_language, bg='#87cefa', fg='black', font=("Helvetica", 13), command= lambda : start_game(win))
    vb.btn_menu_start.place(x=vb.start_btn_x, y=vb.start_btn_y, width=vb.start_btn_width)

    vb.btn_menu_options = tk.Button(win, text=vb.options_language, bg='#87cefa', fg='black', font=("Helvetica", 13), command= lambda : screen_resolution(win))
    vb.btn_menu_options.place(x=vb.options_btn_x, y=vb.options_btn_y, width=vb.options_btn_width)

    vb.btn_menu_exit = tk.Button(win, text=vb.exit_language, bg='#87cefa', fg='black', font=("Helvetica", 13), command=win.destroy)
    vb.btn_menu_exit.place(x=vb.exit_btn_x, y=vb.exit_btn_y, width=vb.exit_btn_width)

    




def image_output(): 
    vb.fon_menu = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\fon_menu.png')
    vb.fon_game = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\fon_game.png')
    vb.x_image = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x.png')
    vb.o_image = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o.png')
    vb.img_win_1_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_1_we.png') 
    vb.img_win_2_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_2_we.png')
    vb.img_win_3_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_3_we.png')
    vb.img_win_4_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_1_ns.png') 
    vb.img_win_5_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_4_ns.png')
    vb.img_win_6_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_7_ns.png')
    vb.img_win_7_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_3_ne.png')
    vb.img_win_8_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_5_ne.png')
    vb.img_win_9_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_7_ne.png')
    vb.img_win_10_x  = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_1_nw.png')
    vb.img_win_11_x  = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_5_nw.png')
    vb.img_win_12_x  = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_9_nw.png')

    vb.img_win_1_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_1_we.png') 
    vb.img_win_2_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_2_we.png')
    vb.img_win_3_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_3_we.png')
    vb.img_win_4_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_1_ns.png') 
    vb.img_win_5_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_4_ns.png')
    vb.img_win_6_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_7_ns.png')
    vb.img_win_7_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_3_ne.png')
    vb.img_win_8_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_5_ne.png')
    vb.img_win_9_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_7_ne.png')
    vb.img_win_10_o  = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_1_nw.png')
    vb.img_win_11_o  = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_5_nw.png')
    vb.img_win_12_o  = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_9_nw.png')

    vb.win_text_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\text_win_x.png')
    vb.win_text_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\text_win_o.png')
    vb.win_text_draw = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\text_win_draw.png')

    vb.mini_x = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\x_50.png')
    vb.mini_o = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\o_50.png')

    vb.img_WIN_DRAW = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\fon_game_WIN_DRAW.png')
    vb.img_WIN_O = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\fon_game_WIN_O.png')
    vb.img_WIN_X = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\fon_game_WIN_X.png')

    vb.pahalka = tk.PhotoImage(file = r'C:\Работы программирование\не законченые работы\X_0\images\fon_1.png')

    


