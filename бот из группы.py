from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import requests
import os
import PIL
from PIL import Image
import imagehash
import shutil
from math import e
from math import pi
from math import sqrt
from math import log
from math import sin
from math import cos
from math import tan
from math import factorial as f
mod = abs
dict = {}
# начальное количество сала
k = 0
# превращение картинок в хэш:
def imgs_urls(val):
    return val.replace(val, f'{file}/{val}')
def imgs_open(val):
    return Image.open(val)
def imgs_hashs(val):
    return str(imagehash.phash(val))
# нахождение дистанции Хэйминга
def hamming_distance(hash2) -> int:
    distance = 0
    for i in range(len(hash)):
        if hash[i] != hash2[i]:
            distance += 1
    return distance
# значение картинки кота (значения обозначают номер 
# последней картинки, которую скачал бот, для начала 
# желательно установить значения по 0, если бот отключился 
# после того, как он установил картинки, то меняй значения 
# на номера посдних картинок в папках)🤡
a = 0
# значение картинки собаки (пример на собаках, у меня эта
# папка имеет название Dogs, к примеру, бот скачал 2 картинки и выключился,
# 1 картинка 1.jpg, 2 соответственно 2.jpg, я ставлю значение z = 2🤡
z = 0
# значение картинки неко тян🤡
t = 0
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
1⃣  Сложения или вычитание - 👉+👈 или 
👉-👈;
2⃣  Умножения или деление - 👉*👈 или 
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

session = vk_api.VkApi(token="d260bf5b76f6e1b9bd43be2962f6ae1cf09b2977a9a1ceeacb97987f3a8a7a7e7b56486d1d926e5fbc8e3")
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

