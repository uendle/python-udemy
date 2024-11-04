import telebot
import csv
from datetime import datetime
import os

# Substitua 'YOUR_BOT_TOKEN' pelo token do seu bot
TOKEN = '5601684431:AAExTIs3ACgNrDCH-j-AgwAuxyMGc7zs198'
bot = telebot.TeleBot(TOKEN)

# Diretório onde os dados serão armazenados
data_dir = '/home/uendle'
os.makedirs(data_dir, exist_ok=True)

# Caminho do arquivo CSV onde todos os dados serão armazenados
csv_file_path = os.path.join(data_dir, 'dados_coletados.csv')

# Cria o arquivo CSV e escreve o cabeçalho se não existir
if not os.path.exists(csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['CNPJ', 'Quantidade', 'Usuário', 'Data e Hora'])

# Dicionário para rastrear o estado de cada usuário
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_states[user_id] = 'waiting_for_cnpj'
    bot.send_message(message.chat.id, "Olá! Por favor, forneça o CNPJ.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id

    if user_id not in user_states:
        bot.send_message(message.chat.id, "Por favor, inicie a coleta de dados clicando no /start.")
        return

    state = user_states[user_id]

    if state == 'waiting_for_cnpj':
        user_states[user_id] = 'waiting_for_quantity'
        user_states[f'{user_id}_cnpj'] = message.text  # Armazena o CNPJ
        bot.send_message(message.chat.id, "Obrigado! Agora, por favor, forneça a quantidade de caixas.")
    
    elif state == 'waiting_for_quantity':
        quantity = message.text
        
        # Armazena os dados no arquivo CSV
        cnpj = user_states[f'{user_id}_cnpj']
        username = message.from_user.username or message.from_user.first_name
        
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([cnpj, quantity, username, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        
        bot.send_message(message.chat.id, "Dados coletados com sucesso! Obrigado!")
        
        # Reinicia a coleta para o próximo usuário
        del user_states[user_id]
    
    else:
        # Reinicia a coleta se receber qualquer outra mensagem
        bot.send_message(message.chat.id, "Coleta reiniciada. Por favor, forneça seu CNPJ.")
        user_states[user_id] = 'waiting_for_cnpj'

if __name__ == '__main__':
    bot.polling()