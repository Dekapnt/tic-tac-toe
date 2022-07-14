import variables as vb
import tkinter as tk
from threading import Thread
import time
import webbrowser as wb
import time

class MyThread(Thread):
    def __init__(self, name, f):
        Thread.__init__(self)
        self.name = name
        self.f = f

    def run(self):
        self.f()



def init_the_main_buttons(root):
    from controls_game import creating_images
    vb.btn_game_1 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white', 
                    command= lambda : creating_images(root, button_active=1))

    vb.btn_game_2 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white',
                    command= lambda : creating_images(root, button_active=2))

    vb.btn_game_3 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white',
                    command= lambda : creating_images(root, button_active=3))

    vb.btn_game_4 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white',
                    command= lambda : creating_images(root, button_active=4))

    vb.btn_game_5 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white',
                    command= lambda : creating_images(root, button_active=5))

    vb.btn_game_6 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white',
                    command= lambda : creating_images(root, button_active=6))

    vb.btn_game_7 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white',
                    command= lambda : creating_images(root, button_active=7))

    vb.btn_game_8 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white',
                    command= lambda : creating_images(root, button_active=8))

    vb.btn_game_9 = tk.Button(root, bg='white', fg='white',
                    activebackground='white', activeforeground='white',
                    command= lambda : creating_images(root, button_active=9))

    vb.btn_game_1.place(x=130, y=130, width=100, height=100)
    vb.btn_game_2.place(x=230, y=130, width=100, height=100)
    vb.btn_game_3.place(x=330, y=130, width=100, height=100)
    vb.btn_game_4.place(x=130, y=230, width=100, height=100)
    vb.btn_game_5.place(x=230, y=230, width=100, height=100)
    vb.btn_game_6.place(x=330, y=230, width=100, height=100)
    vb.btn_game_7.place(x=130, y=330, width=100, height=100)
    vb.btn_game_8.place(x=230, y=330, width=100, height=100)
    vb.btn_game_9.place(x=330, y=330, width=100, height=100)

    vb.pashalka = tk.Button(root, text='М ты нашел\n пасхалку!', command = pahalrf)  #удали перед выгрузкой на сайт
    vb.pashalka.place(x=0, y=560)


def button_click_verification(button_active=int):
    if button_active == 1:
        if vb.motion % 2 == 0:
            vb.x_1 = True
            
        elif vb.motion % 2 != 0:
            vb.o_1 = True

    elif button_active == 2:
        if vb.motion % 2 == 0:
            vb.x_2 = True
            
        elif vb.motion % 2 != 0:
            vb.o_2 = True

    elif button_active == 3:
        if vb.motion % 2 == 0:
            vb.x_3 = True
            
        elif vb.motion % 2 != 0:
            vb.o_3 = True

    elif button_active == 4:
        if vb.motion % 2 == 0:
            vb.x_4 = True
            
        elif vb.motion % 2 != 0:
            vb.o_4 = True
    
    elif button_active == 5:
        if vb.motion % 2 == 0:
            vb.x_5 = True
            
        elif vb.motion % 2 != 0:
            vb.o_5 = True

    elif button_active == 6:
        if vb.motion % 2 == 0:
            vb.x_6 = True
            
        elif vb.motion % 2 != 0:
            vb.o_6 = True

    elif button_active == 7:
        if vb.motion % 2 == 0:
            vb.x_7 = True
            
        elif vb.motion % 2 != 0:
            vb.o_7 = True

    elif button_active == 8:
        if vb.motion % 2 == 0:
            vb.x_8 = True
            
        elif vb.motion % 2 != 0:
            vb.o_8 = True

    elif button_active == 9:
        if vb.motion % 2 == 0:
            vb.x_9 = True
            
        elif vb.motion % 2 != 0:
            vb.o_9 = True


