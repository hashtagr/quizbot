import sqlite3


def get_host_password():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT password FROM passwords WHERE user_type = 'host'"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res[0]


def get_gamer_password():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT password FROM passwords WHERE user_type = \"gamer\""
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res[0]


def add_team_to_game(chat_id, name):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "INSERT INTO game_teams (chat_id, name, access) VALUES (" + str(chat_id) + ", '" + name + "', 'gamer')"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return False
    else:
        con.commit()
        cursor.close()
        con.close()
        return True


def add_team_to_teams(name):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "INSERT INTO teams (name) VALUES ('" + name + "')"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return False
    else:
        con.commit()
        cursor.close()
        con.close()
        return True


def add_host_to_game(chat_id):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "INSERT INTO game_teams (chat_id, name, access) VALUES (" + str(chat_id) + ", 'HOST', 'host')"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return False
    else:
        con.commit()
        cursor.close()
        con.close()
        return True


def get_all_teams():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT name FROM teams"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res if res else 0


def get_host_id():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT chat_id FROM game_teams WHERE access = 'host'"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return int(res[0]) if res else 0


def get_access(chat_id):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT access FROM game_teams WHERE chat_id = '" + str(chat_id) + "'"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res[0] if res else ""


def get_num_of_questions():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT COUNT(*) FROM questions"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return int(res[0]) if res else 0


def get_gamers_chat_id():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT chat_id FROM game_teams WHERE access = 'gamer'"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchall()
    cursor.close()
    con.close()
    return res if res else 0


def get_this_game_scores():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT team, SUM(points) FROM game_board GROUP BY team"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchall()
    cursor.close()
    con.close()
    return res if res else 0


def get_all_games_scores():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT name, points FROM teams"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchall()
    cursor.close()
    con.close()
    return res if res else 0


def get_all_question(num):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT round_num, q_num, question, answer, value FROM questions WHERE id = " + str(num)
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res if res else 0


def get_question(num):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT question, value FROM questions WHERE id = " + str(num)
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res if res else 0


def get_answer(num):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT answer FROM questions WHERE id = " + str(num)
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res[0] if res else 0


def get_question_points(num):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT value FROM questions WHERE id = " + str(num)
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res[0] if res else 0


def get_team_name(chat_id):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT name FROM game_teams WHERE chat_id = " + str(chat_id)
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return res[0] if res else 0


def add_question_res(chat_id, num):
    points = get_question_points(num)
    name = get_team_name(chat_id)
    if name and points:
        con = sqlite3.connect('quizbot.db')
        cursor = con.cursor()
        tmp = "INSERT INTO game_board (team, q_num, points) VALUES ('" + name + "', " + str(num) + ", "\
              + str(points) + ")"
        try:
            cursor.execute(tmp)
        except sqlite3.IntegrityError:
            cursor.close()
            con.close()
            res = False
        else:
            con.commit()
            cursor.close()
            con.close()
            res = True
    else:
        res = False
    return res


def add_wrong_question_res(chat_id, num):
    name = get_team_name(chat_id)
    if name:
        con = sqlite3.connect('quizbot.db')
        cursor = con.cursor()
        tmp = "INSERT INTO game_board (team, q_num, points) VALUES ('" + name + "', " + str(num) + ", 0)"
        try:
            cursor.execute(tmp)
        except sqlite3.IntegrityError:
            cursor.close()
            con.close()
            res = False
        else:
            con.commit()
            cursor.close()
            con.close()
            res = True
    else:
        res = False
    return res


def check(num):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT game_teams.chat_id FROM game_teams " \
          "JOIN game_board ON game_teams.name = game_board.team " \
          f"WHERE game_board.q_num = {str(num)} AND NOT game_board.points = 0"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchall()
    cursor.close()
    con.close()
    return res if res else 0


def check_gamer(chat_id, num):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT game_board.team FROM game_board " \
          "JOIN game_teams ON game_board.team = game_teams.name " \
          f"WHERE game_board.q_num = {num} AND game_teams.chat_id = {chat_id}"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return 0
    else:
        res = cursor.fetchall()
    cursor.close()
    con.close()
    return res[0] if res else 0


def add_user_to_data(chat_id):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "INSERT INTO users_data (chat_id) VALUES (" + str(chat_id) + ")"
    res = False
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        res = False
    else:
        con.commit()
        cursor.close()
        con.close()
        res = True
    return res


def drop_tables():
    res = True
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "DELETE FROM game_board"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        res = False
    else:
        con.commit()
        cursor.close()
        con.close()
        res = True
    if res:
        con = sqlite3.connect('quizbot.db')
        cursor = con.cursor()
        tmp = "DELETE FROM game_teams WHERE access = 'gamer'"
        try:
            cursor.execute(tmp)
        except sqlite3.IntegrityError:
            cursor.close()
            con.close()
            res = False
        else:
            con.commit()
            cursor.close()
            con.close()
            res = True
    else:
        return res
    if res:
        con = sqlite3.connect('quizbot.db')
        cursor = con.cursor()
        tmp = "UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'game_board'"
        # "UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'game_teams';"
        try:
            cursor.execute(tmp)
        except sqlite3.IntegrityError:
            cursor.close()
            con.close()
            res = False
        else:
            con.commit()
            cursor.close()
            con.close()
            res = True
    else:
        return res
    if res:
        con = sqlite3.connect('quizbot.db')
        cursor = con.cursor()
        tmp = "UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'game_teams'"
        try:
            cursor.execute(tmp)
        except sqlite3.IntegrityError:
            cursor.close()
            con.close()
            res = False
        else:
            con.commit()
            cursor.close()
            con.close()
            res = True
    else:
        return res
    return res


def add_result():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "UPDATE teams SET points = points + (SELECT SUM(points) AS sum FROM game_board " \
          "WHERE team = teams.name) WHERE name IN (SELECT team FROM game_board)"
    try:
        cursor.execute(tmp)
    except sqlite3.IntegrityError:
        cursor.close()
        con.close()
        return False
    else:
        con.commit()
        cursor.close()
        con.close()
        return True
    return res
