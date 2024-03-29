import keyboards
import db
import prints
import telebot


bot = telebot.TeleBot("5629181435:AAFOBdRBGJT8tDnddW6kPnGHt5Mj12Y6J_E")
question_num = 0
process = 0


@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user.username
    print(f"new user {user}")
    if db.add_user_to_data(message.chat.id):
        print(f"user {user} added to database")
    if db.get_access(message.chat.id) == "":
        bot.send_message(message.chat.id, text="Добро пожаловать на игру!\nПожалуйста, введите пароль доступа:")


@bot.message_handler(content_types=['text'])
def parser(message):
    if db.get_access(message.chat.id) == "":
        if message.text == db.get_host_password():
            if db.get_host_id() == 0:
                db.add_host_to_game(message.chat.id)
                kb = keyboards.host_menu_buttons()
                bot.send_message(message.chat.id, text="Авторизация ведущего игры пройдена, можете начинать",
                                 reply_markup=kb)
                bot.register_next_step_handler(message, game_process)
            else:
                bot.send_message(message.chat.id, text="Ведущий данной игры уже был авторизован, повторите ввод пароля")
        elif message.text == db.get_gamer_password():
            if db.get_host_id() != 0:
                bot.send_message(message.chat.id, text="Авторизация игрока пройдена. Введите название вашей команды:")
                bot.register_next_step_handler(message, get_team_name)
            else:
                bot.send_message(message.chat.id, text="Пожалуйста, дождитесь команды ведущего и введите пароль снова")
        else:
            bot.send_message(message.chat.id, text="Пароль введен неверно!\nПовторите ввод:")
    else:
        game_process(message)


def get_team_name(message):
    name = message.text
    name.lower()
    if db.add_team_to_game(message.chat.id, name):
        check = db.get_all_teams()
        if not check or name not in check:
            if db.add_team_to_teams(name):
                bot.send_message(db.get_host_id(), text=f"Команда {name} добавлена в команды турнира")
            kb = keyboards.gamer_menu_buttons()
            bot.send_message(message.chat.id, text="Авторизация команды пройдена, мы всегда рады новым командам!\n\n"
                                                   "Если ваша команда до этого уже участвовала в играх этого турнира, "
                                                   "то сообщите ведущему об ошибке", reply_markup=kb)
        else:
            bot.send_message(db.get_host_id(), text=f"Команда {name} снова с нами!")
            kb = keyboards.gamer_menu_buttons()
            bot.send_message(message.chat.id, text="Авторизация команды пройдена, рады снова видеть вас на нашей игре!"
                                                   "\n\nЕсли ваша команда до этого не участвовала в играх этого "
                                                   "турнира, то сообщите ведущему об ошибке", reply_markup=kb)
        bot.register_next_step_handler(message, game_process)
    else:
        bot.send_message(db.get_host_id(), text=f"!!!!Команда {name} пользователя {message.from_user.username} "
                                                f"не может быть добавлена!!!!")
        bot.reply_to(message, text="Команда с таким названием уже есть в этой игре, пожалуйста, выберите другое:")


def game_process(message):
    global question_num, process
    if process == 1:
        question_process(message)
    elif message.text == "🔸 Посмотреть счет этой игры 🔸" or \
            message.text == "🔹 Посмотреть счет этой игры 🔹":
        bot.send_message(message.chat.id, text=prints.print_this_game())
    elif message.text == "🔸 Посмотреть турнирную таблицу 🔸" or \
            message.text == "🔹 Посмотреть турнирную таблицу 🔹":
        bot.send_message(message.chat.id, text=prints.print_all_scores())
    elif message.text == "🔹 Посмотреть следующий вопрос 🔹":
        bot.send_message(db.get_host_id(), text=prints.print_next_question(question_num + 1))
    elif message.text == "🔹 Отправить следующий вопрос 🔹":
        process = 1
        if question_num < db.get_num_of_questions():
            question_num += 1
            for a in db.get_gamers_chat_id():
                bot.send_message(int(a[0]), text=prints.print_question(question_num))
            if db.get_access(message.chat.id) == "host":
                question_process(message)
        else:
            bot.send_message(db.get_host_id(), text="Вопросы закончились")
    elif message.text == "🔹 Записать результат игры 🔹":
        if db.add_result():
            bot.send_message(db.get_host_id(), text="Результат записан")
        else:
            bot.send_message(db.get_host_id(), text="Возникла ошибка\nПроверьте состояние таблиц")
    elif message.text == "🔹 Очистить таблицы 🔹":
        bot.send_message(db.get_host_id(), text=prints.print_this_game())
        bot.send_message(db.get_host_id(), text=prints.print_all_scores())
        if db.drop_tables():
            bot.send_message(db.get_host_id(), text="Таблицы очищены")
        else:
            bot.send_message(db.get_host_id(), text="Возникла ошибка\nПроверьте состояние таблиц")
    else:
        bot.send_message(message.chat.id, text="Ошибка!")
        bot.register_next_step_handler(message, game_process)


def question_process(message):
    global question_num
    if db.get_access(message.chat.id) == "gamer" and not db.check_gamer(message.chat.id, question_num):
        if str(message.text).lower() == db.get_answer(question_num):
            if db.add_question_res(message.chat.id, question_num):
                bot.send_message(db.get_host_id(), text=f"🟢 Команда {db.get_team_name(message.chat.id)} ответила "
                                                        f"'{message.text}', результат успешно записан в базу данных")
            else:
                bot.send_message(db.get_host_id(), text=f"!!!Команда {db.get_team_name(message.chat.id)} ответила "
                                                        f"правильно, но произошла ошибка записи в базу данных!!!")
        else:
            if db.add_wrong_question_res(message.chat.id, question_num):
                bot.send_message(db.get_host_id(), text=f"🔴 Команда {db.get_team_name(message.chat.id)} ответила "
                                                        f"'{message.text}' - неправильно")
            else:
                bot.send_message(db.get_host_id(), text=f"!!!Команда {db.get_team_name(message.chat.id)} ответила "
                                                        f"НЕправильно, но произошла ошибка записи в базу данных!!!")
    elif db.get_access(message.chat.id) == "host":
        kb = keyboards.stop_button()
        bot.send_message(message.chat.id, text="Нажмите кнопку, чтобы закончить прием ответов:", reply_markup=kb)
    else:
        bot.send_message(message.chat.id, text="Пожалуйста,дождитесь, пока ведущий завершит прием ответов")


@bot.callback_query_handler(func=lambda message: True)
def stop(call):
    global question_num, process
    if call.data == 'stop':
        tmp_check = db.check(question_num)
        if tmp_check:
            check = []
            for a in tmp_check:
                check.append(a[0])
            for a in db.get_gamers_chat_id():
                i = 0
                if a[0] in check:
                    bot.send_message(int(a[0]), text="🟢 Вы ответили правильно 🟢")
                else:
                    bot.send_message(int(a[0]), text="🔴 Вы ответили неправильно 🔴")
                i += 1
        else:
            for a in db.get_gamers_chat_id():
                bot.send_message(int(a[0]), text="🔴 Вы не успели ответить 🔴")
        bot.send_message(db.get_host_id(), text="Прием ответов завершен")
    process = 0
