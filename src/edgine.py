import interface


def start():
    try:
        interface.bot.polling()
    except Exception as ex:
        print("err: ", ex)
        start()


start()
