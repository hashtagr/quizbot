import db


def print_this_game():
    text = ""
    res = db.get_this_game_scores()
    if res:
        text += "Счет этой игры:\n"
        for a in res:
            text += f"{a[0]} - {a[1]}\n"
    else:
        text += "Никто из команд пока что не получил баллы за эту игру"
    return text


def print_all_scores():
    text = "Турнирная таблица:\n"
    res = db.get_all_games_scores()
    for a in res:
        text += f"{a[0]} | {a[1]}\n"
    return text


def print_question(question_num):
    text = ""
    res = db.get_question(question_num)
    if res:
        text += "Вопрос:\n\n"
        text += f"{res[0]}\n\nКоличество баллов за вопрос:{res[1]}"
    else:
        text += "Больше нет вопросов"
    return text


def print_next_question(question_num):
    text = ""
    res = db.get_all_games_scores()
    if res:
        text += "Следующий вопрос:\n\n"
        text += f"Раунд {res[0]} вопрос №{res[1]}\n\n{res[2]}\nОтвет: {res[3]}\nКоличество баллов:{res[4]}"
    else:
        text += "Больше нет вопросов"
    return text