def drawing_an_image(root, photo, button_active=int):
    if vb.stop_create_image != True:
        if button_active == 1:
            vb.lbl_image_1 = tk.Label(root, image=photo)
            vb.lbl_image_1.place(x=130, y=130, width=100, height=100)

        elif button_active == 2:
            vb.lbl_image_2 = tk.Label(root, image=photo)
            vb.lbl_image_2.place(x=230, y=130, width=100, height=100)


        elif button_active == 3:
            vb.lbl_image_3 = tk.Label(root, image=photo)
            vb.lbl_image_3.place(x=330, y=130, width=100, height=100)

            
        elif button_active == 4:
            vb.lbl_image_4 = tk.Label(root, image=photo)
            vb.lbl_image_4.place(x=130, y=230, width=100, height=100)
            
        elif button_active == 5:
            vb.lbl_image_5 = tk.Label(root, image=photo)
            vb.lbl_image_5.place(x=230, y=230, width=100, height=100)

        elif button_active == 6:
            vb.lbl_image_6 = tk.Label(root, image=photo)
            vb.lbl_image_6.place(x=330, y=230, width=100, height=100)

        elif button_active == 7:
            vb.lbl_image_7 = tk.Label(root, image=photo)
            vb.lbl_image_7.place(x=130, y=330, width=100, height=100)

        elif button_active == 8:
            vb.lbl_image_8 = tk.Label(root, image=photo)
            vb.lbl_image_8.place(x=230, y=330, width=100, height=100)

        elif button_active == 9:
            vb.lbl_image_9 = tk.Label(root, image=photo)
            vb.lbl_image_9.place(x=330, y=330, width=100, height=100)

def creating_a_win(root, im_1=str, im_2=str, im_3=str, x_1=int, x_2=int, x_3=int, y_1=int, y_2=int, y_3=int):
    photo_1 = im_1
    photo_2 = im_2
    photo_3 = im_3
    vb.lbl_image_win_1 = tk.Label(root, image=photo_1)
    vb.lbl_image_win_2 = tk.Label(root, image=photo_2)
    vb.lbl_image_win_3 = tk.Label(root, image=photo_3)
    vb.lbl_image_win_1.place(x=x_1, y=y_1, width=100, height=100)
    vb.lbl_image_win_2.place(x=x_2, y=y_2, width=100, height=100)
    vb.lbl_image_win_3.place(x=x_3, y=y_3, width=100, height=100)


def destroy_image():
    if vb.lbl_image_1 != '':
        vb.lbl_image_1.destroy()
    if vb.lbl_image_2 != '':
        vb.lbl_image_2.destroy()
    if vb.lbl_image_3 != '':
        vb.lbl_image_3.destroy()
    if vb.lbl_image_4 != '':
        vb.lbl_image_4.destroy()
    if vb.lbl_image_5 != '':
        vb.lbl_image_5.destroy()
    if vb.lbl_image_6 != '':
        vb.lbl_image_6.destroy()
    if vb.lbl_image_7 != '':
        vb.lbl_image_7.destroy()
    if vb.lbl_image_8 != '':
        vb.lbl_image_8.destroy()
    if vb.lbl_image_9 != '':
        vb.lbl_image_9.destroy()



def checking_the_number():
    if vb.score_x > vb.score_o:
        photo = vb.img_WIN_X
        return photo
    elif vb.score_x < vb.score_o:
        photo = vb.img_WIN_O
        return photo
    elif vb.score_x == vb.score_o: 
        photo = vb.img_WIN_DRAW
        return photo




