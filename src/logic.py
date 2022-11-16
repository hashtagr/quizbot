import db


def get_team_name(message, bot):
    name = ""
    name += message.text
    name.lower()
    if db.add_team_to_game(message.chat.id, name):
        if name in db.get_all_teams():
            print(f"Команда {name} снова с нами!")
            bot.send_message(message.chat.id, text="Авторизация команды пройдена, рады снова видеть вас на нашей\
                        игре!\n\nЕсли ваша команда до этого не участвовала в играх этого турнира, то сообщите ведущему\
                        об ошибке.")
        else:
            if db.add_team_to_teams(name):
                print(f"Команда {name} добавлена в команды турнира")
            bot.send_message(message.chat.id, text="Авторизация команды пройдена, мы всегда рады новым командам!\
                        \n\nЕсли ваша команда до этого уже участвовала в играх этого турнира, то сообщите ведущему об\
                        ошибке.")
        authorization_flag = 0
    else:
        print(f"!!!!Команда {name} пользователя {message.from_user.username} не может быть добавлена!!!!")
        bot.reply_to(message, text="Команда с таким названием уже есть в этой игре, пожалуйста, выберите другое:")
        authorization_flag = 1
    return authorization_flag
