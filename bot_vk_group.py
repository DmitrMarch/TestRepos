# !!!!!ЗНАЧКОМ 🤡 ПОМЕЧЕНЫ МЕСТА, ГДЕ НУЖНА ЗМЕНА!!!!!

# для связи с сервером вк
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# для функций Рандомайзера
import random

# для работы с картинками
import requests
import os
import PIL
from PIL import Image
import imagehash
import shutil
from fuzzywuzzy import fuzz

# для функций Калькулятора
from math import e, pi, sqrt, log, sin, cos, tan, factorial as f
mod = abs

# словарь имён (его можно посмотреть тут Словарь имён.txt)
with open('Словарь имён.txt', 'r', encoding='utf-8') as dict_names:
    dict_names1 = eval(dict_names.read())

# значение включения (ex = 0) / выключения проги (ex = 1)
ex = 0

# начальное количество сала и его общая стоимость для кажого пользователя (словарь тут Значения кликера.txt)
with open('Значения кликера.txt', 'r') as dict_klicker:
    dict_klicker1 = eval(dict_klicker.read())

# получение номеров последних картинок из словаря Значения картинок.txt
with open('Значения картинок.txt', 'r') as dict_values:
    dict_values1 = eval(dict_values.read())
    cat = dict_values1['cat']  # значение картинки кота
    dog = dict_values1['dog']  # значение картинки собаки
    neko = dict_values1['neko']  # значение картинки кошкодевочки
    other = dict_values1['other']  # значение картинки из категории другое

bot = '''🤖 Бот 🤖
Доступные команды бота:
1⃣  Фотоопределитель - 
👉Photo👈;
2⃣  Калькулятор - 
👉Calc👈;
3⃣  Рандомайзер - 
👉Rand👈;
4⃣  Выход в меню выбора бота - 👉Назад👈;
5⃣  Смена имени - Имя 
👉Новое имя👈;
6⃣  Свой числовой id - 
👉Id👈;
7⃣  Чужой числовой id - Id 
👉короткий адрес👈;
8⃣  Числовой id группы - Group id 
👉короткий адрес👈.
❗P.s. короткий адрес указывайте без @.'''

calc = '''❎ Калькулятор ❎
Доступные операторы и особые числа:
1⃣  Сложение или вычитание - 👉+👈 или 
👉-👈;
2⃣  Умножение или деление - 👉*👈 или 
👉/👈;
3⃣  Остаток или целая часть от деления - 👉%👈 или 👉//👈;
4⃣  Возведение в степень - 
👉**👈;
5⃣  Квадратный корень из числа - 👉sqrt(число)👈;
6⃣  Обычный или натуральный логарифм из числа - 
👉log(число, основание)👈 
или 👉log(число)👈;
7⃣  Числа е или Пи - 
👉e👈 или 👉pi👈;
8⃣  Синус, косинус или тангенс - 
👉sin(радианы)👈 или 
👉cos(радианы)👈 или 
👉tan(радианы)👈;
9⃣  Факториал из числа - 
👉f(число)👈;
🔟 Модуль из числа - 
👉mod(число)👈.
❗P.s. ввод примера - Реши 
👉пример👈.'''

rand = '''❓ Рандомайзер ❓
Доступные команды рандомайзера:
1⃣  Выбор одного случайного числа из диапазона от 1 до 2 числа - 
👉ранд 1 число 2 число👈;
2⃣  Выбор нескольких случайных чисел(3 число) из диапазона от 1 до 2 числа - 👉несранд3 число 1 число 2 число👈;
3⃣  Выбор случайного слова из списка слов - 👉cранд 1 слово 2 слово и т.д.👈;
4⃣  Выбор нескольких случайных слов(Число) из списка слов - 👉несcрандЧисло 1 слово 2 слово и т.д.👈.
❗P.s. случайные числа или слова не повоторяются, поэтому их количество не должно превышать 
количество чисел или слов в диапазоне или списке; числа в диапазоне пишутся от и до, например, от 1 до 
10 - это числа с 1 по 9.'''

# авторизация с помощью токена группы🤡
session = vk_api.VkApi(token="СЮДА СВОЙ ТОКЕН")  # его можно получить в настройках сообщества во вкладке Работа с API,
# где надо сначала включить LongPool и выбрать нужные типы событий, а также включить сообщения во вкладке Сообщения,
# где есть подвкладка Настройки для бота, только потом создавайте токен

# превращение картинок в хэш
def imgs_urls(val):
    return val.replace(val, f'{file}/{val}')

def imgs_open(val):
    return Image.open(val)

def imgs_hashs(val):
    return str(imagehash.phash(val))

# нахождение схожести в %
def similarity(hash2):
    return fuzz.token_sort_ratio(hash1, hash2)

