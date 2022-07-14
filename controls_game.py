import tkinter as tk
import variables as vb
import controls_game_long_functions as clglf
from controls_game_long_functions import MyThread

def test(win):
    btn_ff = tk.Button(win, text='fff', command= lambda : vb.lbl_fon_game.destroy())
    btn_ff.place(x=10, y= 10)

def start_game(root): # загрузка игры не пихай сюда проверки! 
    vb.lbl_fon_menu.destroy()
    vb.btn_menu_start.destroy()
    vb.btn_menu_options.destroy()
    vb.btn_menu_exit.destroy()

    vb.lbl_fon_game = tk.Label(root, image=vb.fon_game)
    vb.lbl_fon_game.place(x=0, y=0)


    clglf.round_and_score(root)
    clglf.init_the_main_buttons(root)
    if vb.max_seconds != 16:
        clglf.seconds_in_game(root)
        MyThread('поток', lambda : clglf.win_time(root)).start()
    

def creating_images(root, button_active=int): #Создание картинок все проверки сюда!
    if vb.motion % 2 != 0:
        photo = vb.x_image
        vb.motion += 1
    elif vb.motion % 2 == 0:
        photo = vb.o_image
        vb.motion += 1
    
    clglf.button_click_verification(button_active=button_active)
    clglf.drawing_an_image(root, photo, button_active=button_active)
    clglf.checking_for_winnings(root)















    
