from vkbottle import Keyboard, KeyboardButtonColor, \
    Text, OpenLink, Location, EMPTY_KEYBOARD
from vkbottle.bot import Bot, Message

token = "vk1.a.jHUAjp2YYMIW_E0ZQpW2wSFgOBQNrZri-C2eW-DQ7HsYlnWbnt8OLYzi_apJUikWFT1QGgKAh1OW3xwUNUmPIz1sfKO-w6r4kDwNU9d-1JOYMNWqfL7Qr3xWKQlEQ9wFoA5OH5rlv9ihekWhhnqRYKgLwq90z652L88kaIbxU-wesT5v3xnL8EaGWcEcjtJA"
bot = Bot(token=token)


@bot.on.message(text=["Привет", "привет"])
async def handler(message: Message):
    keyboard = Keyboard(one_time=True, inline=False)
    keyboard.add(Text("Cтарт"), color=KeyboardButtonColor.NEGATIVE)
    await message.answer(
        "Приветствую тебя, дорогой друг!😃 Предлагаю тебе пройти тест по физике, которай состоит из 10 вопросов. Если ты готов, нажми кнопку 'Старт'. Удачи!",
        keyboard=keyboard)


@bot.on.message(text="Cтарт")
async def handler(message: Message):
    s = Keyboard(one_time=True)
    s.add(Text("Пушкин"), color=KeyboardButtonColor.NEGATIVE)
    s.add(Text("Тютчев"),color=KeyboardButtonColor.PRIMARY)
    s.row()
    s.add(Text("Маяковский"), color=KeyboardButtonColor.POSITIVE)
    s.add(Text("Ломоносов"))
    await message.answer("Погнали!")
    await message.answer("Первый вопрос:")
    await message.answer(
        "О нем наш великий поэт А.С. Пушкин сказал, что он создал первый в России  университет, что «он, лучше сказать, сам был первым русским университетом».О ком эти слова?🤔",
        keyboard=s)


@bot.on.message(text="Ломоносов")
async def message_handler(message: Message):
    d =  Keyboard()
    d.add(Text("Архимед"), color=KeyboardButtonColor.NEGATIVE)
    d.add(Text("Пифагор"), color=KeyboardButtonColor.PRIMARY)
    d.row()
    d.add(Text("Птолемей"), color=KeyboardButtonColor.POSITIVE)
    d.add(Text("Цезарь"))

    await message.answer(f"Правильный ответ! Молодец!😃")
    await message.answer(f"Второй вопрос:")
    await message.answer(f"О каком ученом говорят, что «он первым стал работать на войну и пал жертвой войны»?", keyboard=d)


@bot.on.message(text="Архимед")
async def message_handler(message: Message):
    f = Keyboard()
    f.add(Text("Ньютон"), color=KeyboardButtonColor.NEGATIVE)
    f.add(Text("Эйнштейн"), color=KeyboardButtonColor.PRIMARY)
    f.row()
    f.add(Text("Галилей"), color=KeyboardButtonColor.POSITIVE)
    f.add(Text("Вольт"))


    await message.answer(f"Правильный ответ! Молодец!😃")
    await message.answer(f"Третий вопрос:")
    await message.answer(f" Один великий физик был приглашен в гости. Сидя в гостиной, он заметил, что два кресла около него пустуют: никто не смел в них сесть.-«Сядьте около меня», - смеясь, попросил он хозяина дома, - «А то мне кажется, что я в Прусской Академии наук.В 1922 году ему была присуждена Нобелевская премия за заслуги в области математической физики (и, особо, за открытие закона фотоэлектрического эффекта).Кто этот великий физик?🤔",keyboard=f)


@bot.on.message(text="Эйнштейн")
async def message_handler(message: Message):
    g = Keyboard()
    g.add(Text("Томсон"), color=KeyboardButtonColor.NEGATIVE)
    g.add(Text("Яблочкин"), color=KeyboardButtonColor.PRIMARY)
    g.row()
    g.add(Text("Эдисон"), color=KeyboardButtonColor.POSITIVE)
    g.add(Text("Кюри"))


    await message.answer(f"Правильный ответ! Молодец!😃")
    await message.answer(f"Четвёртый вопрос:")
    await message.answer(f"Говорят, что этот ученый принялся за одно из своих великих изобретений после скандала с газовой компанией. «Вы имеете большой долг за газовое освещение», - заявила газовая компания и отключила газ. «А я и без вас обойдусь», - возмутился ученый  и изобрел электрическую лампочку. Назовите фамилию ученого.🤔",keyboard=g)


@bot.on.message(text="Эдисон")
async def message_handler(message: Message):
    h = Keyboard()
    h.add(Text("Гамма лучи"), color=KeyboardButtonColor.NEGATIVE)
    h.add(Text("Бета лучи"), color=KeyboardButtonColor.PRIMARY)
    h.row()
    h.add(Text("Рентгеновские лучи"), color=KeyboardButtonColor.POSITIVE)
    h.add(Text("Альфа лучи"))


    await message.answer(f"Правильный ответ! Молодец!😃")
    await message.answer(f"Пятый вопрос:")
    await message.answer(f" Этот человек является первым лауреатом Нобелевской премии по физике. В 1901 году ему была присуждена Нобелевская премия за открытие (лучи), которое носит его имя. Назовите его открытие.🤔", keyboard=h)


