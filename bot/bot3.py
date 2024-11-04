import telebot
from telebot import types

# Substitua pelo seu token
API_TOKEN = '5601684431:AAExTIs3ACgNrDCH-j-AgwAuxyMGc7zs198'

# Inicializa o bot
bot = telebot.TeleBot(API_TOKEN)

# 1. Comando /start - Envia uma mensagem de boas-vindas
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Olá, bem-vindo ao bot! Use /help para ver os comandos disponíveis.")

# 2. Comando /help - Lista os comandos disponíveis
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(
        message.chat.id, 
        "Aqui estão os comandos disponíveis:\n"
        "/start - Inicia o bot\n"
        "/help - Exibe esta mensagem de ajuda\n"
        "/foto - Envia uma foto\n"
        "/audio - Envia um áudio\n"
        "/doc - Envia um documento\n"
        "/options - Mostra opções com teclado customizado"
    )

# 3. Enviar uma foto ao usar o comando /foto
@bot.message_handler(commands=['foto'])
def send_photo(message):
    bot.send_photo(message.chat.id, 'https://cdn.pixabay.com/photo/2023/10/30/01/31/duck-8351436_1280.jpg')

# 4. Enviar um áudio ao usar o comando /audio
@bot.message_handler(commands=['audio'])
def send_audio(message):
    audio = open('meu_arquivo.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)

# 5. Enviar um documento ao usar o comando /doc
@bot.message_handler(commands=['doc'])
def send_document(message):
    doc = open('meu_documento.pdf', 'rb')
    bot.send_document(message.chat.id, doc)

# 6. Criar um teclado customizado e enviar ao usar o comando /options
@bot.message_handler(commands=['options'])
def send_options(message):
    # Cria o teclado inline
    keyboard = types.InlineKeyboardMarkup()
    botao1 = types.InlineKeyboardButton("Opção 1", callback_data='op1')
    botao2 = types.InlineKeyboardButton("Opção 2", callback_data='op2')
    botao3 = types.InlineKeyboardButton("Opção 3", callback_data='op3')
    botao4 = types.InlineKeyboardButton("Opção 4", callback_data='op4')
    botao5 = types.InlineKeyboardButton("Opção 5", callback_data='op5')
    botao6 = types.InlineKeyboardButton("Opção 6", callback_data='op6')
    # Adiciona os botões ao teclado
    keyboard.add(botao1, botao2, botao3, botao4, botao5, botao6)
    bot.send_message(message.chat.id, "Escolha uma opção:", reply_markup=keyboard)

# 7. Lidar com as respostas dos botões do teclado customizado
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'op1':
        bot.send_message(call.message.chat.id, "Você escolheu a Opção 1!")
    elif call.data == 'op2':
        bot.send_message(call.message.chat.id, "Você escolheu a Opção 2!")
    elif call.data == 'op3':
        bot.send_message(call.message.chat.id, "Você escolheu a Opção 3!")
    elif call.data == 'op4':
        bot.send_message(call.message.chat.id, "Você escolheu a Opção 4!")
    elif call.data == 'op5':
        bot.send_message(call.message.chat.id, "Você escolheu a Opção 5!")
    elif call.data == 'op6':
        bot.send_message(call.message.chat.id, "Você escolheu a Opção 6!")
    else:
        bot.send_message(call.message.chat.id, "Algo deu errado!")

# 8. Repetir qualquer mensagem enviada para o bot (eco)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

# 9. Lidar com fotos enviadas para o bot
@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    bot.reply_to(message, "Bela foto!")

# 10. Lidar com documentos enviados para o bot
@bot.message_handler(content_types=['document'])
def document_handler(message):
    bot.reply_to(message, "Recebi o seu documento!")

# 11. Coloca o bot em modo polling para ficar ativo
bot.polling()
