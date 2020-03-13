# -*- coding: utf-8 -*-
import telebot
import apiai, json
bot = telebot.TeleBot("965457992:AAGxFZYTn0SHf77Sis6mCoHZ1JzEZ2lIVqU")

@bot.message_handler(commands=['start'])
def greeting(message):
	bot.send_message(message.chat.id, "Здравствуйте, чем я могу Вам помочь?")
@bot.message_handler(content_types=['text'])
def lalala(message):
	request = apiai.ApiAI('ca3d18eb99584581b4fdce3d63f02ba4').text_request()
	request.lang = 'ru'
	request.session_id = 'BatlabAIBot'
	request.query = message.text
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech']
	if response:
		bot.send_message(message.chat.id, text=response)
	else:
		bot.send_message(message.chat.id, text='Я Вас не совсем понял!')
bot.polling(none_stop=True)
