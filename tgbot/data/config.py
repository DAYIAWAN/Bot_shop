# - *- coding: utf- 8 - *-
import configparser

read_config = configparser.ConfigParser()
read_config.read("settings.ini")

BOT_TOKEN = read_config['settings']['token'].strip().replace(" ", "")  # Токен бота
PATH_DATABASE = "tgbot/data/database.db"  # Путь к БД
PATH_LOGS = "tgbot/data/logs.log"  # Путь к Логам
BOT_VERSION = "3.3"  # Версия бота


# Получение администраторов бота
def get_admins():
    read_admins = configparser.ConfigParser()
    read_admins.read("settings.ini")

    admins = read_admins['settings']['admin_id'].strip().replace(" ", "")

    if "," in admins:
        admins = admins.split(",")
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while "" in admins: admins.remove("")
    while " " in admins: admins.remove(" ")
    while "\r" in admins: admins.remove("\r")
    while "\n" in admins: admins.remove("\n")

    admins = list(map(int, admins))

    return admins


BOT_DESCRIPTION = f"""
<b>⚜ Bot Version: <code>{BOT_VERSION}</code>
🔗 Link: <a href='https://kwork.ru/script-programming/22401668/premium-bot-avtoprodazh-telegram-magazin-telegram-autoshop'>Click me</a>
♻ Bot created by @deathdilemma
🍩 Donate to the author: <a href='https://sobe.ru/na/a212u0i8E2C7'>Click me</a>
""".strip()
