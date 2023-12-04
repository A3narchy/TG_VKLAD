from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на ваш токен бота
bot = telebot.TeleBot('6827182788:AAF1dPMP8HKlyOFc8C0EEGcxwSlNC8lzfCs')

@bot.message_handler(commands=['start'])
def start(message):
    send_keyboard1(message.chat.id)

@bot.message_handler(commands=['cancel'])
def cancel_action(message):
    bot.reply_to(message, "Все предыдущие действия отменены")
    send_keyboard1(message.chat.id)

url = 'https://www.sravni.ru/vklady/top/#popup=5dbc0425d67e15001b400b86'
page = requests.get(url)
soup = BeautifulSoup(page.content.decode('utf-8'), "html.parser")

percent_elements = soup.find_all('div', class_='_1mfld7a')      # Срок и проценты
title = soup.find_all('span', class_='_jp36ng')                 # Название вклада
summa = soup.find_all('div', class_='_5gmjom _1livb46')         # Сумма
title_bank = soup.find_all('span', class_='_15rrp4h')           # Название банка

def bank():
    lines_printed = 0         #
    bank_list = []            # Создаем пустой список для хранения строк
    for element in title_bank:
        text_content = element.get_text(strip=True)
        bank_list.append(text_content)  # Добавляем строку в список
        lines_printed += 1
        if lines_printed == 6:
            break
    return bank_list

def vklad(title):
    lines_printed = 0
    vklad_list = []                     # Создаем пустой список для хранения строк
    for element in title:
        title_text = element.get_text(strip=True)
        vklad_list.append(title_text)  # Добавляем строку в список
        lines_printed += 1
        if lines_printed == 6:
            break
    return vklad_list

def srok():
    words_to_remove = ['%']
    lines_printed = 0
    srok_list = []
    for element in percent_elements:
        text_content = element.get_text(strip=True)
        if not any(word in text_content for word in words_to_remove):
            srok_list.append(text_content)
            lines_printed += 1
            if lines_printed == 6:
                break
    return srok_list

def proccent():
    words_to_remove = ['дней', 'дня', 'месяцев']
    lines_printed = 0
    proccent_list = []
    for element in percent_elements:
        text_content = element.get_text(strip=True)
        if not any(word in text_content for word in words_to_remove):
            proccent_list.append(text_content)
            lines_printed += 1
            if lines_printed == 6:
                break
    return proccent_list         

def cash():
    words_to_remove = ['%','дней', 'дня', 'месяцев']  
    lines_printed = 0
    cash_list = []  # Создаем пустой список для хранения строк
    for element in summa:
        text_content = element.get_text(strip=True)
        if not any(word in text_content for word in words_to_remove):
            cash_list.append(text_content)  # Добавляем строку в список
            lines_printed += 1
            if lines_printed == 6:
                break
    return cash_list

vklad_data = vklad(title)
first_vklad_line = vklad_data[0]  # Получаем первую строку из списка
second_vklad_line = vklad_data[1]  # Получаем вторую строку из списка
three_vklad = vklad_data[2]
four_vklad = vklad_data[3]
five_vklad = vklad_data[4]

bank_data = bank()
first_bank = bank_data[0]  # Получаем первую строку из списка
second_bank = bank_data[1]  # Получаем вторую строку из списка
three_bank = bank_data[2]
four_bank = bank_data[3]
five_bank = bank_data[4]

cash_data = cash()
first_cash = cash_data[0]  # Получаем первую строку из списка
second_cash = cash_data[1]  # Получаем вторую строку из списка
three_cash = cash_data[2]
four_cash = cash_data[3]
five_cash = cash_data[4]

srok_data = srok()
first_srok = srok_data[0]  # Получаем первую строку из списка
second_srok = srok_data[1]  # Получаем вторую строку из списка
three_srok = srok_data[2]
four_srok = srok_data[3]
five_srok = srok_data[4]

proccent_data = proccent()
first_proccent = proccent_data[0]  # Получаем первую строку из списка
second_proccent = proccent_data[1]  # Получаем вторую строку из списка
three_proccent = proccent_data[2]
four_proccent = proccent_data[3]
five_proccent = proccent_data[4]

bot.set_my_commands([
    ('start', 'Начать'),
    ('cancel', 'Отмена'),
    ('kalk', 'Калькулятор')
    # Другие команды
])

def send_keyboard1(chat_id):
    markup = types.InlineKeyboardMarkup()                                           # Создание клавиатуры типа InlineKeyboardMarkup
    item1 = types.InlineKeyboardButton('🌟 Вклады', callback_data='option1')      # Создание кнопок с соответствующими callback_data
    item2 = types.InlineKeyboardButton('🚀 Все комманды', callback_data='option2')
    item3 = types.InlineKeyboardButton('🎲 Помощь', callback_data='option3')
    markup.row(item1, item2)                                                       # Добавление кнопок в разметку
    markup.add(item3)
    # Отправка сообщения с клавиатурой
    bot.send_message(chat_id, "Я бот анархиста:", reply_markup=markup)

def send_keyboard2(chat_id):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('🔔 Следуюшие вклады', callback_data='option4')
    item2 = types.InlineKeyboardButton('💡 Выход ', callback_data='option100')
    markup.row(item1, item2)
    bot.send_message(chat_id, "Выберите предпочтительную опцию:", reply_markup=markup)

def send_keyboard3(chat_id):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('🔔 Следуюшие вклады', callback_data='option5')
    item2 = types.InlineKeyboardButton('💡 Выход ', callback_data='option100')
    markup.row(item1, item2)
    bot.send_message(chat_id, "Выберите предпочтительную опцию:", reply_markup=markup)

