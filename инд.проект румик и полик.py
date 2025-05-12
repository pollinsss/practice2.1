import telebot
import random
from telebot import types


API_TOKEN = '7874899741:AAGnlbVTIfuoDAgyjSoYlsvGlhjTiHJKqQ8'
bot = telebot.TeleBot(API_TOKEN)

jokes = {
    "short": [
        "Почему программисты не любят природу? Потому что в ней слишком много багов.",
        "Какой язык программирования самый оптимистичный? Java, потому что у него всегда есть исключения!",
        "Программисты на работе общаются двумя фразами: «непонятно» и «вроде работает».",
    ],
    "long": [
        "Приходит программист в аптеку и спрашивает: 'У вас есть что-нибудь от усталости?' Аптекарь отвечает: 'Да, у нас есть отпуск!'",
        "Звонит программист другу: 'Ты где?' Друг отвечает: 'На работе.' Программист: 'А что ты там делаешь?' Друг: 'Работаю.' Программист: 'А что ты там делаешь?' Друг: 'Работаю.' Программист: 'А что ты там делаешь?' Друг: 'Работаю.' Программист: 'А что ты там делаешь?' Друг: 'Работаю.' Программист: 'А что ты там делаешь?' Друг: 'Работаю.'",
        "Работа программиста и шамана имеет много общего — оба бормочут непонятные слова, совершают непонятные действия и не могут объяснить, как оно работает ",

    ]
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-анекдот. Выберите действие:\n"
                          "/joke - Получить случайный анекдот\n"
                          "/category - Получить анекдот по категории\n"
                          "/add - Добавить новый анекдот (только для администраторов)\n"
                          "/list - Получить список всех анекдотов\n"
                          "/topic - Получить анекдот на определённую тему")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    category = random.choice(list(jokes.keys()))
    joke = random.choice(jokes[category])
    bot.reply_to(message, joke)

@bot.message_handler(commands=['category'])
def ask_category(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Короткие")
    item2 = types.KeyboardButton("Длинные")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Короткие", "Длинные"])
def send_category_joke(message):
    category = "short" if message.text == "Короткие" else "long"
    joke = random.choice(jokes[category])
    bot.reply_to(message, joke)

@bot.message_handler(commands=['add'])
def add_joke(message):
    bot.reply_to(message, "Введите анекдот:")
    bot.register_next_step_handler(message, process_new_joke)

def process_new_joke(message):
    new_joke = message.text
    jokes["short"].append(new_joke)
    bot.reply_to(message, "Анекдот добавлен!")

@bot.message_handler(commands=['list'])
def list_jokes(message):
    all_jokes = "\n".join([f"{i+1}. {joke}" for category in jokes.values() for i, joke in enumerate(category)])
    bot.reply_to(message, f"Список анекдотов:\n{all_jokes}")

@bot.message_handler(commands=['topic'])
def ask_topic(message):
    bot.reply_to(message, "Введите тему анекдота:")
    bot.register_next_step_handler(message, process_topic)

def process_topic(message):
    topic = message.text
    bot.reply_to(message, f"Извините, анекдоты на тему '{topic}' пока не добавлены.")

bot.polling()



