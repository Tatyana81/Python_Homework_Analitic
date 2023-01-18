from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
import sqlite3

bot_token = "1032714419:AAG8P2VOrikrQ-ODnvyWabFP8SyLdKvfHBI"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

conn = sqlite3.connect('students.db', check_same_thread=False)
cursor = conn.cursor()


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет! Я бот-телефонный справочник. Выбери команду \n"
    "/show - показать весь телефонный справочник \n/find - найти по фамилии\n"
    "/add - добавить запись \n/delete - удалить запись \n/exit - выход")


def exit(update, context):
    context.bot.send_message(update.effective_chat.id, "Пока, пока!")


# показать всех студентов 

def gg():
    cursor.execute("select * from students")
    results = cursor.fetchall()
    my_list = []
    for x in results:
        my_list.append(' | '.join(map(str,x)))
    my_str = '\n'.join(my_list)
    return(my_str)
   

def show(update, context):
    context.bot.send_message(update.effective_chat.id, text = gg())


def find(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите фамилию с большой буквы ")
    return 1

def delete(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите номер id")
    return 1


def add(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите имя, фамилию и телефон через пробел ")
    return 1


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

# поиск записи
def find_bd(surname2):
    surname2 = str(surname2)
    cursor.execute(f"select * from students where surname like '%{surname2}%'")
    results = cursor.fetchall()
    my_list = []
    for x in results:
        my_list.append(' | '.join(map(str,x)))
    my_str = '\n'.join(my_list)
    return(my_str)


def delete_bd(id):
    cursor.execute(
        f"delete from students where id={id}"
    )
    conn.commit()
    

def find_surname(update, context):
    surname = update.message.text
    update.message.reply_text(
        f"Ответ {find_bd(surname)}. Введите еще фамилию или нажмите /stop")


def delete_id(update, context):
    id = update.message.text
    delete_bd(id)
    update.message.reply_text(
        f"Запись с номером {id} удалена. Введите еще id или нажмите /stop")


def add_id(update, context):
    data = update.message.text
    add_bd(data)
    update.message.reply_text(
        f"Запись добавлена. Введите еще данные или нажмите /stop. Для просмотра списка нажмите /show")


def add_bd(data):
    data_ls = data.split()
    name = data_ls[0]
    surname = data_ls[1]
    number = int(data_ls[2])
    cursor.execute(
        f"insert into students (name, surname, number) "
        f"values ('{name}', '{surname}', {number})")
    conn.commit()
    

find_handler = ConversationHandler(
    entry_points=[CommandHandler('find', find)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, find_surname)]
        },
    fallbacks=[CommandHandler('stop', stop)]
    )


delete_handler = ConversationHandler(
    entry_points=[CommandHandler('delete', delete)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, delete_id)]
        },
    fallbacks=[CommandHandler('stop', stop)]
    )


add_handler = ConversationHandler(
    entry_points=[CommandHandler('add', add)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, add_id)]
        },
    fallbacks=[CommandHandler('stop', stop)]
    )


start_handler = CommandHandler('start', start)
exit_handler = CommandHandler('exit', exit)
show_handler = CommandHandler('show', show)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(exit_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(find_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(add_handler)

updater.start_polling()
updater.idle()