for event in VkLongPoll(session).listen():
    try:
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            peer_id = event.peer_id
            user = session.method('users.get', {
                "user_ids": user_id
            })
            name = user[0]['first_name'] + ' ' + user[0]['last_name']
            if user_id in dict:
                name = dict[user_id]
            # клавиатура выбора бота:
            keyboard1 = VkKeyboard()
            keyboard1.add_button('Основной Бот', VkKeyboardColor.POSITIVE)
            keyboard1.add_button('Кликер Бот', VkKeyboardColor.NEGATIVE)
            # клавиатура Основного Бота:
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
            # клавиатура Кликер Бота:
            keyboard3 = VkKeyboard()
            keyboard3.add_button('Сало', VkKeyboardColor.POSITIVE)
            keyboard3.add_line()
            keyboard3.add_button('Профиль', VkKeyboardColor.PRIMARY)
            keyboard3.add_button('Топ', VkKeyboardColor.PRIMARY)
            keyboard3.add_line()
            keyboard3.add_button('Назад', VkKeyboardColor.NEGATIVE)
            # выбор Да или Нет
            keyboard4 = VkKeyboard()
            keyboard4.add_button('✅Да', VkKeyboardColor.POSITIVE)
            keyboard4.add_button('❌Нет', VkKeyboardColor.NEGATIVE)
            # приветствие:
            if 'начать' == text:
                write_msg(peer_id, f'Добро пожаловать, {name}.\nВыберите бота:', keyboard1)
            # выбор Основного Бота:
            elif 'основной бот' == text or 'основной бот' == text[29:41]:
                write_msg(peer_id,
                          'Основной Бот.\nВыберите кнопку:\nP.s. для вывода информации о кнопках нажмите 👉Info👈.',
                          keyboard2)
            # выбор Кликер Бота:
            elif 'кликер бот' == text or 'кликер бот' == text[29:39]:
                write_msg(peer_id, 'Кликер Бот.\nВыберите кнопку:', keyboard3)
            # переход в меню выбора бота:
            elif 'назад' == text or 'назад' == text[29:34]:
                write_msg(peer_id, 'Выберите бота:', keyboard1)
            # главная инфо команда Бота:
            elif 'info' == text or 'info' == text[29:33]:
                write_msg(peer_id, bot)
            # первая подглавная инфо команда Бота:
            elif 'calc' == text or 'calc' == text[29:33]:
                write_msg(peer_id, calc)
            # вторая подглавная инфо команда Бота:
            elif 'rand' == text or 'rand' == text[29:33]:
                write_msg(peer_id, rand)
            # фотоопределитель
            elif 'photo' == text:
                write_msg(peer_id, '📷Фотоопределитель📷\nНапишите Фото 👉ссылка на фотографию👈, и бот попытается '
                                   'распознать, что на фотографии.\nP.s. пока доступны только фотографии котов, собак '
                                   'и неко тян.')
            elif 'фото http' == text[:9] or 'фото\nhttp' == text[:8]:
                try:
                    cat_distance = 0
                    dog_distance = 0
                    neko_distance = 0
                    text = event.text[5:]
                    if 'amp;' in text:
                        url = text.replace('amp;', '')
                    else:
                        url = text
                    img = requests.get(
                        url,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                          "(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
                        }).content
                    with open('photo.jpg', 'wb') as handler:
                        handler.write(img)
                    img = Image.open('photo.jpg')
                    hash = str(imagehash.phash(img))
                    file = 'Cats' # название папки с котами (у меня все эти папки находятся тут 
                    # C:\Users\Dmitriy\PycharmProjects\pythonProject в конце pythonProject - это 
                    # название рабочей папки, где находятся все твои программы) 🤡
                    cat_imgs = os.listdir(file)
                    cat_imgs = list(map(imgs_urls, cat_imgs))
                    cat_imgs = list(map(imgs_open, cat_imgs))
                    cat_hashs = list(map(imgs_hashs, cat_imgs))
                    cat_distances = list(map(hamming_distance, cat_hashs))
                    file = 'Dogs' # название папки с собаками 🤡
                    dog_imgs = os.listdir(file)
                    dog_imgs = list(map(imgs_urls, dog_imgs))
                    dog_imgs = list(map(imgs_open, dog_imgs))
                    dog_hashs = list(map(imgs_hashs, dog_imgs))
                    dog_distances = list(map(hamming_distance, dog_hashs))
                    file = 'Neko' # название папки с неко тян 🤡
                    neko_imgs = os.listdir(file)
                    neko_imgs = list(map(imgs_urls, neko_imgs))
                    neko_imgs = list(map(imgs_open, neko_imgs))
                    neko_hashs = list(map(imgs_hashs, neko_imgs))
                    neko_distances = list(map(hamming_distance, neko_hashs))
                    for distance in cat_distances:
                        if distance <= 10:
                            cat_distance += 1
                    for distance in dog_distances:
                        if distance <= 10:
                            dog_distance += 1
                    for distance in neko_distances:
                        if distance <= 10:
                            neko_distance += 1
                    if hash in cat_hashs:
                        write_msg(peer_id, 'Это картинка кота.')
                    elif hash in dog_hashs:
                        write_msg(peer_id, 'Это картинка собаки.')
                    elif hash in neko_hashs:
                        write_msg(peer_id, 'Это картинка неко тян.')
                    elif cat_distance >= 1:
                        write_msg(peer_id, 'Бот обнаружил кота на фотографии, это правильно?', keyboard4)
                        for event in VkLongPoll(session).listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                text = event.text.lower()
                                peer_id = event.peer_id
                                if '✅да' == text or '✅да' == text[29:32]:
                                    a += 1
                                    shutil.move('photo.jpg', f'Cats/cat_{a}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.', keyboard2)
                                    break
                                elif '❌нет' == text or '❌нет' == text[29:33]:
                                    write_msg(peer_id, 'Бот ещё учится, но вы можете его развить, отправив ещё одну '
                                                       'фотографию.', keyboard2)
                                    break
                    elif dog_distance >= 1:
                        write_msg(peer_id, 'Бот обнаружил собаку на фотографии, это правильно?', keyboard4)
                        for event in VkLongPoll(session).listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                text = event.text.lower()
                                peer_id = event.peer_id
                                if '✅да' == text or '✅да' == text[29:32]:
                                    z += 1
                                    shutil.move('photo.jpg', f'Dogs/dog_{z}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.', keyboard2)
                                    break
                                elif '❌нет' == text or '❌нет' == text[29:33]:
                                    write_msg(peer_id, 'Бот ещё учится, но вы можете его развить, отправив ещё одну '
                                                       'фотографию.', keyboard2)
                                    break
                    elif neko_distance >= 1:
                        write_msg(peer_id, 'Бот обнаружил неко тян на фотографии, это правильно?', keyboard4)
                        for event in VkLongPoll(session).listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                text = event.text.lower()
                                peer_id = event.peer_id
                                if '✅да' == text or '✅да' == text[29:32]:
                                    t += 1
                                    shutil.move('photo.jpg', f'Neko/neko_{t}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание неко тян улучшилось.', keyboard2)
                                    break
                                elif '❌нет' == text or '❌нет' == text[29:33]:
                                    write_msg(peer_id, 'Бот ещё учится, но вы можете его развить, отправив ещё одну '
                                                       'фотографию.', keyboard2)
                                    break
                    else:
                        write_msg(peer_id, 'Бот не смог распознать того, кто находится на фотографии.\nНапишите сами.')
                        for event in VkLongPoll(session).listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                text = event.text.lower()
                                peer_id = event.peer_id
                                if 'кот' in text or 'кошка' == text:
                                    a += 1
                                    shutil.move('photo.jpg', f'Cats/cat_{a}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.', keyboard2)
                                    break
                                elif 'собак' in text or 'щено' in text or 'пес' in text or 'пёс' in text:
                                    z += 1
                                    shutil.move('photo.jpg', f'Dogs/dog_{z}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.', keyboard2)
                                    break
                                elif 'неко' in text or 'кошкодевочка' == text:
                                    t += 1
                                    shutil.move('photo.jpg', f'Neko/neko_{t}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание неко тян улучшилось.', keyboard2)
                                    break
                                else:
                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать.', keyboard2)
                                    break
                except requests.exceptions.InvalidURL:
                    write_msg(peer_id, '🚫Ошибка, некорректная ссылка🚫')
                except PIL.UnidentifiedImageError:
                    write_msg(peer_id, '🚫Ошибка, бот не смог открыть фотографию🚫')
                except TypeError:
                    write_msg(peer_id, '🚫Произошла ошибка со стороны сервера фотографии🚫')
                except requests.exceptions.ConnectionError:
                    write_msg(peer_id, '🚫Ошибка, не получилось скачать фотографию🚫')
            # имена
            elif 'имя ' == text[:4]:
                nick = event.text[4:]
                dict[user_id] = nick
                write_msg(peer_id, f'@id{user_id} ({name}), ваше новое имя - {nick}.\nЧтобы посмотреть топ новых имён '
                                   f'напишите\n👉Имена👈.\nЧтобы удалить новое имя напишите 👉Кик имя👈.')
            elif 'имена' == text:
                s = []
                for b in dict.items():
                    user = session.method('users.get', {
                        "user_ids": b[0]
                    })
                    username = user[0]['first_name'] + ' ' + user[0]['last_name']
                    s.append(f'@id{b[0]} ({username}) - {b[1]}')
                top = '\n'.join(s)
                write_msg(peer_id, 'Топ новых имён:\n' + top)
            elif 'кик имя' == text:
                try:
                    nick = dict[user_id]
                    name = user[0]['first_name'] + ' ' + user[0]['last_name']
                    del dict[user_id]
                    write_msg(peer_id, f'@id{user_id} ({nick}), теперь вы снова {name}.')
                except KeyError:
                    write_msg(peer_id, 'У вас и так нет нового имени.')
            # команды Кликер Бота:
            # сало:
            elif 'сало' == text or 'сало' == text[29:33]:
                o = random.choice(range(100, 1001))
                k = round(k + o / 1000, 2)
                m = 185
                n = 505.05
                l = round(m * k, 2)
                p = round(l * 2.73, 2)
                write_msg(peer_id, f'''Поздравляю! Вы получили {o} г сала.
Сала на складе: {k} кг.
Цена всего сала на складе: {l} грн / {p} ₽.
Цена за кг: {m} грн / {n} ₽.''')
            # профиль:
            elif 'профиль' == text or 'профиль' == text[29:36]:
                write_msg(peer_id, f'''Ваш ID: {user_id}
Вы собрали {k} кг сала''')
            # топ:
            elif 'топ' == text or 'топ' == text[29:32]:
                write_msg(peer_id, f'''Топ по количеству сала на складе:
1) @id{user_id} ({name}) - {k} кг сала''')
            # свой айди:
            elif 'id' == text or 'id' == text[29:31]:
                user_id = event.user_id
                write_msg(peer_id, f'Твой айди: {user_id}')
            # чужой айди:
            elif 'id ' == text[:3]:
                try:
                    text = text.replace('ids ', '')
                    user = session.method('users.get', {
                        "user_ids": text
                    })
                    id = user[0]['id']
                    write_msg(peer_id, f'Айди пользователя: {id}')
                except vk_api.exceptions.ApiError:
                    write_msg(peer_id, '🚫Ошибка, неправильно введён короткий адрес🚫')
            # айди группы:
            elif 'group id ' == text[:9]:
                try:
                    text = text.replace('group id ', '')
                    group = session.method('groups.getById', {
                        "group_id": text
                    })
                    id = group[0]['id']
                    write_msg(peer_id, f'Айди группы: {id}')
                except vk_api.exceptions.ApiError:
                    write_msg(peer_id, '🚫Ошибка, неправильно введён короткий адрес🚫')
            # секретная команда выключения Бота
            elif 'exit' == text:
                user_id = event.user_id
                if user_id == # сюда вставь свой user id без # в начале🤡':
                    write_msg(# сюда тоже свой user id без #, '💤Выключение бота💤')
                    break
            # команда Калькулятора:
            elif 'реши ' == text[:5]:
                try:
                    string = text.replace('реши ', '')
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
            # 1 число:
            elif 'ранд ' == text[:5]:
                try:
                    text = text.replace('ранд ', '')
                    d = int(text[:text.index(' ')])
                    g = int(text[text.index(' '):].replace(' ', ''))
                    h = range(d, g)
                    i = str(random.choice(h))
                    write_msg(peer_id, 'Рандомное число: ' + i)
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
            # несколько чисел:
            elif 'несранд' == text[:7]:
                try:
                    text = text.replace('несранд', '')
                    d = int(text[:text.index(' ')])
                    text = text[text.index(' '):]
                    text = text.strip()
                    g = int(text[:text.index(' ')])
                    h = int(text[text.index(' '):].replace(' ', ''))
                    i = range(g, h)
                    j = str(random.sample(i, d))
                    write_msg(peer_id, 'Рандомные числа: ' + h[1:-1])
                except ValueError:
                    write_msg(peer_id, '🚫Количество случайных чисел превышает количество чисел в диапазоне, или они '
                                       'неправильно введены🚫')
                except NameError:
                    write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                except IndexError:
                    write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                except TypeError:
                    write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
                except SyntaxError:
                    write_msg(peer_id, '🚫Неправильно введены диапазон чисел или количество случайных чисел🚫')
            # случайные слова:
            # 1 слово:
            elif 'сранд ' == text[:6]:
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
            # несколько слов:
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
    except Exception as aboba:
        peer_id = event.peer_id
        write_msg(peer_id, f'🚫Произошла ошибка{aboba}🚫')
