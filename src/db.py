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
    return res


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


def drop_tables():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "BEGIN TRANSACTION;" \
          "DELETE FROM game_board;" \
          "COMMIT;" \
          "BEGIN TRANSACTION" \
          "DELETE FROM game_teams;" \
          "COMMIT;" \
          "BEGIN TRANSACTION;" \
          "UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'game_board';" \
          "COMMIT;" \
          "BEGIN TRANSACTION;" \
          "UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'game_teams';" \
          "COMMIT"
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


def add_result():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "UPDATE teams SET points = (SELECT sum FROM " \
          "(SELECT game_board.team, teams.points + SUM(game_board.points) AS sum FROM game_board " \
          "JOIN teams ON game_board.team = teams.name) " \
          "WHERE team = teams.name) WHERE name IN (SELECT teams.name FROM teams " \
          "JOIN game_board ON teams.name = game_board.team)"
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
        res = cursor.fetchone()
    cursor.close()
    con.close()
    return int(res) if res else 0


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
    tmp = "SELECT round_num, q_num, question, answer FROM questions WHERE id = " + str(num)
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
    res = False
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


def check(num):
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT game_teams.chat_id FROM game_teams " \
          "JOIN game_board ON game_teams.name = game_board.team " \
          "WHERE game_board.q_num = " + str(num)
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