#; vb.btn_game_2.destroy(); vb.btn_game_3.destroy(); vb.btn_game_4.destroy(); vb.btn_game_5.destroy(); vb.btn_game_6.destroy(); vb.btn_game_7.destroy(); vb.btn_game_8.destroy(); vb.btn_game_9.destroy()
def reset(root, mode=False):
    from controls_game import start_game
    from controls_menu import start_menu
    vb.lbl_win_fon.destroy()
    vb.btn_reset.destroy()
    vb.btn_exit.destroy()
    vb.btn_exit_menu.destroy()
    if vb.no_delete_image != True and vb.out_of_time != True:
        vb.lbl_image_win_1.destroy(); vb.lbl_image_win_2.destroy(); vb.lbl_image_win_3.destroy()
    destroy_image()
    vb.stop_create_image = False
    vb.lbl_fon_game.destroy()
    vb.lbl_fon_menu.destroy()
    vb.motion = 1
    vb.x_1 = False; vb.o_1 = False; vb.x_2 = False; vb.o_2 = False; vb.x_3 = False; vb.o_3 = False; vb.x_4 = False; vb.o_4 = False; vb.x_5 = False
    vb.o_5 = False; vb.x_6 = False; vb.o_6 = False; vb.x_7 = False; vb.o_7 = False; vb.x_8 = False; vb.o_8 = False; vb.x_9 = False; vb.o_9 = False
    vb.lbl_round_text.destroy()
    vb.lbl_score_text_x.destroy()
    vb.lbl_text_p_1.destroy()
    vb.lbl_text_p_2.destroy()
    vb.lbl_text_p_1_game.destroy()
    vb.lbl_text_p_2_game.destroy()
    vb.lbl_score_text_mini_o.destroy()
    vb.lbl_score_text_mini_x.destroy()
    vb.lbl_score_text.destroy()
    vb.stop_seconds_in_game = False

    vb.lbl_fon_menu.destroy()

    if mode == False:
        destroy_btn()
        start_game(root)
        vb.seconds = int(str(vb.max_seconds) + '0' + '0')
        
        
    elif mode == True:
        destroy_btn()
        start_menu(root)
        vb.number_reset = 0
        vb.score_x = 0
        vb.score_o = 0
        vb.number_round = 1
        vb.seconds = int(str(vb.max_seconds) + '0' + '0')

def destroy_btn():
    if vb.btn_game_1 != '':
        vb.btn_game_1.destroy()
    if vb.btn_game_2 != '':
        vb.btn_game_2.destroy()
    if vb.btn_game_3 != '':
        vb.btn_game_3.destroy()
    if vb.btn_game_4 != '':
        vb.btn_game_4.destroy()
    if vb.btn_game_5 != '':
        vb.btn_game_5.destroy()
    if vb.btn_game_6 != '':
        vb.btn_game_6.destroy()
    if vb.btn_game_7 != '':
        vb.btn_game_7.destroy()
    if vb.btn_game_8 != '':
        vb.btn_game_8.destroy()
    if vb.btn_game_9 != '':
        vb.btn_game_9.destroy()
          
    
    
    
    

    
def none():
    return None

def dele():
    vb.lbl_win_fon.destroy()
    vb.lbl_fon_game.destroy()
    print('f')

def test(win):
    btn_ff = tk.Button(win, text='fff', command = dele)
    btn_ff.place(x=10, y= 10)

