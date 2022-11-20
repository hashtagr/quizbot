from telebot import types


def host_menu_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('🔹 Посмотреть следующий вопрос 🔹')
    btn2 = types.KeyboardButton('🔹 Отправить следующий вопрос 🔹')
    btn3 = types.KeyboardButton('🔹 Посмотреть счет этой игры 🔹')
    btn4 = types.KeyboardButton('🔹 Посмотреть турнирную таблицу 🔹')
    btn5 = types.KeyboardButton('🔹 Записать результат игры 🔹')
    btn6 = types.KeyboardButton('🔹 Очистить таблицы 🔹')
    kb.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return kb


def gamer_menu_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('🔸 Посмотреть счет этой игры 🔸')
    btn2 = types.KeyboardButton('🔸 Посмотреть турнирную таблицу 🔸')
    # btn3 = types.KeyboardButton('🔸  🔸')
    # btn4 = types.KeyboardButton('🔸  🔸')
    kb.add(btn1, btn2)#, btn3, btn4)
    return kb


def stop_button():
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Стоп', callback_data='stop')
    return kb
