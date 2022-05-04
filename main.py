import telebot
bot = telebot.TeleBot(Token)
#Mensagem inicial para começar o bot.
@bot.message_handler(commands=['start','help'])
def send_start_message(message):
    lang=message.from_user.language_code
    if lang=="pt-br":
        bot.reply_to(message, "Olá, eu sou o PokeBot, eu te envio uma rom de pokemon que você escolher :3\n"
                                "Temos todos os jogos de pokemons desde GBA até 3DS\n"
                              "Digite o nome do jogo que você deseja:")
    elif lang=="es":
        bot.reply_to(message, "¡Hola, soy PokeBot, te envío una rom de Pokémon de tu elección :3 ")
    else:
        bot.reply_to(message, "Hello, I'm PokeBot, i send you a pokemon rom of your choice :3 ")
#Será verificado qual rom o usuário solicitará e enviará o FileID imdeiatamente.
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(f'Usuário:{message.chat.id} [{message.from_user.first_name}|{message.from_user.last_name}|{message.from_user.username}] {message.from_user.language_code} requisitou: {message.text}. {message.id}')
    necessitarom=True
    if message.text.count("latinum")>0:
        bot.send_photo(message.chat.id,'https://static.wikia.nocookie.net/pokepediabr/images/8/83/Platinum_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160129222124&path-prefix=pt-br')
        rom = "BQACAgEAAxkDAAP-X9fe36xpBClD2pXWgG1Uuuhd_JYAAhEBAALD5LlGqC1LZTSTjroeBA"
        print('Enviei Platinum.')
    elif message.text.count("earl"):
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/a/af/Pearl_EN_boxart.jpg/revision/latest/scale-to-width-down/1000?cb=20160129211425&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBGl_X4czOJUQ7fCgFL7jlD0fvZOalAAITAQACw-S5RlerRMFKI2Q8HgQ"
        print("Enviei Pearl")
    elif message.text.count("iamond")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/6/69/Diamond_EN_boxart.jpg/revision/latest/scale-to-width-down/1000?cb=20160129211709&path-prefix=pt-br")
        rom="BQACAgEAAxkDAAIBD1_X4T0ciJ7p2V-46aU1l4mDStdGAAIXAQACw-S5RlSscDUaYoJzHgQ"
        print('Enviei Diamond.')
    elif message.text.count("old")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/6/6e/HeartGold_EN_boxart.jpg/revision/latest/scale-to-width-down/1000?cb=20160130201205&path-prefix=pt-br")
        rom="BQACAgEAAxkDAAIBJV_X4mlwuzh2zmycZs92eOhGNk2gAAIYAQACw-S5Rnq5-3OeyGXhHgQ"
        print('Enviei HearthGold.')
    elif message.text.count("ilver") > 0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/5/5c/SoulSilver_EN_boxart.jpg/revision/latest/scale-to-width-down/1000?cb=20160130201145&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBKF_X44mQbbrE_lP_w9xzSoc4sSnPAAIZAQACw-S5Rq8CqF0Stzt5HgQ"
        print('Enviei SoulSilver.')
    elif message.text.count("2") > 0 and message.text.count("lack")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/3/34/Black_2_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160131174604&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBL1_X5XhzFwbDoNjLEg33rAOI3mbDAAIdAQACw-S5RvHaCcuTJUWEHgQ"
        print("Enviei Black 2")
    elif message.text.count("lack")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/d/dc/Black_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160131172244&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAPbX9fXIxTh-xzxe8FPfgXqjAsJSF8AAv4AA8PkuUb8U3DnYDgBLR4E"
        print('Enviei Black.')
    elif message.text.count("2") > 0 and message.text.count("hite")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/1/14/White_2_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160131174311&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBNV_X57TFpDPgNf69ren7_U9Uy5VMAAIfAQACw-S5Rs4OBp7QInNxHgQ"
        print('Enviei White 2.')
    elif message.text.count("hite") > 0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/0/08/White_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160131172139&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBMl_X5odjKe3o_7bONLaTvoUsQCZQAAIeAQACw-S5Rs8eKmNeNYffHgQ"
        print('Enviei White.')
    elif message.text.count("mega")>0 and message.text.count("ub")>0:
        necessitarom=False
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/5/5b/Omega_Ruby_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160131183943&path-prefix=pt-br")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBxF_X9YPr4g2NiEDU9pxSE6nXCYUgAAJZAgACuaRoAAHU1YVHbefseR4E")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIByF_X9Y4-kfCmKY56A_a38Isj8uGyAAJaAgACuaRoAAH9Be4vc3rcEx4E")
        print('Enviei OmegaRuby')
    elif message.text.count("lpha")>0 and message.text.count("ire")>0:
        necessitarom=False
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/f/f2/Alpha_Sapphire_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160131183754&path-prefix=pt-br")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBzF_X9c19z2MeVogaO-O1t_CJYTyNAAJBAgACuaRoAAGIzy-iHZ8hVx4E")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIB0F_X9dfDQ-QPujW7f7WoJiWOerWeAAJCAgACuaRoAAE5x1ElHUpBIR4E")
        print('Enviei AlphaSapphire')
    elif message.text.count("ire")>0 and message.text.count("ap")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/0/05/Sapphire_boxart.jpg/revision/latest/scale-to-width-down/500?cb=20160129181327&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBSF_X683OjOCkBHiUnp3tA7j22OHvAAIjAQACw-S5RtMxsthIhu0KHgQ"
        print('Enviei Sapphire')
    elif message.text.count("ire")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/d/d4/FireRed_boxart.jpg/revision/latest/scale-to-width-down/400?cb=20160129185552&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBPF_X6rvwBVDWQlkUk3vWxfZf4ercAAIgAQACw-S5RhUcm7z3i-YuHgQ"
        print('Enviei FireRed.')
    elif message.text.count("eaf")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/f/fd/LeafGreen_boxart.jpg/revision/latest/scale-to-width-down/400?cb=20160129185537&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBQF_X6u4qyPU8f6BJYkwFpD5Ivlx3AAIhAQACw-S5RrgFrp6GeNG5HgQ"
        print('Enviei LeafGreen.')
    elif message.text.count("merald")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/6/65/Emerald_EN_boxart.jpg/revision/latest/scale-to-width-down/1000?cb=20160129203404&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBRF_X62v_VZNrKvwShZx8jwITSdOAAAIiAQACw-S5RiSd6s35TdFxHgQ"
        print('Enviei Emerald')
    elif message.text.count("ub")>0:
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/c/c4/Ruby_boxart.jpg/revision/latest/scale-to-width-down/500?cb=20160129181339&path-prefix=pt-br")
        rom = "BQACAgEAAxkDAAIBTF_X6_56xmYGwWK7FXX0xp0uGiV8AAIkAQACw-S5RrAbxt20vO2iHgQ"
        print('Enviei Ruby')
    elif message.text.count("x")>0 or message.text.count("X")>0:
        necessitarom=False
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/2/27/X_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160131183416&path-prefix=pt-br")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBbF_X7cF0M43D0jjwBWoaZL029yiAAAL1AAO5pGgAARUohbswuUb8HgQ")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBcF_X7f-fqlX2NCXr0_4PoOuxdrQYAAL2AAO5pGgAARKw9xU3F1ziHgQ")
        print('Enviei X')
    elif message.text.count("y")>0 or message.text.count("Y")>0:
        necessitarom=False
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/4/41/Y_EN_boxart.png/revision/latest/scale-to-width-down/1000?cb=20160131183346&path-prefix=pt-br")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBdF_X757RVXO-sfJ801DheYoTZLj0AAIgBAACrIYxUOUBvVZtr7klHgQ")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBeF_X76jSEkHDSqM3iXp6q2ZEjXOpAAIhBAACrIYxUAvQL25-xcLtHgQ")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBfF_X77QKHirZ5OKV8HtyEfkE9OuRAAIiBAACrIYxUMoECOitTdCyHgQ")
        print('Enviei Y')
    elif message.text.count("ltra")>0 and message.text.count("un")>0:
        necessitarom=False
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/3/36/DHhA38wXgAE3eeW.jpg/revision/latest/scale-to-width-down/320?cb=20170820044017&path-prefix=pt-br")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBnl_X81bkZhtmb7cfjaG_CZR7JGYJAAKkAgACCutRULuDcIEOk1MWHgQ")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBol_X819puxGFVk8LR3iSybcuY-ByAAKmAgACCutRUA0iaNbNZYanHgQ")
        print('Enviei UltraSun')
    elif message.text.count("ltra")>0 and message.text.count("oon")>0:
        necessitarom=False
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/7/79/DHhBDHDXcAApHsU.jpg/revision/latest/scale-to-width-down/320?cb=20170820044128&path-prefix=pt-br")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBvF_X9GxYVD_qPphbwjcZdnswAopIAALzAQAC6vsYUBgvtWpupGuvHgQ")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBwF_X9JH_ro1Q0p6UXOq52aAW5azHAAL7AQAC6vsYUEkcpXKdFgcZHgQ")
        print('Enviei UltraMoon')
    elif message.text.count("oon")>0:
        necessitarom=False
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/5/51/MoonBoxart.png/revision/latest/scale-to-width-down/1000?cb=20161030054315&path-prefix=pt-br")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBgF_X8L0PyTCVHksfp4yXw6SbgHc5AAJyAQACuaRoAAEwQR7jfhGDXB4E")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBhF_X8TcmYpQKYt-80hqsnqyxd3TtAAJzAQACuaRoAAHBNuNZOAABUJoeBA")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBiF_X8Uc6mFKik-YWdrLgjTS5uo1AAAJ0AQACuaRoAAFEmnMVHlROUh4E")
        print('Enviei Moon')
    elif message.text.count("un")>0:
        necessitarom=False
        bot.send_photo(message.chat.id, "https://static.wikia.nocookie.net/pokepediabr/images/5/51/MoonBoxart.png/revision/latest/scale-to-width-down/1000?cb=20161030054315&path-prefix=pt-br")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBgF_X8L0PyTCVHksfp4yXw6SbgHc5AAJyAQACuaRoAAEwQR7jfhGDXB4E")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBhF_X8TcmYpQKYt-80hqsnqyxd3TtAAJzAQACuaRoAAHBNuNZOAABUJoeBA")
        bot.send_document(message.chat.id, "BQACAgQAAxkDAAIBiF_X8Uc6mFKik-YWdrLgjTS5uo1AAAJ0AQACuaRoAAFEmnMVHlROUh4E")
        bot.send_message(message.chat.id, "Ficamos te devendo! Desculpe...")
        print('Enviei Moon')
    else:
        necessitarom=False
        print("Enviei nada.")
        bot.send_message(chat_id=message.chat.id, text="Desculpa, não entendi :/")
    if necessitarom:
        bot.send_document(message.chat.id, rom)

bot.polling()