def victori(root, x_or_o_or_draw, mode=False):  
    x_or_o_or_draw = x_or_o_or_draw.upper()
    if x_or_o_or_draw == 'X':
        photo = vb.win_text_x
    elif x_or_o_or_draw == 'O':
        photo = vb.win_text_o
    elif x_or_o_or_draw == 'DRAW':
        photo = vb.win_text_draw

    vb.btn_game_1.configure(command=none)
    vb.btn_game_2.configure(command=none)
    vb.btn_game_3.configure(command=none)
    vb.btn_game_4.configure(command=none)
    vb.btn_game_5.configure(command=none)
    vb.btn_game_6.configure(command=none)
    vb.btn_game_7.configure(command=none)
    vb.btn_game_8.configure(command=none)
    vb.btn_game_9.configure(command=none)

    


    time.sleep(1.5)

    vb.lbl_win_fon = tk.Label(root, image=photo)
    vb.lbl_win_fon.place(x=0, y=0)

    
    time.sleep(1)

    if mode == False:
        vb.btn_reset = tk.Button(root, text=vb.restart_language, bg='#87cefa', fg='black', font=('Helvetica', 15), command= lambda : reset(root))
        vb.btn_reset.place(x=95, y=340, width=115, height=40)
 
        vb.btn_exit = tk.Button(root, text = vb.exit_language, bg='#87cefa', fg='black', font=('Helvetica', 15), command= lambda : root.destroy())
        vb.btn_exit.place(x=220, y=340, width=100, height=40)
 
        vb.btn_exit_menu = tk.Button(root, text=vb.exit_to_menu, bg='#87cefa', fg='black', font=('Helvetica', 13), command= lambda : reset(root, mode=True))
        vb.btn_exit_menu.place(x=330, y=340, width=100, height=40)
 
        vb.lbl_text_p_1 = tk.Label(root, text='P1', bg='black', fg='#87cefa', font=('', 30))
        vb.lbl_text_p_1.place(x=185, y=180)
        vb.lbl_text_p_2 = tk.Label(root, text='P2', bg='black', fg='#87cefa', font=('', 30))
        vb.lbl_text_p_2.place(x=315, y=180)
 
        text_2 = str(vb.score_x) + ':' + str(vb.score_o)
        int(vb.score_x); int(vb.score_o)
        vb.lbl_score_text_x = tk.Label(root, text=text_2, bg='black', fg='#87cefa', font=('', 30))
        vb.lbl_score_text_x.place(x=235, y=180, height=50, width=80)

    elif mode == True:
        photo_2 = checking_the_number()
        vb.lbl_win_fon_2 = tk.Label(root, image=photo_2)
        vb.lbl_win_fon_2.place(x=0, y=0)

        vb.lbl_text_p_1 = tk.Label(root, text='P1', bg='black', fg='#87cefa', font=('', 30))
        vb.lbl_text_p_1.place(x=185, y=260, )
        vb.lbl_text_p_2 = tk.Label(root, text='P2', bg='black', fg='#87cefa', font=('', 30))
        vb.lbl_text_p_2.place(x=310, y=260)
 
        text_2 = str(vb.score_x) + ':' + str(vb.score_o)
        int(vb.score_x); int(vb.score_o)
        vb.lbl_score_text_x = tk.Label(root, text=text_2, bg='black', fg='#87cefa', font=('', 30))
        vb.lbl_score_text_x.place(x=245, y=260, height=50, width=60)

        vb.btn_exit_menu = tk.Button(root, text=vb.exit_to_menu, bg='#87cefa', fg='black', font=('Helvetica', 13), command= lambda : reset(root, mode=True))
        vb.btn_exit_menu.place(x=225, y=340, width=100, height=40)




def plus_score(x_or_o):
    if x_or_o == 'o':
        if vb.number_round % 2 != 0:
            vb.score_x += 1
        elif vb.number_round % 2 == 0:
            vb.score_o += 1
    if x_or_o == 'x':
        if vb.number_round % 2 != 0:
            vb.score_o += 1
        elif vb.number_round % 2 == 0:
            vb.score_x += 1

def win_time(root):
    while True:
        time.sleep(0.1)
        if vb.seconds == 0:
            if vb.motion % 2 != 0:
                vb.number_reset += 1
                if vb.max_round == 6:
                    MyThread('первый поток', lambda : victori(root, 'O')).start()
                elif vb.max_round == vb.number_reset:
                    MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
                else:
                    MyThread('первый поток', lambda : victori(root, 'O')).start()
                vb.out_of_time = True
                plus_score('o')
                print(vb.number_reset)
                break
            elif vb.motion % 2 == 0:
                vb.number_reset += 1
                if vb.max_round == 6:
                    MyThread('первый поток', lambda : victori(root, 'X')).start()
                elif vb.max_round == vb.number_reset:
                    MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
                else:
                    MyThread('первый поток', lambda : victori(root, 'X')).start()
                vb.out_of_time = True
                plus_score('x')
                print(vb.number_reset)
                break
        if vb.motion % 2 != 0:
            if vb.stop_assigning_values_2 == False:
                vb.seconds = int(str(vb.max_seconds) + '0' + '0')
                vb.stop_assigning_values_2 = True
                vb.stop_assigning_values_3 = False
        elif vb.motion % 2 == 0:
            if vb.stop_assigning_values_3 == False:
                vb.seconds = int(str(vb.max_seconds) + '0' + '0')
                vb.stop_assigning_values_3 = True
                vb.stop_assigning_values_2 = False
            



