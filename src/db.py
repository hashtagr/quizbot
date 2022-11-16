import sqlite3


def get_host_password():
    con = sqlite3.connect('quizbot.db')
    cursor = con.cursor()
    tmp = "SELECT password FROM passwords WHERE user_type = \"host\""
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


def get_host_chat_id():
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
