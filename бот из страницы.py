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
# превращение картинок в хэш:
def imgs_urls(a):
    return a.replace(a, f'{file}/{a}')
def imgs_open(a):
    return Image.open(a)
def imgs_hashs(a):
    return str(imagehash.phash(a))
# нахождение дистанции Хэйминга
def hamming_distance(hash2) -> int:
    distance = 0
    for i in range(len(hash)):
        if hash[i] != hash2[i]:
            distance += 1
    return distance
# значение картинки кота
a = 16
# значение картинки собаки
z = 3
# значение картинки неко тян
t = 2
bot = '''🤖 Бот 🤖
Доступные команды бота:
1⃣  Для функции Фотоопределитель нажмите 
👉Photo👈;
2⃣  Для функции Калькулятор напишите 👉Calc👈;
3⃣  Для функции Рандомайзер напишите 👉Rand👈;
4⃣  Для того, чтобы поменять своё имя, напишите Имя 👉Новое имя👈;
5⃣  Для того, чтобы узнать свой числовой id, напишите 👉Id👈;
6⃣  Для того, чтобы узнать чужой числовой id, напишите 
Id 👉короткий адрес👈;
7⃣  Для того, чтобы узнать числовой id группы, напишите 
Group id 👉короткий адрес👈.
❗P.s. короткий адрес указывайте без @.'''

calc = '''❎ Калькулятор ❎
Доступные операторы и особые числа:
1⃣  Для сложения или вычитания напишите 👉+👈 или 
👉-👈;
2⃣  Для умножения или деления напишите 👉*👈 или 👉/👈;
3⃣  Для нахождения остатка или целой части от деления напишите 👉%👈 или 👉//👈;
4⃣  Для возведения в степень напишите 👉**👈;
5⃣  Для выведения квадратного корня из числа напишите 
👉sqrt(число)👈;
6⃣  Для нахождения обычного или натурального логарифма из числа напишите 
👉log(число, основание)👈 или 👉log(число)👈;
7⃣ Для написания чисел е или Пи используйте 👉e👈 или 
👉pi👈;
8⃣  Для написания синуса, косинуса или тангенса используйте 👉sin(радианы)👈 или 👉cos(радианы)👈 или 
👉tan(радианы)👈;
9⃣  Для написания факториала из числа напишите 
👉f(число)👈;
🔟 Для написания модуля из числа напишите 
👉mod(число)👈.
❗P.s. для ввода примера напишите: Реши 👉пример👈.'''

rand = '''❓ Рандомайзер ❓
Доступные команды рандомайзера:
1⃣  Для выбора одного случайного числа из диапазона от 1 до 2 числа используйте команду 
👉ранд 1 число 2 число👈;
2⃣  Для выбора нескольких случайных чисел(3 число) из диапазона от 1 до 2 числа используйте команду 
👉несранд3 число 1 число 2 число👈;
3⃣  Для выбора случайного слова из списка слов используйте команду 
👉cранд 1 слово 2 слово и т.д.👈;
4⃣  Для выбора нескольких случайных слов(Число) из списка слов используйте команду 
👉несcрандЧисло 1 слово 2 слово и т.д.👈.
❗P.s. случайные числа или слова не повоторяются, поэтому их количество не должно превышать 
количество чисел или слов в диапазоне или списке; числа в диапазоне пишутся от и до, например, от 1 до 
10 - это числа с 1 по 9.'''

session = vk_api.VkApi(token="сюда вставь свой токен")
def write_msg(peer_id, message):
    session.method('messages.send', {
        'peer_id': peer_id,
        'message': message,
        'random_id': 0,
    })