def checking_for_winnings(root):
    vb.max_round = int(vb.max_round)
    if vb.x_1 and vb.x_2 and vb.x_3:
        creating_a_win(root, im_1=vb.img_win_1_x, im_2=vb.img_win_2_x, im_3=vb.img_win_3_x, x_1=130, x_2=230, x_3=330, y_1=130, y_2=129, y_3=130)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('x')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        
    elif vb.x_4 and vb.x_5 and vb.x_6:
        creating_a_win(root, im_1=vb.img_win_1_x, im_2=vb.img_win_2_x, im_3=vb.img_win_3_x, x_1=130, x_2=230, x_3=330, y_1=230, y_2=229, y_3=230)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('x')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        
    elif vb.x_7 and vb.x_8 and vb.x_9:
        creating_a_win(root, im_1=vb.img_win_1_x, im_2=vb.img_win_2_x, im_3=vb.img_win_3_x, x_1=130, x_2=230, x_3=330, y_1=330, y_2=329, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('x')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        
    elif vb.x_1 and vb.x_4 and vb.x_7:
        creating_a_win(root, im_1=vb.img_win_4_x, im_2=vb.img_win_5_x, im_3=vb.img_win_6_x, x_1=130, x_2=129, x_3=130, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('x')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        
    elif vb.x_2 and vb.x_5 and vb.x_8:
        creating_a_win(root, im_1=vb.img_win_4_x, im_2=vb.img_win_5_x, im_3=vb.img_win_6_x, x_1=230, x_2=229, x_3=230, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('x')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        
    elif vb.x_3 and vb.x_6 and vb.x_9:
        creating_a_win(root, im_1=vb.img_win_4_x, im_2=vb.img_win_5_x, im_3=vb.img_win_6_x, x_1=330, x_2=329, x_3=330, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('x')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        
    elif vb.x_1 and vb.x_5 and vb.x_9:
        creating_a_win(root, im_1=vb.img_win_10_x, im_2=vb.img_win_11_x, im_3=vb.img_win_12_x, x_1=130, x_2=230, x_3=330, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('x')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        
    elif vb.x_3 and vb.x_5 and vb.x_7:
        creating_a_win(root, im_1=vb.img_win_7_x, im_2=vb.img_win_8_x, im_3=vb.img_win_9_x, x_1=330, x_2=230, x_3=130, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('x')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'X', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'X')).start()
        


    elif vb.o_1 and vb.o_2 and vb.o_3:
        creating_a_win(root, im_1=vb.img_win_1_o, im_2=vb.img_win_2_o, im_3=vb.img_win_3_o, x_1=130, x_2=230, x_3=330, y_1=130, y_2=130, y_3=130)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('o')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        
    elif vb.o_4 and vb.o_5 and vb.o_6:
        creating_a_win(root, im_1=vb.img_win_1_o, im_2=vb.img_win_2_o, im_3=vb.img_win_3_o, x_1=130, x_2=230, x_3=330, y_1=230, y_2=230, y_3=230)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('o')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        
    elif vb.o_7 and vb.o_8 and vb.o_9:
        creating_a_win(root, im_1=vb.img_win_1_o, im_2=vb.img_win_2_o, im_3=vb.img_win_3_o, x_1=130, x_2=230, x_3=330, y_1=330, y_2=330, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('o')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        
    elif vb.o_1 and vb.o_4 and vb.o_7:
        creating_a_win(root, im_1=vb.img_win_4_o, im_2=vb.img_win_5_o, im_3=vb.img_win_6_o, x_1=130, x_2=130, x_3=130, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('o')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        
    elif vb.o_2 and vb.o_5 and vb.o_8:
        creating_a_win(root, im_1=vb.img_win_4_o, im_2=vb.img_win_5_o, im_3=vb.img_win_6_o, x_1=230, x_2=230, x_3=230, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('o')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        
    elif vb.o_3 and vb.o_6 and vb.o_9:
        creating_a_win(root, im_1=vb.img_win_4_o, im_2=vb.img_win_5_o, im_3=vb.img_win_6_o, x_1=330, x_2=330, x_3=330, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('o')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        
    elif vb.o_1 and vb.o_5 and vb.o_9:
        creating_a_win(root, im_1=vb.img_win_10_o, im_2=vb.img_win_11_o, im_3=vb.img_win_12_o, x_1=130, x_2=230, x_3=330, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('o')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        
    elif vb.o_3 and vb.o_5 and vb.o_7:
        creating_a_win(root, im_1=vb.img_win_7_o, im_2=vb.img_win_8_o, im_3=vb.img_win_9_o, x_1=330, x_2=230, x_3=130, y_1=130, y_2=230, y_3=330)
        vb.number_reset += 1
        vb.stop_create_image = True
        vb.stop_seconds_in_game = True
        plus_score('o')
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'O', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'O')).start()
            


    elif vb.motion == 10:
        vb.stop_create_image = True
        vb.no_delete_image = True
        vb.stop_seconds_in_game = True
        vb.number_reset += 1
        if vb.max_round == 6:
            MyThread('первый поток', lambda : victori(root, 'draw')).start()
        elif vb.max_round == vb.number_reset:
            MyThread('первый поток', lambda : victori(root, 'draw', mode=True)).start()
        else:
            MyThread('первый поток', lambda : victori(root, 'draw')).start()


def pahalrf():
    wb.open('https://t.me/meynerSyOVu')


def checking_the_language():
    if vb.language == 'English':
        vb.text_language = 'Language'
        vb.save_language = 'Save'
        vb.back_language = 'Back'
        vb.start_game_language = 'Start game'
        vb.options_language = 'Options'
        vb.exit_language = 'Exit'
        vb.restart_language = 'Continue'
        vb.exit_to_menu = 'Exit to\nmenu'
        vb.listbox_save_x = 500
        vb.round_language = 'Round '
        vb.round_option = 'Number of rounds'
        vb.seconds_option = 'Number of seconds'
    elif vb.language == 'Русский':
        vb.text_language = 'Язык'
        vb.save_language = 'Cохраить'
        vb.back_language = 'Назад'
        vb.start_game_language = 'Начать игру'
        vb.options_language = 'Настройки'
        vb.exit_language = 'Выход'
        vb.restart_language = 'Продолжить'
        vb.exit_to_menu = 'Выход в\nменю'
        vb.listbox_save_x = 460
        vb.round_language = 'Раунд '
        vb.round_option = 'Количество раундов'
        vb.seconds_option = 'Количество секунд'


def save_language():
    file = open('C:\Работы программирование\не законченые работы\X_0\данные.txt', 'w')
    file.write(vb.language)
    file.close()

    file_2 = open('C:\Работы программирование\не законченые работы\X_0\раунды и секунды.txt', 'w')
    file_2.write(str(vb.max_round))
    vb.max_round = int(vb.max_round)
    file_2.write(str(vb.max_seconds))
    vb.max_seconds = int(vb.max_seconds)
    file_2.close()
    
    

def inserting_a_language():
    file = open('C:\Работы программирование\не законченые работы\X_0\данные.txt', 'r')
    vb.language = file.read(7)
    file.close()

    file_2 = open('C:\Работы программирование\не законченые работы\X_0\раунды и секунды.txt', 'r')
    vb.max_round = int(file_2.read(1))
    vb.max_seconds = int(file_2.read())
    file_2.close()


def round_and_score(root):
    text = vb.round_language + str(vb.number_round)
    int(vb.number_round)
    vb.lbl_round_text = tk.Label(root, text=text, font=('', 40), bg= 'black', fg='#87cefa')
    vb.lbl_round_text.place(x=175, y=2, width=230)

    vb.lbl_text_p_1_game = tk.Label(root, text='P1', bg='black', fg='#87cefa', font=('', 11))
    vb.lbl_text_p_1_game.place(x=95, y=60)
    vb.lbl_text_p_2_game = tk.Label(root, text='P2', bg='black', fg='#87cefa', font=('', 11))
    vb.lbl_text_p_2_game.place(x=125, y=60)

    if vb.number_round % 2 != 0:
        vb.lbl_score_text_mini_x = tk.Label(root, image=vb.mini_x)
        vb.lbl_score_text_mini_x.place(x=30, y=80, width=50, height=50)
        text_2 = str(vb.score_x) + ':' + str(vb.score_o)
        int(vb.score_x); int(vb.score_o)
        vb.lbl_score_text = tk.Label(root, text=text_2, bg='black', fg='#87cefa', font=('', 30))
        vb.lbl_score_text.place(x=80, y=80, height=50, width=80)
        vb.lbl_score_text_mini_o = tk.Label(root, image=vb.mini_o)
        vb.lbl_score_text_mini_o.place(x=160, y=80, width=50, height=50)

    elif vb.number_round % 2 == 0:
        vb.lbl_score_text_mini_o = tk.Label(root, image=vb.mini_o)
        vb.lbl_score_text_mini_o.place(x=30, y=80, width=50, height=50)
        text_2 = str(vb.score_x) + ':' + str(vb.score_o)
        int(vb.score_x); int(vb.score_o)
        vb.lbl_score_text = tk.Label(root, text=text_2, bg='black', fg='#87cefa', font=('', 30))
        vb.lbl_score_text.place(x=80, y=80, height=50, width=80)
        vb.lbl_score_text_mini_x = tk.Label(root, image=vb.mini_x)
        vb.lbl_score_text_mini_x.place(x=160, y=80, width=50, height=50)


    vb.number_round += 1

def min_text_round(root):        
    vb.lbl_text_max_round.destroy()
    if vb.max_round != 1:
        vb.max_round -= 1
    vb.lbl_text_max_round = tk.Label(root, text=vb.max_round, font=('Helvetica', 14), bg='#87cefa')
    vb.lbl_text_max_round.place(x=245, y=240, height=25, width=50)
    
def min_text_seconds(root):
    vb.lbl_text_max_seconds.destroy()
    if vb.max_seconds != 1:
        vb.max_seconds -= 1
    vb.lbl_text_max_round = tk.Label(root, text=vb.max_seconds, font=('Helvetica', 14), bg='#87cefa')
    vb.lbl_text_max_round.place(x=245, y=290, height=25, width=50)



def max_text_round(root):
    if vb.max_round != 5 and vb.max_round != 6:
        #vb.lbl_text_max_round.destroy()
        vb.max_round += 1
        vb.lbl_text_max_round = tk.Label(root, text=vb.max_round, font=('Helvetica', 14), bg='#87cefa')
        vb.lbl_text_max_round.place(x=245, y=240, height=25, width=50)
    elif vb.max_round == 5:
        vb.lbl_text_max_round.destroy()
        if vb.max_round == 5:
            vb.max_round += 1
        vb.lbl_text_max_round = tk.Label(root, text='∞', font=('Helvetica', 14), bg='#87cefa')
        vb.lbl_text_max_round.place(x=245, y=240, height=25, width=50)
        
def max_text_seconds(root):
    if vb.max_seconds != 15 and vb.max_seconds != 16:
        vb.lbl_text_max_seconds.destroy()
        vb.max_seconds += 1
        vb.lbl_text_max_seconds = tk.Label(root, text=vb.max_seconds, font=('Helvetica', 14), bg='#87cefa')
        vb.lbl_text_max_seconds.place(x=245, y=290, height=25, width=50)
    elif vb.max_seconds == 15:
        vb.lbl_text_max_seconds.destroy()
        if vb.max_seconds == 15:
            vb.max_seconds += 1
        vb.lbl_text_max_seconds = tk.Label(root, text='∞', font=('Helvetica', 14), bg='#87cefa')
        vb.lbl_text_max_seconds.place(x=245, y=290, height=25, width=50)


def round_and_seconds(root):
    #раунды
    vb.max_round = int(vb.max_round)
    vb.lbl_text_round = tk.Label(root, text=vb.round_option, font=('Helvetica', 12), bg='#87cefa')
    vb.lbl_text_round.place(x=40, y=240, width=170, height=25)

    if vb.max_round != 6:
        vb.lbl_text_max_round = tk.Label(root, text=vb.max_round, font=('Helvetica', 14), bg='#87cefa')
        vb.lbl_text_max_round.place(x=245, y=240, height=25, width=50)
    elif vb.max_round == 6:
        vb.lbl_text_max_round = tk.Label(root, text='∞', font=('Helvetica', 14), bg='#87cefa')
        vb.lbl_text_max_round.place(x=245, y=240, height=25, width=50)

    vb.btn_min_number_round = tk.Button(root, text='-', bg='#87cefa', font=('Helvetica', 16), command = lambda : min_text_round(root))
    vb.btn_min_number_round.place(x=215, y=240, height=25, width=25)

    vb.btn_max_number_round = tk.Button(root, text='+', bg='#87cefa', font=('Helvetica', 16), command = lambda : max_text_round(root))
    vb.btn_max_number_round.place(x=300, y=240, height=25, width=25)

    #секунды

    vb.max_seconds = int(vb.max_seconds)
    vb.lbl_text_seconds = tk.Label(root, text=vb.seconds_option, font=('Helvetica', 12), bg='#87cefa')
    vb.lbl_text_seconds.place(x=40, y=290, width=170, height=25)

    if vb.max_seconds != 16:
        vb.lbl_text_max_seconds = tk.Label(root, text=vb.max_seconds, font=('Helvetica', 14), bg='#87cefa')
        vb.lbl_text_max_seconds.place(x=245, y=290, height=25, width=50)
    elif vb.max_seconds == 16:
        vb.lbl_text_max_seconds = tk.Label(root, text='∞', font=('Helvetica', 14), bg='#87cefa')
        vb.lbl_text_max_seconds.place(x=245, y=290, height=25, width=50)

    vb.btn_min_number_seconds = tk.Button(root, text='-', bg='#87cefa', font=('Helvetica', 16), command = lambda : min_text_seconds(root))
    vb.btn_min_number_seconds.place(x=215, y=290, height=25, width=25)

    vb.btn_max_number_seconds = tk.Button(root, text='+', bg='#87cefa', font=('Helvetica', 16), command = lambda : max_text_seconds(root))
    vb.btn_max_number_seconds.place(x=300, y=290, height=25, width=25)

def min_seconds(root):
    
    text = str(vb.seconds)# + ':' + str(vb.milliseconds)
    int(vb.seconds); int(vb.milliseconds)
    vb.lbl_seconds_game = tk.Label(root, text=text, font=('', 40), bg= 'black', fg='#87cefa')
    vb.lbl_seconds_game.place(x=425, y= 80, width=125, height=50)

'''def min_milliseconds():
    if vb.milliseconds == 0:
        vb.milliseconds == 99
    vb.milliseconds -= 1
    
    after(10, min_milliseconds)'''

def seconds_in_game(root):
    if vb.stop_seconds_in_game != True:
        if vb.stop_assigning_values == False:
            vb.seconds = vb.max_seconds
            vb.stop_assigning_values = True
            vb.seconds = int(str(vb.seconds) + '0' + '0')
        vb.seconds = int(vb.seconds) - 1
        if len(str(vb.seconds)) == 4:
            text = str(vb.seconds)[:2] + ':' + str(vb.seconds)[2:]
        elif len(str(vb.seconds)) == 3:
            text = str(vb.seconds)[0] + ':' + str(vb.seconds)[1:]
        elif len(str(vb.seconds)) == 2:
            text = '0' + ':' + str(vb.seconds)[0:]
        elif len(str(vb.seconds)) == 1:
            text = '0' + ':' + '0' + str(vb.seconds)[0:]
        vb.lbl_seconds_game = tk.Label(root, text=text, font=('', 40), bg= 'black', fg='#87cefa')
        vb.lbl_seconds_game.place(x=425, y= 80, width=125, height=50)

        if vb.seconds != 0:
            
            vb.lbl_seconds_game.after(10, lambda : seconds_in_game(root))

    
    



