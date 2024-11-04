#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types
TOKEN = '5601684431:AAExTIs3ACgNrDCH-j-AgwAuxyMGc7zs198'

bot= telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def mensagem(mensagem):
    bot.reply_to(mensagem, "ola Bom dia!")

@bot.message_handler(commands=['foto'])
def mensagem(mensagem):
    bot.send_photo(mensagem.chat.id, "https://cdn.pixabay.com/photo/2023/10/30/01/31/duck-8351436_1280.jpg")


@bot.message_handler(commands=['options'])
def metodo_mensagem(msg):

    keyboard = types.InlineKeyboardMarkup()

    botao1 = types.InlineKeyboardButton("Opção 1", callback_data='op1')
    botao2 = types.InlineKeyboardButton("Opção 2", callback_data='op2')

    keyboard.add(botao1, botao2)
    bot.send_message(msg.chat.id, "Escolha uma opção:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'op1':
        bot.send_message(call.message.chat.id, "Você escolheu a Opção 1!")
    elif call.data == 'op2':
        bot.send_message(call.message.chat.id, "Você escolheu a Opção 2!")






@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    bot.reply_to(message, "Bela foto!")

# @bot.message_handler(func=lambda m: True)#papagaio
# def repetir(mensagem):
#     bot.reply_to(mensagem, mensagem.text)
    

lista= ['1','2','3']
@bot.message_handler(lista)
def metodo_mensagem(mensagem):
    bot.send_message(mensagem.chat, "ola")



bot.infinity_polling()