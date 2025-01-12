#     @nikita_film_bot

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


list_command = """
/help - назви всіх команд
/hello - Привітання
/say1 - Вірш Ліни Костенко "Крила"
/say2 - Тарас Шевченко "Заповіт"
/say3 - Іван Франко "Каменярі"
/say4 - Леся Українка "Contra spem spero"
/say5 - Павло Тичина "Гаї шумлять"
/say6 - Олександр Олесь "Чари ночі"
/say7 - Василь Симоненко "Ти знаєш, що ти людина?"
/say8 - Дмитро Павличко "Два кольори"
/say9 - Богдан-Ігор Антонич "Різдво"
/say10 - Олена Теліга "Сучасникам"
"""


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def say1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Ліна Костенко\nКрила\nЛюдина нібито не літає...\nА крила має, а крила має!")

async def say2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Тарас Шевченко\nЗаповіт\nЯк умру, то поховайте\nМене на могилі...")

async def say3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Іван Франко\nКаменярі\nЯ бачив дивний сон. Немов передо мною\nБезмірна, та пуста і дика площина...")

async def say4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Леся Українка\nContra spem spero\nГетьте, думи, ви, хмари осінні!")

async def say5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Павло Тичина\nГаї шумлять\nГаї шумлять — я слухаю,\nХмарки біжать — милуюся...")

async def say6(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Олександр Олесь\nЧари ночі\nСміються, плачуть солов'ї\nІ б'ють піснями в груди...")

async def say7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Василь Симоненко\nТи знаєш, що ти людина?\nТи знаєш, що ти людина?\nТи знаєш про це чи ні?")

async def say8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Дмитро Павличко\nДва кольори\nЯк я малим збирався навесні\nПіти у світ незнаними шляхами...")

async def say9(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Богдан-Ігор Антонич\nРіздво\nНародився Бог на санях\nВ лемківськім містечку Дуклі.")

async def say10(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Олена Теліга\nСучасникам\nНе треба слів! Хай буде тільки діло!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(list_command)


app = ApplicationBuilder().token("7623558621:AAGuJJvmKeC_uuY4QylqUnuipakolBA1V3w").build()


app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("say1", say1))
app.add_handler(CommandHandler("say2", say2))
app.add_handler(CommandHandler("say3", say3))
app.add_handler(CommandHandler("say4", say4))
app.add_handler(CommandHandler("say5", say5))
app.add_handler(CommandHandler("say6", say6))
app.add_handler(CommandHandler("say7", say7))
app.add_handler(CommandHandler("say8", say8))
app.add_handler(CommandHandler("say9", say9))
app.add_handler(CommandHandler("say10", say10))


app.run_polling()