@bot.on.message(text="Рентгеновские лучи")
async def message_handler(message: Message):
     j = Keyboard()
     j.add(Text("Динамит"), color=KeyboardButtonColor.NEGATIVE)
     j.add(Text("Атомная бомба"), color=KeyboardButtonColor.PRIMARY)
     j.row()
     j.add(Text("Ядерная бомба"), color=KeyboardButtonColor.POSITIVE)
     j.add(Text("Водородная бомба"))

     await message.answer(f"Правильный ответ! Молодец!😃")
     await message.answer(f"Шестой вопрос:")
     await message.answer(f"Альфред Нобель был известным инженером и изобретателем, выдающимся предпринимателем и финансистом. Он в совершенстве владел пятью языками. В 1968 году он был награжден медалью Шведской академии наук. По своим убеждениям он был ярым пацифистом (сторонником мира) и в 1905 году писал: «Мои открытия скорее прекратят войны, чем ваши конгрессы в защиту мира. Когда враждующие стороны обнаружат, что они в один миг могут уничтожить друг друга, люди откажутся от этих ужасов и от ведения войны». Какое открытие сделал Альфред Нобель?🤔", keyboard=j)


@bot.on.message(text="Динамит")
async def message_handler(message: Message):
    k =  Keyboard()
    k.add(Text("Фарадей"), color=KeyboardButtonColor.NEGATIVE)
    k.add(Text("Эрстед"), color=KeyboardButtonColor.PRIMARY)
    k.row()
    k.add(Text("Попов"), color=KeyboardButtonColor.POSITIVE)
    k.add(Text("Столяров"))

    await message.answer(f"Правильный ответ! Молодец!😃")
    await message.answer(f"Седьмой вопрос:")
    await message.answer(f"В 1909 году Нобелевская премия по физике была присуждена итальянцу Гильельмо Маркони за работы по созданию беспроволочного телеграфа. На самом же деле первым это открытие сделал другой человек – русский физик и электротехник. У нас его имя известно каждому. Назовите его фамилию🤔", keyboard=k)


@bot.on.message(text="Попов")
async def message_handler(message: Message):
    z = Keyboard()
    z.add(Text("Постулаты Бора"), color=KeyboardButtonColor.NEGATIVE)
    z.add(Text("Фотоэффект"), color=KeyboardButtonColor.PRIMARY)
    z.row()
    z.add(Text("Теория струн"), color=KeyboardButtonColor.POSITIVE)
    z.add(Text("Теория электронов"))

    await message.answer(f"Правильный ответ! Молодец!😃")
    await message.answer(f"Восьмой вопрос:")
    await message.answer(f"Какая теория объясняет гравитацию на квантовом уровне?", keyboard=z)


@bot.on.message(text="Теория струн")
async def message_handler(message: Message):
     x = Keyboard()
     x.add(Text("Кот"), color=KeyboardButtonColor.NEGATIVE)
     x.add(Text("Собака"), color=KeyboardButtonColor.PRIMARY)
     x.row()
     x.add(Text("Хомяк"), color=KeyboardButtonColor.POSITIVE)
     x.add(Text("Попугай"))

     await message.answer(f"Правильный ответ! Молодец!😃")
     await message.answer(f"Девятый вопрос:")
     await message.answer(f"Какое животное ассоциируется с фамилией ученого Шрёдингера?", keyboard=x)


@bot.on.message(text="Кот")
async def message_handler(message: Message):
     c = Keyboard()
     c.add(Text("Сахаров"), color=KeyboardButtonColor.NEGATIVE)
     c.add(Text("Резерфорд"), color=KeyboardButtonColor.PRIMARY)
     c.row()
     c.add(Text("Герц"), color=KeyboardButtonColor.POSITIVE)
     c.add(Text("Тесла"))

     await message.answer(f"Правильный ответ! Молодец!😃")
     await message.answer("И так, десятый вопрос:")
     await message.answer(f"Какой знаменитый физик, будучи всю жизнь физиком, получил 'Нобелевскую премию' по химии в 1908 году?", keyboard=c)


@bot.on.message(text="Резерфорд")
async def message_handler(message: Message):
    v = Keyboard(one_time=True)
    v.add(Text("Я"), color=KeyboardButtonColor.POSITIVE)


    await message.answer(f"Правильный ответ! Молодец!😃")
    await message.answer(f"Бонусный вопрос")
    await message.answer(f"Кто крутой и на всё ответил?!😃", keyboard=v)


@bot.on.message(text="Я")
async def message_handler(message: Message):
      await message.answer(f"Вау! Ты ответил на все вопросы, да ты настоящий физик! Умница❤")
      await message.answer(f"Посвящаю тебя в почётные ряды физфака, да прибудет с тобой сила!😃")
      await message.answer(attachment="photo-214436936_457239018")




@bot.on.message()
async def message_handler(message: Message):
      await message.answer(f"Неправильный ответ! Попробуй ещё раз, я уверен, у тебя всё получится!😃")



bot.run_forever()
