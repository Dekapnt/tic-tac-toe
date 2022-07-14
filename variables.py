
"""фоны и картинки"""
fon_menu = '' """Фон первого меню"""; fon_game = '' """фон игры"""
img_win_1_x = '' """первая картинка выйгрыша"""; img_win_2_x = '' """вторая картинка выйгрыша"""; img_win_3_x = '' """третья картинка выйгрыша"""
img_win_4_x = '' """четвертая картинка выйгрыша"""; img_win_5_x = '' """пятая картинка выйгрыша"""; img_win_6_x = '' """шестая картинка выйгрыша"""
img_win_7_x = ''; img_win_8_x = ''; img_win_9_x = ''; img_win_10_x = ''; img_win_11_x = ''; img_win_12_x = ''
img_win_1_o = ''; img_win_2_o = ''; img_win_3_o = ''; img_win_4_o= ''; img_win_5_o = ''; img_win_6_o = ''
img_win_7_o = ''; img_win_8_o = ''; img_win_9_o = ''; img_win_10_o = ''; img_win_11_o = ''; img_win_12_o = ''
mini_x = ''; mini_o = ''
img_WIN_X = ''; img_WIN_O = ''; img_WIN_DRAW = ''

#фон при выйгрыше
win_text_x = ''; win_text_o = ''; win_text_draw = ''



"""кнопки\ надписи из меню"""
btn_menu_start = '' """Кнопка старт из меню"""; btn_menu_options = '' """Кнопка опций из меню"""; btn_menu_exit = '' """кнопка выход из меню"""
lbl_fon_menu = '' """фон меню подгрузка""" 


"""опции"""
listbox = '' """разрешение экрана для удаления"""; selected_screen_resolution = ''; """выбранный размер экрана"""; lbl_listbox = '' """текст разрешение экрана"""
btn_save_listbox = '' """сохранение настроек"""; btn_back = '' """выход из опций"""
file_win_resolution = '' """параметры.txt"""; 



"""размеры окон/положение кнопок/надписей из меню"""    




language = ''

start_btn_x = 40; """полоэение старт по х"""; start_btn_y = 150; """положение старт по у """; start_btn_width = 100; """ширина старт"""

options_btn_x = 40; """полоэение опций по х"""; options_btn_y = 190; """положение опций по у """; options_btn_width = 100; """ширина опций"""

exit_btn_x = 40; """полоэение опций по х"""; exit_btn_y = 230; """положение опций по у """; exit_btn_width = 100; """ширина опций"""


"""положение кнопок/надписей из опций"""
listbox_x = 40; """полоэение разрешений по х"""; listbox_y = 180; """положение разрешений по у """; listbox_width = 125; """ширина разрешений"""

listbox_lbl_x = 40; """полоэение надписи разрешение по х"""; listbox_lbl_y = 155; """положение надписи разрешение по у """

listbox_save_x = 500; """полоэение сохранения по х"""; listbox_save_y = 515; """положение сохранения по у """


"""кнопки controls_game.start_game"""
lbl_fon_game = '' """фон игры подгрузка"""
lbl_win_fon = '' """фон выйгрыша подгрузка"""
lbl_win_fon_2 = ''

btn_game_1 = ''; btn_game_2 = ''; btn_game_3 = ''; btn_game_4 = ''; btn_game_5 = ''
btn_game_6 = ''; btn_game_7 = ''; btn_game_8 = ''; btn_game_9 = ''


"""переменные из creating_images"""
motion = 1; """количество ходов"""; x_image = '' """картинка Х"""; o_image = '' """картинка о"""
stop_create_image = False


"""переменые проверки creating_images"""
x_1 = False; o_1 = False; x_2 = False; o_2 = False; x_3 = False; o_3 = False; x_4 = False; o_4 = False; x_5 = False
o_5 = False; x_6 = False; o_6 = False; x_7 = False; o_7 = False; x_8 = False; o_8 = False; x_9 = False; o_9 = False


"""переменные из отрисовки creating_images"""
lbl_image_1 = ''; lbl_image_2 = ''; lbl_image_3 = ''; lbl_image_4 = ''; lbl_image_5 = ''
lbl_image_6 = ''; lbl_image_7 = ''; lbl_image_8 = ''; lbl_image_9 = ''


"""переменные из отрисовки выйгрыша"""
lbl_image_win_1 = ''; lbl_image_win_2 = ''; lbl_image_win_3 = ''
btn_exit_menu = ''; btn_exit = ''; btn_reset = ''
stop_win_test_x = False; stop_win_test_o = False


"""переменные для удаления"""
no_delete_image = False

"""переменные для раундов и счета"""
lbl_round_text = ''; number_round = 1; lbl_score_text = ''; win_numer_x = 0; win_number_o = 0
score_x = 0; score_o = 0; lbl_score_text_mini_x = ''; lbl_score_text_mini_o = ''; lbl_score_text_x = ''
lbl_text_p_1 = ''; lbl_text_p_2 = ''
lbl_text_p_1_game = ''; lbl_text_p_2_game = ''


"""переменные для выбора количества раундов и секунд"""
lbl_text_round = ''; lbl_text_max_round = ''
btn_min_number_round = ''; btn_max_number_round = ''
max_round = 3; number_reset = 0
lbl_win_p1 = ''; lbl_win_p2 = ''; lbl_win_draw = ''

max_seconds = 10; lbl_text_seconds = ''; lbl_text_max_seconds = ''; btn_min_number_seconds = ''; btn_max_number_seconds = ''
lbl_seconds_game= ''; seconds = 00; milliseconds = 00; 
stop_assigning_values = False; out_of_time = False
stop_seconds_in_game = False; stop_assigning_values_2 = False; stop_assigning_values_3 = False

"""ВСЕ НАДПИСИ"""
text_language = ''
save_language = ''
back_language = ''
start_game_language = ''
options_language = ''
exit_language = ''
restart_language = ''
exit_to_menu = ''
round_language = ''
round_option = ''
seconds_option = ''


pashalka = '' #УДАЛИ
pahalka = '' #УДАЛИ!