def send_keyboard4(chat_id):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('🔔 Следуюшие вклады', callback_data='option6')
    item2 = types.InlineKeyboardButton('💡 Выход ', callback_data='option100')
    markup.row(item1, item2)
    bot.send_message(chat_id, "Выберите предпочтительную опцию:", reply_markup=markup)

def send_keyboard5(chat_id):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('🔔 Следуюшие вклады', callback_data='option7')
    item2 = types.InlineKeyboardButton('💡 Выход ', callback_data='option100')
    markup.row(item1, item2)
    bot.send_message(chat_id, "Выберите предпочтительную опцию:", reply_markup=markup)

def send_keyboard6(chat_id):
    markup = types.InlineKeyboardMarkup()
    item2 = types.InlineKeyboardButton('💡 Выход ', callback_data='option100')
    markup.row(item2)
    bot.send_message(chat_id, "Сегодня закончились вклады, ожидайте следующего дня.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)                                # Обработчик нажатий на кнопки
def callback_query(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == 'option1':
        bot.send_message(chat_id, "Вы выбрали вклады")
        vklad_info = "Информация о вкладе:\n\n" + \
                    f"Название банка: {first_bank}\n" +\
                    f"Название вклада: {first_vklad_line}\n" +\
                    f"Сумма вклада: {first_cash}\n" +\
                    f"Срок вклада: {first_srok}\n" +\
                    f"Проценты : {first_proccent}\n"
        bot.send_message(chat_id, vklad_info)
        send_keyboard2(chat_id)

    elif call.data == 'option2':
        bot.send_message(chat_id, "Вы выбрали узнать все мои комманды")
        commands = "Вот все мои комманды:\n\n" +\
                    f"/start чтобы запустить бота\n" +\
                    f"/cancel чтобы отменить все действия, и вернуться в главное меню\n" +\
                    f"/kalk чтобы включить калькулятор который рассчитывает ваш процент."
        bot.send_message(chat_id, commands) 

    elif call.data == 'option4':
        bot.send_message(chat_id, "Вы выбрали следующий вклад")
        vklad_info2 = "Информация о вкладе:\n\n" + \
                    f"Название банка: {second_bank}\n" +\
                    f"Название вклада: {second_vklad_line}\n" +\
                    f"Сумма вклада: {second_cash}\n" +\
                    f"Срок вклада: {second_srok}\n" +\
                    f"Проценты : {second_proccent}\n"
        bot.send_message(chat_id, vklad_info2)
        send_keyboard3(chat_id)

    elif call.data == 'option5':
        bot.send_message(chat_id, "Вы выбрали следующий вклад")
        vklad_info3 = "Информация о вкладе:\n\n" + \
                    f"Название банка: {three_bank}\n" +\
                    f"Название вклада: {three_vklad}\n" +\
                    f"Сумма вклада: {three_cash}\n" +\
                    f"Срок вклада: {three_srok}\n" +\
                    f"Проценты : {three_proccent}\n"
        bot.send_message(chat_id, vklad_info3)
        send_keyboard4(chat_id)
    
    elif call.data == 'option6':
        bot.send_message(chat_id, "Вы выбрали следующий вклад")
        vklad_info3 = "Информация о вкладе:\n\n" + \
                    f"Название банка: {four_bank}\n" +\
                    f"Название вклада: {four_vklad}\n" +\
                    f"Сумма вклада: {four_cash}\n" +\
                    f"Срок вклада: {four_srok}\n" +\
                    f"Проценты : {four_proccent}\n"
        bot.send_message(chat_id, vklad_info3)
        send_keyboard5(chat_id)

    elif call.data == 'option7':
        bot.send_message(chat_id, "Вы выбрали следующий вклад")
        vklad_info4 = "Информация о вкладе:\n\n" + \
                    f"Название банка: {five_bank}\n" +\
                    f"Название вклада: {five_vklad}\n" +\
                    f"Сумма вклада: {five_cash}\n" +\
                    f"Срок вклада: {five_srok}\n" +\
                    f"Проценты : {five_proccent}\n"
        bot.send_message(chat_id, vklad_info4)                 
        send_keyboard6(chat_id)
        
    elif call.data == 'option3':
        bot.send_message(chat_id, "Если у вас возникли сотруднение или идеи как улучшить меня, обращайтесь создателю моему. https://t.me/Anarchy3")
        send_keyboard1(chat_id)

    elif call.data == 'option100':
        bot.send_message(chat_id, "Вы выбрали выход")
        send_keyboard1(chat_id)

# Обработчик команды /start
@bot.message_handler(commands=['kalk'])
def kalkulator(message):
    bot.reply_to(message,   "Привет! Этот бот рассчитывает выплаченные проценты.\nВведите через пробел значения P, I, T, K.\n\n" + \
                                f"Где P — первоначальная сумма вложений\n" +\
                                f" I — годовая ставка\n" +\
                                f" T — количество дней вклада\n" +\
                                f" K — количество дней в году — 365 или 366.\n")

# Обработчик текстовых сообщений с параметрами для расчета
@bot.message_handler(func=lambda message: True)
def calculate_interest(message):
    try:
        values = message.text.split()
        if len(values) != 4:
            bot.reply_to(message, "Неверное значение.\n\n" +\
                                f"Где P — первоначальная сумма вложений.\n" +\
                                f" I — годовая ставка\n" +\
                                f" T — количество дней вклада\n" +\
                                f" K — количество дней в году — 365 или 366.\n")
            return
        
        P, I, T, K = map(lambda x: float(x.replace(',','.')), values)
        
        S = P * I * T/K/100
        rounded_result = round(S, 1)
        bot.reply_to(message, f"Выплаченные проценты: {rounded_result} рублей")
        send_keyboard1(message.chat.id)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {str(e)}")

# Запуск бота
bot.polling()


