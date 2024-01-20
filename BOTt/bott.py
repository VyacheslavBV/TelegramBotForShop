from aiogram import Bot, executor, Dispatcher, types

token = "6345377534:AAFuvS4VbxfwBh-GlXMtCPQhR3gGzYI6dgk"
bot = Bot(token)
dp = Dispatcher(bot= bot)



mass_accessories = ["0000", "1234"]
mass_underwear = []
mass_trousers = []
mass_sweater = []
mass_outerwear = []

mass_accessories_key = ["Товар 1", "Товар 2"]
mass_underwear_key = []
mass_trousers_key = []
mass_sweater_key = []
mass_outerwear_key = []

flag_accessories = False
flag_underwear = False
flag_trousers = False
flag_sweater = False
flag_outerwear = False

flag_accessories_1 = False
flag_underwear_1 = False
flag_trousers_1 = False
flag_sweater_1 = False
flag_outerwear_1 = False



@dp.message_handler(commands= ["start"] )
async def cmd_start(msg: types.Message) -> None:
    global flag_trousers, flag_accessories, flag_sweater, flag_outerwear, flag_underwear
    global flag_accessories_1, flag_underwear_1, flag_trousers_1, flag_sweater_1, flag_outerwear_1
    await msg.answer(msg.chat.id)

    flag_accessories_1 = False
    flag_underwear_1 = False
    flag_trousers_1 = False
    flag_sweater_1 = False
    flag_outerwear_1 = False
    flag_accessories = False
    flag_underwear = False
    flag_trousers = False
    flag_sweater = False
    flag_outerwear = False
    await msg.answer("Вас приветствует Ledy Bot! \n Выберите одну из предложенных категорий: "
                     "\n /adminhelp - помощь от менеджера \n /outerwear - верхняя одежда \n /underwear - нижнее белье, "
                     "\n /trousers - штаны, юбки и т.д. \n /sweater - кофты, свитеры, футболки и т.д. \n /accessories - акссесуары и прочее.")

@dp.message_handler(commands= ["adminhelp"])
async def adminhelp(msg: types.Message) -> None:
    await msg.answer("@BVDblue - Вопросы по работе бота \n ___ - по продажам \n /start - начать с начала")

@dp.message_handler(commands= ["underwear"])
async def underwear(msg: types.Message) -> None:
    global flag_underwear
    flag_underwear = True
    await msg.answer("Пожалуйста, введите артикул товара (Пример: 0000) \n /close - назад")

@dp.message_handler(commands= ["outerwear"])
async def underwear(msg: types.Message) -> None:
    global flag_outerwear
    flag_outerwear = True
    await msg.answer("Пожалуйста, введите артикул товара (Пример: 0000) \n /close - назад")

@dp.message_handler(commands= ["sweater"])
async def underwear(msg: types.Message) -> None:
    global flag_sweater
    flag_sweater = True
    await msg.answer("Пожалуйста, введите артикул товара (Пример: 0000) \n /close - назад")

@dp.message_handler(commands= ["trousers"])
async def underwear(msg: types.Message) -> None:
    global flag_trousers
    flag_trousers = True
    await msg.answer("Пожалуйста, введите артикул товара (Пример: 0000) \n /close - назад")

@dp.message_handler(commands= ["accessories"])
async def underwear(msg: types.Message) -> None:
    global flag_accessories
    flag_accessories = True
    await msg.answer("Пожалуйста, введите артикул товара (Пример: 0000) \n /close - назад")

@dp.message_handler(commands= ["yes"])
async def underwear(msg: types.Message) -> None:
    global truefalse, answer
    truefalse = False
    await msg.answer("Заявка создана, ожидайте отклика от менеджера ___ \n /start - сделать еще одну заявку")
    await bot.send_message(728859491, f"@{msg.from_user.username}, заявка - {answer}")
    del answer

@dp.message_handler(commands= ["no"])
async def underwear(msg: types.Message) -> None:
    global truefalse, answer
    truefalse = False
    del answer
    global flag_trousers, flag_accessories, flag_sweater, flag_outerwear, flag_underwear
    global flag_accessories_1, flag_underwear_1, flag_trousers_1, flag_sweater_1, flag_outerwear_1
    flag_accessories_1 = False
    flag_underwear_1 = False
    flag_trousers_1 = False
    flag_sweater_1 = False
    flag_outerwear_1 = False
    flag_accessories = False
    flag_underwear = False
    flag_trousers = False
    flag_sweater = False
    flag_outerwear = False
    await msg.answer("Вас приветствует Ledy Bot! \n Выберите одну из предложенных категорий: "
                     "\n /adminhelp - помощь от менеджера \n /outerwear - верхняя одежда \n /underwear - нижнее белье, "
                     "\n /trousers - штаны, юбки и т.д. \n /sweater - кофты, свитеры, футболки и т.д. \n /accessories - акссесуары и прочее.")


