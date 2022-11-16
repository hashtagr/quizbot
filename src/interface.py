import logic
import db
import telebot


bot = telebot.TeleBot("5629181435:AAFOBdRBGJT8tDnddW6kPnGHt5Mj12Y6J_E")
authorization_flag = 0


def get_team_name(message):
    global authorization_flag
    name = ""
    name += message.text
    name.lower()
    if db.add_team_to_game(message.chat.id, name):
        if name in db.get_all_teams():
            bot.send_message(db.get_host_id(), text=f"Команда {name} снова с нами!")
            bot.send_message(message.chat.id, text="Авторизация команды пройдена, рады снова видеть вас на нашей\
            игре!\n\nЕсли ваша команда до этого не участвовала в играх этого турнира, то сообщите\
            ведущему об ошибке")
        else:
            if db.add_team_to_teams(name):
                bot.send_message(db.get_host_id(), text=f"Команда {name} добавлена в команды турнира")
            bot.send_message(message.chat.id, text="Авторизация команды пройдена, мы всегда рады новым командам!\
            \n\nЕсли ваша команда до этого уже участвовала в играх этого турнира, то сообщите\
            ведущему об ошибке")
        authorization_flag = 0
    else:
        bot.send_message(db.get_host_id(), text=f"!!!!Команда {name} пользователя {message.from_user.username} не может\
        быть добавлена!!!!")
        bot.reply_to(message, text="Команда с таким названием уже есть в этой игре, пожалуйста, выберите другое:")
        authorization_flag = 1


@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.username
    print(f"new user: {user}")
    bot.send_message(message.chat.id, text="Добро пожаловать на игру!\nПожалуйста, введите пароль доступа:")


@bot.message_handler(content_types=['text'])
def parser(message):
    global authorization_flag
    if db.get_access(message.chat.id) == "":
        if message.text == db.get_host_password() or message.chat.id == db.get_host_id():
            db.add_host_to_game(message.chat.id)
            bot.send_message(message.chat.id, text="Авторизация ведущего игры пройдена, можете начинать")
        elif message.text == db.get_gamer_password():
            if db.get_host_id() != 0:
                bot.send_message(message.chat.id, text="Авторизация игрока пройдена. Введите название вашей команды:")
                bot.register_next_step_handler(message, get_team_name)
            else:
                bot.send_message(message.chat.id, text="Пожалуйста, дождитесь авторизации ведущего")
        else:
            bot.send_message(message.chat.id, text="Пароль введен неверно!\nПовторите ввод:")
    else:
        if authorization_flag:
            get_team_name(message)
        else:
            bot.send_message(message.chat.id, text="что...")
        # bot.send_message(message.chat.id, text="gjnhlhrjh;")