# метод отправки сообщений
def write_msg(peer_id, message, keyboard=None):
    post = {
        'peer_id': peer_id,
        'message': message,
        'random_id': 0
    }
    if keyboard == keyboard1:
        post['keyboard'] = keyboard1.get_keyboard()
    elif keyboard == keyboard2:
        post['keyboard'] = keyboard2.get_keyboard()
    elif keyboard == keyboard3:
        post['keyboard'] = keyboard3.get_keyboard()
    elif keyboard == keyboard4:
        post['keyboard'] = keyboard4.get_keyboard()
    else:
        post = post
    session.method('messages.send', post)

# метод получения информации о сообщении
def msg_info(msg_id):
    return session.method('messages.getById', {
        'message_ids': msg_id,
        'extended': 1
    })

# метод получения инфы о пользователе по его айди
def user_info(user_id):
    return session.method('users.get', {
        "user_ids": user_id
    })

# вечный цикл вайл
while 1:

    # секретная команда включения бота
    if ex == 1:

        # проверка трай-эксепт секретного цикла фор на потерю соединения с сервером вк
        try:
            for event in VkLongPoll(session).listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                    text = event.text.lower()  # текст сообщения
                    peer_id = event.peer_id  # универсальный айди чата (для группы, беседы или пользователя)
                    try:  # проверка на наличие айди пользователя
                        user_id = event.user_id  # айди пользователя
                    except AttributeError:  # что бот делает в случае, если его нет
                        continue
                    if 'start' == text:
                        if user_id == 445186298:  # твой айди пользователя
                            write_msg(peer_id, '☕Запуск бота☕')
                            break
        except requests.exceptions.ReadTimeout:
            print('Потеряно соединение с сервером вк в секретном цикле фор')

    # проверка трай-эксепт основного цикла фор на потерю соединения с сервером вк
    try:

        # бот слушает события от сервера вк
        for event in VkLongPoll(session).listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:  # проверка события
                text = event.text.lower()  # текст сообщения
                peer_id = event.peer_id  # универсальный айди чата (для группы, беседы или пользователя)
                try:  # проверка на наличие айди пользователя
                    user_id = event.user_id  # айди пользователя
                except AttributeError:  # что бот делает в случае, если его нет
                    continue
                atchs = event.attachments  # вложения

                # клавиатура выбора бота
                keyboard1 = VkKeyboard()
                keyboard1.add_button('Основной Бот', VkKeyboardColor.POSITIVE)
                keyboard1.add_button('Кликер Бот', VkKeyboardColor.NEGATIVE)

                # клавиатура Основного Бота
                keyboard2 = VkKeyboard()
                keyboard2.add_button('Info')
                keyboard2.add_line()
                keyboard2.add_button('Photo', VkKeyboardColor.POSITIVE)
                keyboard2.add_button('Id', VkKeyboardColor.POSITIVE)
                keyboard2.add_line()
                keyboard2.add_button('Rand', VkKeyboardColor.PRIMARY)
                keyboard2.add_button('Calc', VkKeyboardColor.PRIMARY)
                keyboard2.add_line()
                keyboard2.add_button('Назад', VkKeyboardColor.NEGATIVE)

                # клавиатура Кликер Бота
                keyboard3 = VkKeyboard()
                keyboard3.add_button('Сало', VkKeyboardColor.POSITIVE)
                keyboard3.add_line()
                keyboard3.add_button('Профиль', VkKeyboardColor.PRIMARY)
                keyboard3.add_button('Топ', VkKeyboardColor.PRIMARY)
                keyboard3.add_line()
                keyboard3.add_button('Назад', VkKeyboardColor.NEGATIVE)

                # клавиатура выбора Да или Нет
                keyboard4 = VkKeyboard()
                keyboard4.add_button('✅Да', VkKeyboardColor.POSITIVE)
                keyboard4.add_button('❌Нет', VkKeyboardColor.NEGATIVE)

                # приветствие в ответ на Начать
                if 'начать' == text:
                    user = user_info(user_id)  # получение инфы о пользователе по его айди
                    name = user[0]['first_name'] + ' ' + user[0]['last_name']  # получение имени пользователя
                    if user_id in dict_names1:  # проверка на наличие нового имени у пользователя в словаре
                        name = dict_names1[user_id]  # присвоение нового имени пользователю при наличии его в словаре
                    write_msg(peer_id, f'Добро пожаловать, {name}.\nВыберите бота:', keyboard1)

                # выбор Основного Бота
                elif 'основной бот' == text or 'основной бот' == text[29:41]:
                    write_msg(peer_id,
                              'Основной Бот.\nВыберите кнопку:\nP.s. для вывода информации о кнопках нажмите 👉Info👈.',
                              keyboard2)

                # выбор Кликер Бота
                elif 'кликер бот' == text or 'кликер бот' == text[29:39]:
                    write_msg(peer_id, 'Кликер Бот.\nВыберите кнопку:', keyboard3)

                # переход в меню выбора бота
                elif 'назад' == text or 'назад' == text[29:34]:
                    write_msg(peer_id, 'Выберите бота:', keyboard1)

                # главная инфо команда Бота
                elif 'info' == text or 'info' == text[29:33]:
                    write_msg(peer_id, bot)

                # Калькулятор инфо
                elif 'calc' == text or 'calc' == text[29:33]:
                    write_msg(peer_id, calc)

                # Рандомайзер инфо
                elif 'rand' == text or 'rand' == text[29:33]:
                    write_msg(peer_id, rand)

                # Фотоопределитель инфо
                elif 'photo' == text or 'photo' == text[29:34]:
                    write_msg(peer_id, '📷Фотоопределитель📷\nНапишите 👉Фото👈 вместе с отправкой фотографии, и бот '
                                       'попытается её распознать.\nP.s. пока доступны только фотографии котов, собак '
                                       'и кошкодевочек.')

                # команды Фотоопределителя
                elif 'фото' == text and atchs != {} and atchs['attach1_type'] == 'photo':
                    try:
                        url = 0
                        cat_distance = 0
                        dog_distance = 0
                        neko_distance = 0
                        other_distance = 0
                        user_id1 = event.user_id
                        msg_id = event.message_id
                        info = msg_info(msg_id)
                        sizes = (info['items'][0]['attachments'][0]['photo']['sizes'])
                        s_w = []
                        for size in sizes:
                            width = size['width']
                            s_w.append(width)
                        max_w = max(s_w)
                        min_w = min(s_w)
                        if max_w == min_w:
                            url = sizes[0]['url']
                        else:
                            for size in sizes:
                                width = size['width']
                                if width == max_w:
                                    url = size['url']
                        img = requests.get(
                            url,
                            headers={
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                              "(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
                            }).content
                        with open('photo.jpg', 'wb') as handler:
                            handler.write(img)
                        img = Image.open('photo.jpg')
                        hash1 = str(imagehash.phash(img))
                        file = 'Cats'  # папка с котами (все папки прилагаются)
                        cat_imgs = os.listdir(file)
                        cat_url_imgs = list(map(imgs_urls, cat_imgs))
                        cat_open_imgs = list(map(imgs_open, cat_url_imgs))
                        cat_hashs = list(map(imgs_hashs, cat_open_imgs))
                        cat_distances = list(map(similarity, cat_hashs))
                        file = 'Dogs'  # папка с собаками
                        dog_imgs = os.listdir(file)
                        dog_url_imgs = list(map(imgs_urls, dog_imgs))
                        dog_open_imgs = list(map(imgs_open, dog_url_imgs))
                        dog_hashs = list(map(imgs_hashs, dog_open_imgs))
                        dog_distances = list(map(similarity, dog_hashs))
                        file = 'Nekot'  # папка с неко тян
                        neko_imgs = os.listdir(file)
                        neko_url_imgs = list(map(imgs_urls, neko_imgs))
                        neko_open_imgs = list(map(imgs_open, neko_url_imgs))
                        neko_hashs = list(map(imgs_hashs, neko_open_imgs))
                        neko_distances = list(map(similarity, neko_hashs))
                        file = 'Others'  # папка с пикчами из категории другое
                        other_imgs = os.listdir(file)
                        other_url_imgs = list(map(imgs_urls, other_imgs))
                        other_open_imgs = list(map(imgs_open, other_url_imgs))
                        other_hashs = list(map(imgs_hashs, other_open_imgs))
                        other_distances = list(map(similarity, other_hashs))
                        other_dict = dict(zip(other_hashs, other_imgs))
                        other_dict2 = dict(zip(other_distances, other_imgs))
                        for distance in cat_distances:
                            if distance >= 60:
                                cat_distance += 1
                        for distance in dog_distances:
                            if distance >= 60:
                                dog_distance += 1
                        for distance in neko_distances:
                            if distance >= 60:
                                neko_distance += 1
                        for distance in other_distances:
                            if distance >= 60:
                                other_distance += 1
                        if hash1 in cat_hashs:
                            write_msg(peer_id, 'Это картинка кота.')
                        elif hash1 in dog_hashs:
                            write_msg(peer_id, 'Это картинка собаки.')
                        elif hash1 in neko_hashs:
                            write_msg(peer_id, 'Это картинка кошкодевочки.')
                        elif hash1 in other_hashs:
                            other_name = other_dict[hash1]
                            if '_' in other_name:
                                other_name = other_name[:other_name.index('_')]
                            else:
                                other_name = other_name[:other_name.index('.')]
                            write_msg(peer_id, f'На фото {other_name}.')
                        elif cat_distance >= 1:
                            write_msg(peer_id, 'Бот обнаружил кота на фотографии, это правильно?', keyboard4)
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    if ('✅да' == text or '✅да' == text[29:32]) and user_id2 == user_id1:
                                        cat += 1
                                        dict_values1['cat'] = cat
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                        break
                                    elif ('❌нет' == text or '❌нет' == text[29:33]) and user_id2 == user_id1:
                                        write_msg(peer_id, 'Бот ещё учится, напишите свой вариант того, что на фото.')
                                        for event in VkLongPoll(session).listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                                user_id2 = event.user_id
                                                text = event.text.lower()
                                                other_value = 0
                                                for value in other_dict.values():
                                                    if '_' in value:
                                                        value = value[:value.index('_')]
                                                    else:
                                                        value = value[:value.index('.')]
                                                    if text == value:
                                                        other_value = value
                                                if ('кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in
                                                        text) and user_id2 == user_id1:
                                                    cat += 1
                                                    dict_values1['cat'] = cat
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                                    break
                                                elif ('собак' in text or 'щено' in text or 'пес' in text or 'пёс' in
                                                      text) and user_id2 == user_id1:
                                                    dog += 1
                                                    dict_values1['dog'] = dog
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                                    break
                                                elif ('неко' in text or 'кошкодевочка' == text or 'кошкодевочки' ==
                                                      text) and user_id2 == user_id1:
                                                    neko += 1
                                                    dict_values1['neko'] = neko
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Nekot/neko_{neko}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                                    break
                                                elif text == other_value and user_id2 == user_id1:
                                                    other += 1
                                                    dict_values1['other'] = other
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                                    write_msg(peer_id,
                                                              f'Распознавание фотографий из категории "{text}" '
                                                              f'улучшено.')
                                                    break
                                                elif user_id2 == user_id1:
                                                    other += 1
                                                    dict_values1['other'] = other
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                                       'добавлено в папку с будущими фотографиями для '
                                                                       'распознавания.')
                                                    break
                                                elif ('/' in text or '\\' in text or '"' in text or '<' in text or '>'
                                                      in text or '|' in text or '*' in text or '?' in text or ':' in
                                                      text) and user_id2 == user_id1:
                                                    write_msg(peer_id, 'Нельзя использовать символы /, \\, *, :, ?, <, '
                                                                       '>, |, ".')
                                        break
                        elif dog_distance >= 1:
                            write_msg(peer_id, 'Бот обнаружил собаку на фотографии, это правильно?', keyboard4)
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    if ('✅да' == text or '✅да' == text[29:32]) and user_id2 == user_id1:
                                        dog += 1
                                        dict_values1['dog'] = dog
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                        break
                                    elif ('❌нет' == text or '❌нет' == text[29:33]) and user_id2 == user_id1:
                                        write_msg(peer_id, 'Бот ещё учится, напишите свой вариант того, что на фото.')
                                        for event in VkLongPoll(session).listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                                user_id2 = event.user_id
                                                text = event.text.lower()
                                                other_value = 0
                                                for value in other_dict.values():
                                                    if '_' in value:
                                                        value = value[:value.index('_')]
                                                    else:
                                                        value = value[:value.index('.')]
                                                    if text == value:
                                                        other_value = value
                                                if ('кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in
                                                        text) and user_id2 == user_id1:
                                                    cat += 1
                                                    dict_values1['cat'] = cat
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                                    break
                                                elif ('собак' in text or 'щено' in text or 'пес' in text or 'пёс' in
                                                      text) and user_id2 == user_id1:
                                                    dog += 1
                                                    dict_values1['dog'] = dog
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                                    break
                                                elif ('неко' in text or 'кошкодевочка' == text or 'кошкодевочки' ==
                                                      text) and user_id2 == user_id1:
                                                    neko += 1
                                                    dict_values1['neko'] = neko
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Nekot/neko_{neko}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                                    break
                                                elif text == other_value and user_id2 == user_id1:
                                                    other += 1
                                                    dict_values1['other'] = other
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                                    write_msg(peer_id,
                                                              f'Распознавание фотографий из категории "{text}" '
                                                              f'улучшено.')
                                                    break
                                                elif user_id2 == user_id1:
                                                    other += 1
                                                    dict_values1['other'] = other
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                                       'добавлено в папку с будущими фотографиями для '
                                                                       'распознавания.')
                                                    break
                                                elif ('/' in text or '\\' in text or '"' in text or '<' in text or '>'
                                                      in text or '|' in text or '*' in text or '?' in text or ':' in
                                                      text) and user_id2 == user_id1:
                                                    write_msg(peer_id, 'Нельзя использовать символы /, \\, *, :, ?, <, '
                                                                       '>, |, ".')
                                        break
                        elif neko_distance >= 1:
                            write_msg(peer_id, 'Бот обнаружил кошкодевочку на фотографии, это правильно?', keyboard4)
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    if ('✅да' == text or '✅да' == text[29:32]) and user_id2 == user_id1:
                                        neko += 1
                                        dict_values1['neko'] = neko
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Nekot/neko_{neko}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                        break
                                    elif ('❌нет' == text or '❌нет' == text[29:33]) and user_id2 == user_id1:
                                        write_msg(peer_id, 'Бот ещё учится, напишите свой вариант того, что на фото.')
                                        for event in VkLongPoll(session).listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                                user_id2 = event.user_id
                                                text = event.text.lower()
                                                other_value = 0
                                                for value in other_dict.values():
                                                    if '_' in value:
                                                        value = value[:value.index('_')]
                                                    else:
                                                        value = value[:value.index('.')]
                                                    if text == value:
                                                        other_value = value
                                                if ('кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in
                                                        text) and user_id2 == user_id1:
                                                    cat += 1
                                                    dict_values1['cat'] = cat
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                                    break
                                                elif ('собак' in text or 'щено' in text or 'пес' in text or 'пёс' in
                                                      text) and user_id2 == user_id1:
                                                    dog += 1
                                                    dict_values1['dog'] = dog
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                                    break
                                                elif ('неко' in text or 'кошкодевочка' == text or 'кошкодевочки' ==
                                                      text) and user_id2 == user_id1:
                                                    neko += 1
                                                    dict_values1['neko'] = neko
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Nekot/neko_{neko}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                                    break
                                                elif text == other_value and user_id2 == user_id1:
                                                    other += 1
                                                    dict_values1['other'] = other
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                                    write_msg(peer_id,
                                                              f'Распознавание фотографий из категории "{text}" '
                                                              f'улучшено.')
                                                    break
                                                elif user_id2 == user_id1:
                                                    other += 1
                                                    dict_values1['other'] = other
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                                       'добавлено в папку с будущими фотографиями для '
                                                                       'распознавания.')
                                                    break
                                                elif ('/' in text or '\\' in text or '"' in text or '<' in text or '>'
                                                      in text or '|' in text or '*' in text or '?' in text or ':' in
                                                      text) and user_id2 == user_id1:
                                                    write_msg(peer_id, 'Нельзя использовать символы /, \\, *, :, ?, <, '
                                                                       '>, |, ".')
                                        break
                        elif other_distance >= 1:
                            mnum = max(other_distances)
                            other_name2 = other_dict2[19]
                            if '_' in other_name2:
                                other_name2 = other_name2[:other_name2.index('_')]
                            else:
                                other_name2 = other_name2[:other_name2.index('.')]
                            write_msg(peer_id, f'На фото, возможно {other_name2}, это правильно? Напишите Да или Нет.')
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    if ('✅да' == text or '✅да' == text[29:32]) and user_id2 == user_id1:
                                        other += 1
                                        dict_values1['other'] = other
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                        write_msg(peer_id, f'Распознавание фотографий из категории "{other_name2}" '
                                                           f'улучшено.')
                                        break
                                    elif ('❌нет' == text or '❌нет' == text[29:33]) and user_id2 == user_id1:
                                        write_msg(peer_id, 'Бот ещё учится, напишите свой вариант того, что на фото.')
                                        for event in VkLongPoll(session).listen():
                                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                                user_id2 = event.user_id
                                                text = event.text.lower()
                                                other_value = 0
                                                for value in other_dict.values():
                                                    if '_' in value:
                                                        value = value[:value.index('_')]
                                                    else:
                                                        value = value[:value.index('.')]
                                                    if text == value:
                                                        other_value = value
                                                if ('кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in
                                                        text) and user_id2 == user_id1:
                                                    cat += 1
                                                    dict_values1['cat'] = cat
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                                    break
                                                elif ('собак' in text or 'щено' in text or 'пес' in text or 'пёс' in
                                                      text) and user_id2 == user_id1:
                                                    dog += 1
                                                    dict_values1['dog'] = dog
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                                    break
                                                elif ('неко' in text or 'кошкодевочка' == text or 'кошкодевочки' ==
                                                      text) and user_id2 == user_id1:
                                                    neko += 1
                                                    dict_values1['neko'] = neko
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Nekot/neko_{neko}.jpg')
                                                    write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                                    break
                                                elif text == other_value and user_id2 == user_id1:
                                                    other += 1
                                                    dict_values1['other'] = other
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                                    write_msg(peer_id,
                                                              f'Распознавание фотографий из категории "{text}" '
                                                              f'улучшено.')
                                                    break
                                                elif user_id2 == user_id1:
                                                    other += 1
                                                    dict_values1['other'] = other
                                                    with open('Значения картинок.txt', 'w') as dict_values:
                                                        dict_values.write(str(dict_values1))
                                                    shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                                       'добавлено в папку с будущими фотографиями для '
                                                                       'распознавания.')
                                                    break
                                                elif ('/' in text or '\\' in text or '"' in text or '<' in text or '>'
                                                      in text or '|' in text or '*' in text or '?' in text or ':' in
                                                      text) and user_id2 == user_id1:
                                                    write_msg(peer_id, 'Нельзя использовать символы /, \\, *, :, ?, <, '
                                                                       '>, |, ".')
                                        break
                        else:
                            write_msg(peer_id, 'Бот не смог распознать фотографию.\nНапишите, что же на ней.')
                            for event in VkLongPoll(session).listen():
                                if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                    user_id2 = event.user_id
                                    text = event.text.lower()
                                    other_value = 0
                                    for value in other_dict.values():
                                        if '_' in value:
                                            value = value[:value.index('_')]
                                        else:
                                            value = value[:value.index('.')]
                                        if text == value:
                                            other_value = value
                                    if ('кот' in text or 'кошка' == text or 'кошки' == text or 'кошак' in
                                            text) and user_id2 == user_id1:
                                        cat += 1
                                        dict_values1['cat'] = cat
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Cats/cat_{cat}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                        break
                                    elif ('собак' in text or 'щено' in text or 'пес' in text or 'пёс' in
                                          text) and user_id2 == user_id1:
                                        dog += 1
                                        dict_values1['dog'] = dog
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Dogs/dog_{dog}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                        break
                                    elif ('неко' in text or 'кошкодевочка' == text or 'кошкодевочки' ==
                                          text) and user_id2 == user_id1:
                                        neko += 1
                                        dict_values1['neko'] = neko
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Nekot/neko_{neko}.jpg')
                                        write_msg(peer_id, 'Хорошо, распознавание кошкодевочек улучшилось.')
                                        break
                                    elif text == other_value and user_id2 == user_id1:
                                        other += 1
                                        dict_values1['other'] = other
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                        write_msg(peer_id,
                                                  f'Распознавание фотографий из категории "{text}" '
                                                  f'улучшено.')
                                        break
                                    elif user_id2 == user_id1:
                                        other += 1
                                        dict_values1['other'] = other
                                        with open('Значения картинок.txt', 'w') as dict_values:
                                            dict_values.write(str(dict_values1))
                                        shutil.move('photo.jpg', f'Others/{text}_{other}.jpg')
                                        write_msg(peer_id, 'Бот ещё не научился его(её) распознавать, фото '
                                                           'добавлено в папку с будущими фотографиями для '
                                                           'распознавания.')
                                        break
                                    elif ('/' in text or '\\' in text or '"' in text or '<' in text or '>'
                                          in text or '|' in text or '*' in text or '?' in text or ':' in
                                          text) and user_id2 == user_id1:
                                        write_msg(peer_id, 'Нельзя использовать символы /, \\, *, :, ?, <, '
                                                           '>, |, ".')
                    except requests.exceptions.InvalidURL:
                        write_msg(peer_id, '🚫Ошибка, некорректная ссылка🚫')
                    except PIL.UnidentifiedImageError:
                        write_msg(peer_id, '🚫Ошибка, бот не смог открыть фотографию🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Произошла ошибка со стороны сервера фотографии🚫')
                    except requests.exceptions.ConnectionError:
                        write_msg(peer_id, '🚫Ошибка, не получилось скачать фотографию🚫')

                # работа с именами пользователей:

                # установка нового имени пользователю
                elif 'имя ' == text[:4]:
                    user = user_info(user_id)  # получение инфы о пользователе по его айди
                    name = user[0]['first_name'] + ' ' + user[0]['last_name']  # получение имени пользователя
                    if user_id in dict_names1:  # проверка на наличие нового имени у пользователя в словаре
                        name = dict_names1[user_id]  # присвоение нового имени пользователю при его наличии
                    nick = event.text[4:]
                    dict_names1[user_id] = nick
                    with open('Словарь имён.txt', 'w', encoding='utf-8') as dict_names:
                        dict_names.write(str(dict_names1))
                    write_msg(peer_id, f'@id{user_id} ({name}), ваше новое имя - {nick}.\nЧтобы посмотреть топ '
                                       f'новых имён напишите 👉Имена👈.\nЧтобы удалить новое имя напишите 👉Кик имя👈.')

                # выведение списка новых имён у пользователей
                elif 'имена' == text:
                    s = []
                    for b in dict_names1.items():
                        user = user_info(b[0])
                        username = user[0]['first_name'] + ' ' + user[0]['last_name']
                        s.append(f'@id{b[0]} ({username}) - {b[1]}')
                    top = '\n'.join(s)
                    if top != '':
                        write_msg(peer_id, 'Топ новых имён:\n' + top)
                    else:
                        write_msg(peer_id, 'Нет пользователей с новыми именами.')

                # удаление новго имени пользователя
                elif 'кик имя' == text:
                    try:
                        user = user_info(user_id)  # получение инфы о пользователе по его айди
                        # пользователю при наличии его в словаре
                        nick = dict_names1[user_id]
                        del dict_names1[user_id]
                        with open('Словарь имён.txt', 'w') as dict_names:
                            dict_names.write(str(dict_names1))
                        name = user[0]['first_name'] + ' ' + user[0]['last_name']
                        write_msg(peer_id, f'@id{user_id} ({nick}), теперь вы снова {name}.')
                    except KeyError:
                        write_msg(peer_id, 'У вас и так нет нового имени.')

                # команды Кликер Бота:

                # получение сала на склад
                elif 'сало' == text or 'сало' == text[29:33]:
                    if user_id in dict_klicker1:
                        kg = dict_klicker1[user_id][0]
                    else:
                        kg = 0
                    ran = random.choice(range(100, 1001))
                    kg = round(kg + ran / 1000, 2)
                    sgrn = 185
                    srub = 505.05
                    grn = round(sgrn * kg, 2)
                    rub = round(grn * 2.73, 2)
                    dict_klicker1[user_id] = [kg, grn, rub]
                    with open('Значения кликера.txt', 'w') as dict_klicker:
                        dict_klicker.write(str(dict_klicker1))
                    write_msg(peer_id, f'''Поздравляю! Вы получили {ran} г сала.
    Сала на складе: {kg} кг.
    Цена всего сала на складе: {grn} грн / {rub} ₽.
    Цена за кг: {sgrn} грн / {srub} ₽.''')

                # личный профиль
                elif 'профиль' == text or 'профиль' == text[29:36]:
                    if user_id in dict_klicker1:
                        kg, grn, rub = dict_klicker1[user_id][0:3]
                    else:
                        kg, grn, rub = 0, 0, 0
                    write_msg(peer_id, f'''Ваш ID: {user_id};
    Вы собрали {kg} кг сала общей стоимостью {grn} грн / {rub} ₽.''')

                # топ по количеству сала на складе
                elif 'топ' == text or 'топ' == text[29:32]:
                    if dict_klicker1 != {}:
                        user_idm1 = 0
                        user_idm2 = 0
                        user_idm3 = 0
                        user_idm4 = 0
                        user_idm5 = 0
                        name1 = 0
                        name2 = 0
                        name3 = 0
                        name4 = 0
                        name5 = 0
                        mkg2 = 0
                        mkg3 = 0
                        mkg4 = 0
                        mkg5 = 0
                        skg = []
                        for tup in dict_klicker1.items():
                            kg = tup[1][0]
                            skg.append(kg)
                        skg.sort()
                        lskg = len(skg)
                        mkg1 = skg[-1]
                        for tup in dict_klicker1.items():
                            kg = tup[1][0]
                            if kg == mkg1:
                                user_idm1 = tup[0]
                                if user_idm1 in dict_names1.keys():
                                    name1 = dict_names1[user_idm1]
                                else:
                                    user = user_info(user_idm1)
                                    name1 = user[0]['first_name'] + ' ' + user[0]['last_name']
                        if lskg >= 2:
                            mkg2 = skg[-2]
                            for tup in dict_klicker1.items():
                                kg = tup[1][0]
                                if kg == mkg2:
                                    user_idm2 = tup[0]
                                    if user_idm2 in dict_names1.keys():
                                        name2 = dict_names1[user_idm2]
                                    else:
                                        user = user_info(user_idm2)
                                        name2 = user[0]['first_name'] + ' ' + user[0]['last_name']
                        if lskg >= 3:
                            mkg3 = skg[-3]
                            for tup in dict_klicker1.items():
                                kg = tup[1][0]
                                if kg == mkg3:
                                    user_idm3 = tup[0]
                                    if user_idm3 in dict_names1.keys():
                                        name3 = dict_names1[user_idm3]
                                    else:
                                        user = user_info(user_idm3)
                                        name3 = user[0]['first_name'] + ' ' + user[0]['last_name']
                        if lskg >= 4:
                            mkg4 = skg[-4]
                            for tup in dict_klicker1:
                                kg = tup[1][0]
                                if kg == mkg4:
                                    user_idm4 = tup[0]
                                    if user_idm4 in dict_names1.keys():
                                        name4 = dict_names1[user_idm4]
                                    else:
                                        user = user_info(user_idm4)
                                        name4 = user[0]['first_name'] + ' ' + user[0]['last_name']
                        if lskg >= 5:
                            mkg5 = skg[-5]
                            for tup in dict_klicker1:
                                kg = tup[1][0]
                                if kg == mkg5:
                                    user_idm5 = tup[0]
                                    if user_idm5 in dict_names1.keys():
                                        name5 = dict_names1[user_idm5]
                                    else:
                                        user = user_info(user_idm5)
                                        name5 = user[0]['first_name'] + ' ' + user[0]['last_name']
                        if user_idm2 == 0:
                            write_msg(peer_id, f'''Топ по количеству сала на складе:
    1) @id{user_idm1} ({name1}) - {mkg1} кг сала.''')
                        elif user_idm2 == 0 and user_idm3 == 0:
                            write_msg(peer_id, f'''Топ по количеству сала на складе:
    1) @id{user_idm1} ({name1}) - {mkg1} кг сала;
    2) @id{user_idm2} ({name2}) - {mkg2} кг сала.''')
                        elif user_idm2 == 0 and user_idm3 == 0 and user_idm4 == 0:
                            write_msg(peer_id, f'''Топ по количеству сала на складе:
    1) @id{user_idm1} ({name1}) - {mkg1} кг сала;
    2) @id{user_idm2} ({name2}) - {mkg2} кг сала;
    3) @id{user_idm3} ({name3}) - {mkg3} кг сала.''')
                        elif user_idm2 == 0 and user_idm3 == 0 and user_idm4 == 0 and user_idm5 == 0:
                            write_msg(peer_id, f'''Топ по количеству сала на складе:
    1) @id{user_idm1} ({name1}) - {mkg1} кг сала;
    2) @id{user_idm2} ({name2}) - {mkg2} кг сала;
    3) @id{user_idm3} ({name3}) - {mkg3} кг сала;
    4) @id{user_idm4} ({name4}) - {mkg4} кг сала.''')
                        elif user_idm5 != 0:
                            write_msg(peer_id, f'''Топ по количеству сала на складе:
    1) @id{user_idm1} ({name1}) - {mkg1} кг сала;
    2) @id{user_idm2} ({name2}) - {mkg2} кг сала;
    3) @id{user_idm3} ({name3}) - {mkg3} кг сала;
    4) @id{user_idm4} ({name4}) - {mkg4} кг сала;
    5) @id{user_idm4} ({name4}) - {mkg4} кг сала.''')
                    else:
                        write_msg(peer_id, 'Ещё нет новых пользователей.')

                # работа с разными айди:

                # получение своего айди
                elif 'id' == text or 'id' == text[29:31]:
                    user_id = event.user_id
                    write_msg(peer_id, f'Твой айди: {user_id}')

                # получение чужого айди
                elif 'id ' == text[:3]:
                    try:
                        text = text.replace('id ', '')
                        user = user_info(user_id)
                        ids = user[0]['id']
                        write_msg(peer_id, f'Айди пользователя: {ids}')
                    except vk_api.exceptions.ApiError:
                        write_msg(peer_id, '🚫Ошибка, неправильно введён короткий адрес🚫')

                # получение айди группы
                elif 'group id ' == text[:9]:
                    try:
                        text = text.replace('group id ', '')
                        group = session.method('groups.getById', {
                            "group_id": text
                        })
                        group_id = group[0]['id']
                        write_msg(peer_id, f'Айди группы: {group_id}')
                    except vk_api.exceptions.ApiError:
                        write_msg(peer_id, '🚫Ошибка, неправильно введён короткий адрес🚫')

                # секретная команда выключения Бота
                elif 'exit' == text:
                    if user_id == "СЮДА АЙДИ":  # опять твой айди пользователя🤡
                        write_msg(peer_id, '💤Выключение бота💤')
                        ex = 1
                        break

                # команды Калькулятора
                elif 'реши ' == text[:5]:
                    try:
                        string = text.replace('реши ', '')
                        if ',' in string:
                            string = string.replace(',', '.')
                        b = 'Ответ: ' + str(eval(string))
                        if '.0' == b[-2:]:
                            c = b.replace('.0', '')
                            write_msg(peer_id, c)
                        else:
                            write_msg(peer_id, b)
                    except NameError:
                        write_msg(peer_id, '🚫Ошибка, проверьте пример🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Ошибка, проверьте пример🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Ошибка, проверьте пример🚫')
                    except ZeroDivisionError:
                        write_msg(peer_id, '🚫На 0 делить нельзя🚫')

                # команды Рандомайзера:

                # случайные числа:

                # 1 число
                elif 'ранд ' == text[:5]:
                    try:
                        text = text.replace('ранд ', '').split()
                        d = int(text[0])
                        e = int(text[1])
                        f = range(d, e)
                        g = str(random.choice(f))
                        write_msg(peer_id, 'Рандомное число: ' + g)
                    except ValueError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')
                    except NameError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')
                    except IndexError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Неправильно введён диапазон чисел🚫')

                # несколько чисел
                elif 'несранд' == text[:7]:
                    try:
                        text = text.replace('несранд', '')
                        g = int(text[:text.index(' ')])
                        text = text[text.index(' '):].split()
                        d = int(text[0])
                        e = int(text[1])
                        f = range(d, e)
                        h = str(random.sample(f, g))
                        write_msg(peer_id, 'Рандомные числа: ' + h[1:-1])
                    except ValueError:
                        write_msg(peer_id, '🚫Количество случайных чисел превышает количество чисел в диапазоне, или '
                                           'они неправильно введены🚫')
                    except NameError:
                        write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                    except IndexError:
                        write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')

                # случайные слова:

                # 1 слово
                elif 'сранд' == text[:5]:
                    try:
                        lw = text.replace('сранд ', '').split()
                        rw = random.choice(lw)
                        write_msg(peer_id, 'Случайное слово: ' + rw)
                    except ValueError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')
                    except NameError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')
                    except IndexError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Неправильно введён список слов🚫')

                # несколько слов
                elif 'нессранд' == text[:8]:
                    try:
                        text = text.replace('нессранд', '')
                        n = int(text[:text.index(' ')])
                        lw = text = text[text.index(' '):].split()
                        lrw = str(random.sample(lw, n))[1:-1].replace("'", '')
                        write_msg(peer_id, 'Рандомные слова: ' + lrw)
                    except ValueError:
                        write_msg(peer_id, '🚫Количество случайных слов превышает количество слов в списке, или они '
                                           'неправильно введены🚫')
                    except NameError:
                        write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                    except IndexError:
                        write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                    except TypeError:
                        write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                    except SyntaxError:
                        write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
    except requests.exceptions.ReadTimeout:
        print('Потеряно соединение с сервером вк в основном цикле фор')