@dp.message_handler(commands= ["close"])
async def underwear(msg: types.Message) -> None:
    global flag_trousers, flag_accessories, flag_sweater, flag_outerwear, flag_underwear
    global flag_accessories_1, flag_underwear_1, flag_trousers_1, flag_sweater_1, flag_outerwear_1
    flag_accessories_1 = False
    flag_underwear_1 = False
    flag_trousers_1 = False
    flag_sweater_1 = False
    flag_outerwear_1 = False
    flag_accessories = False
    flag_underwear = False
    flag_trousers = False
    flag_sweater = False
    flag_outerwear = False
    await msg.answer("Вас приветствует Ledy Bot! \n Выберите одну из предложенных категорий: "
                     "\n /adminhelp - помощь от менеджера \n /outerwear - верхняя одежда \n /underwear - нижнее белье, "
                     "\n /trousers - штаны, юбки и т.д. \n /sweater - кофты, свитеры, футболки и т.д. \n /accessories - акссесуары и прочее.")




@dp.message_handler()
async def none(msg: types.Message) -> None:
    global flag_trousers, flag_accessories, flag_sweater, flag_outerwear, flag_underwear
    global mass_sweater, mass_underwear, mass_accessories, mass_outerwear, mass_trousers
    global mass_trousers_key, mass_underwear_key, mass_accessories_key, mass_outerwear_key, mass_sweater_key
    global flag_accessories_1, flag_underwear_1, flag_trousers_1, flag_sweater_1, flag_outerwear_1
    global art , truefalse, answer

    if not(flag_accessories_1 or flag_underwear_1 or flag_trousers_1 or flag_sweater_1 or flag_outerwear_1):

        if msg.text in mass_underwear and flag_underwear == True:
            flag_underwear = False
            flag_underwear_1 = True
            art = msg.text
            await msg.answer("Пожалуйста, выберите размер")
        elif msg.text in mass_outerwear and flag_outerwear == True:
            flag_outerwear = False
            flag_outerwear_1 = True
            art = msg.text
            await msg.answer("Пожалуйста, выберите размер")
        elif msg.text in mass_trousers and flag_trousers == True:
            flag_trousers = False
            flag_trousers_1 = True
            art = msg.text
            await msg.answer("Пожалуйста, выберите размер")
        elif msg.text in mass_accessories and flag_accessories == True:
            flag_accessories = False
            flag_accessories_1 = True
            art = msg.text
            await msg.answer("Пожалуйста, выберите размер")
        elif msg.text in mass_sweater and flag_sweater == True:
            flag_sweater = False
            flag_sweater_1 = True
            art = msg.text
            await msg.answer("Пожалуйста, выберите размер")
        else:
            await msg.answer("Товар не найден \n /close - выбрать другую категорию \n /adminhelp - помощь менеджера")

    else:
        if flag_sweater_1 == True:
            flag_sweater_1 = False
            truefalse = True
            answer = mass_sweater_key[mass_sweater.index(art)] + ", " + art + ", " + msg.text
            await msg.answer(f"{mass_sweater_key[mass_sweater.index(art)]} {art} {msg.text} \n Подтвердите все верно? \n /yes - все верно \n /no - заявка составлена неверно, начнем сначала")
            del art

        elif flag_outerwear_1 == True:
            flag_outerwear_1 =False
            truefalse = True
            answer = mass_outerwear_key[mass_outerwear.index(art)] + ", " + art + ", " + msg.text
            await msg.answer(f"{mass_outerwear_key[mass_outerwear.index(art)]} {art} {msg.text} \n Подтвердите все верно? \n /yes - все верно \n /no - заявка составлена неверно, начнем сначала")
            del art

        elif flag_accessories_1 == True:
            flag_accessories_1 = False
            truefalse = True
            answer = mass_accessories_key[mass_accessories.index(art)] + ", " + art + ", " + msg.text
            await msg.answer(f"{mass_accessories_key[mass_accessories.index(art)]} {art} {msg.text} \n Подтвердите все верно? \n /yes - все верно \n /no - заявка составлена неверно, начнем сначала")
            del art

        elif flag_underwear_1 == True:
            flag_underwear_1 = False
            truefalse = True
            answer = mass_underwear_key[mass_underwear.index(art)] + ", " + art + ", " + msg.text
            await msg.answer(f"{mass_underwear_key[mass_underwear.index(art)]} {art} {msg.text} \n Подтвердите все верно? \n /yes - все верно \n /no - заявка составлена неверно, начнем сначала")
            del art

        elif flag_trousers_1 == True:
            flag_trousers_1 = False
            truefalse = True
            answer = mass_trousers_key[mass_trousers.index(art)] + ", " + art + ", " + msg.text
            await msg.answer(f"{mass_trousers_key[mass_sweater.index(art)]} {art} {msg.text} \n Подтвердите все верно? \n /yes - все верно \n /no - заявка составлена неверно, начнем сначала")
            del art



if __name__ == '__main__':
    executor.start_polling(dp)