for event in VkLongPoll(session).listen():
    try:
        if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
            text = event.text.lower()
            peer_id = event.peer_id
            user_id = event.user_id
            user = session.method('users.get', {
                "user_ids": user_id
            })
            name = user[0]['first_name'] + ' ' + user[0]['last_name']
            if user_id in dict:
                name = dict[user_id]
            # главная инфо команда Бота:
            if 'bot' == text:
                write_msg(peer_id, f'{name}, бот вас приветсвует.\n' + bot)
            # первая подглавная инфо команда Бота:
            elif 'calc' == text:
                write_msg(peer_id, calc)
            # вторая подглавная инфо команда Бота:
            elif 'rand' == text:
                write_msg(peer_id, rand)
            elif 'photo' in text[:5] or 'photo' in text[29:34]:
                write_msg(peer_id,
                          '📷Фотоопределитель📷\nНапишите Фото 👉ссылка на фотографию👈, и бот попытается распознать, '
                          'что на фотографии.\nP.s. пока доступны только фотографии котов, собак и неко тян.')
            elif 'фото http' in text[:9] or 'фото\nhttp' in text[:8]:
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
                    file = 'Cats'
                    cat_imgs = os.listdir(file)
                    cat_imgs = list(map(imgs_urls, cat_imgs))
                    cat_imgs = list(map(imgs_open, cat_imgs))
                    cat_hashs = list(map(imgs_hashs, cat_imgs))
                    cat_distances = list(map(hamming_distance, cat_hashs))
                    file = 'Dogs'
                    dog_imgs = os.listdir(file)
                    dog_imgs = list(map(imgs_urls, dog_imgs))
                    dog_imgs = list(map(imgs_open, dog_imgs))
                    dog_hashs = list(map(imgs_hashs, dog_imgs))
                    dog_distances = list(map(hamming_distance, dog_hashs))
                    file = 'Neko'
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
                        write_msg(peer_id, 'На вашей фотографии кот? Напишите ✅да или ❌нет.')
                        for event in VkLongPoll(session).listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                text = event.text.lower()
                                peer_id = event.peer_id
                                if '✅да' in text[:3] or '✅да' in text[29:32]:
                                    a += 1
                                    shutil.move('photo.jpg', f'Cats/cat_{a}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                    break
                                elif '❌нет' in text[:4] or '❌нет' in text[29:33]:
                                    write_msg(peer_id, 'Бот ещё учится, но вы можете его развить, отправив ещё одну '
                                                       'фотографию.')
                                    break
                    elif dog_distance >= 1:
                        write_msg(peer_id, 'На вашей фотографии собака? Напишите ✅да или ❌нет.')
                        for event in VkLongPoll(session).listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                text = event.text.lower()
                                peer_id = event.peer_id
                                if '✅да' in text[:3] or '✅да' in text[29:32]:
                                    z += 1
                                    shutil.move('photo.jpg', f'Dogs/dog_{z}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                    break
                                elif '❌нет' in text[:4] or '❌нет' in text[29:33]:
                                    write_msg(peer_id, 'Бот ещё учится, но вы можете его развить, отправив ещё одну '
                                                       'фотографию.')
                                    break
                    elif neko_distance >= 1:
                        write_msg(peer_id, 'На вашей фотографии неко тян? Напишите ✅да или ❌нет.')
                        for event in VkLongPoll(session).listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                                text = event.text.lower()
                                peer_id = event.peer_id
                                if '✅да' in text[:3] or '✅да' in text[29:32]:
                                    t += 1
                                    shutil.move('photo.jpg', f'Neko/neko_{t}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание неко тян улучшилось.')
                                    break
                                elif '❌нет' in text[:4] or '❌нет' in text[29:33]:
                                    write_msg(peer_id, 'Бот ещё учится, но вы можете его развить, отправив ещё одну '
                                                       'фотографию.')
                                    break
                    else:
                        write_msg(peer_id, 'Бот не смог распознать того, кто находится на фотографии.\nНапишите сами.')
                        for event in VkLongPoll(session).listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.to_me or event.from_me:
                                text = event.text.lower()
                                peer_id = event.peer_id
                                if 'кот' in text or 'кошка' == text:
                                    a += 1
                                    shutil.move('photo.jpg', f'Cats/cat_{a}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание котов улучшилось.')
                                    break
                                elif 'собак' in text[:5] or 'щено' in text[:4]:
                                    z += 1
                                    shutil.move('photo.jpg', f'Dogs/dog_{z}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание собак улучшилось.')
                                    break
                                elif 'неко' in text or 'кошкодевочка' == text:
                                    t += 1
                                    shutil.move('photo.jpg', f'Neko/neko_{t}.jpg')
                                    write_msg(peer_id, 'Хорошо, распознавание неко тян улучшилось.')
                                    break
                                else:
                                    write_msg(peer_id, 'Бот ещё не научился его(её) распознавать.')
                                    break
                except requests.exceptions.InvalidURL:
                    write_msg(peer_id, '🚫Ошибка, некорректная ссылка🚫')
                except PIL.UnidentifiedImageError:
                    write_msg(peer_id, '🚫Ошибка, бот не смог открыть фотографию🚫')
                except TypeError:
                    write_msg(peer_id, '🚫Ошибка на стороне вк🚫')
                except requests.exceptions.ConnectionError:
                    write_msg(peer_id, '🚫Ошибка, не получилось скачать фотографию🚫')
            # имена
            elif 'имя ' in text[:4].lower():
                nick = event.text[4:]
                dict[user_id] = nick
                write_msg(peer_id, f'@id{user_id} ({name}), ваше новое имя - {nick}.\nЧтобы посмотреть топ новых имён '
                                   f'напишите 👉Имена👈.\nЧтобы удалить новое имя напишите 👉Кик имя👈.')
            elif 'имена' in text[:5]:
                s = []
                for b in dict.items():
                    user = session.method('users.get', {
                        "user_ids": b[0]
                    })
                    username = user[0]['first_name'] + ' ' + user[0]['last_name']
                    s.append(f'@id{b[0]} ({username}) - {b[1]}')
                top = '\n'.join(s)
                write_msg(peer_id, 'Топ новых имён:\n' + top)
            elif 'кик имя' in text[:7]:
                try:
                    nick = dict[user_id]
                    name = user[0]['first_name'] + ' ' + user[0]['last_name']
                    del dict[user_id]
                    write_msg(peer_id, f'@id{user_id} ({nick}), теперь вы снова {name}.')
                except KeyError:
                    write_msg(peer_id, 'У вас и так нет нового имени.')
            # свой айди
            elif 'id' == text:
                write_msg(peer_id, f'Твой айди: {user_id}')
            # чужой айди
            elif 'id ' in text[:3]:
                try:
                    text = text.replace('id ', '')
                    user = session.method('users.get', {
                        "user_ids": text
                    })
                    id = user[0]['id']
                    write_msg(peer_id, f'Айди пользователя: {id}')
                except vk_api.exceptions.ApiError:
                    write_msg(peer_id, '🚫Ошибка, неправильно введён короткий адрес🚫')
            # айди группы
            elif 'group id ' in text[:9]:
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
                if user_id == 445186298:
                    write_msg(445186298, '💤Выключение бота💤')
                    break
            # команда Калькулятора:
            elif 'реши ' in text[:5]:
                try:
                    string = text.replace('реши ', '')
                    b = 'Ответ: ' + str(eval(string))
                    if '.0' in b[-2:]:
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
            elif 'ранд ' in text[:5]:
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
            # несколько чисел:
            elif 'несранд' in text[:7]:
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
            elif 'сранд' in text[:5]:
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
            elif 'нессранд' in text[:8]:
                try:
                    text = text.replace('нессранд', '')
                    n = int(text[:text.index(' ')])
                    lw = text = text[text.index(' '):].split()
                    lrw = str(random.sample(lw, n))[1:-1].replace("'", '')
                    write_msg(peer_id, 'Рандомные слова: ' + lrw)
                except ValueError:
                    write_msg(peer_id, '🚫Количество случайных слов превышает количество слов в списке, или они неправильно '
                                       'введены🚫')
                except NameError:
                    write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                except IndexError:
                    write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                except TypeError:
                    write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
                except SyntaxError:
                    write_msg(peer_id, '🚫Неправильно введены список слов или количество случайных слов🚫')
    except Exception as aboba:
        print(aboba)
