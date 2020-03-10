# -*- coding: utf-8 -*-
import telebot
import apiai, json
bot = telebot.TeleBot("965457992:AAGxFZYTn0SHf77Sis6mCoHZ1JzEZ2lIVqU")

@bot.message_handler(commands=['start'])
def greeting(message):
	bot.send_message(message.chat.id, "Hello, my friend, how can I help you?")
@bot.message_handler(content_types=['text'])
def lalala(message):
	request = apiai.ApiAI('ca3d18eb99584581b4fdce3d63f02ba4').text_request()# Токен API к Dialogflow
	request.lang = 'ru' # На каком языке будет послан запрос
	request.session_id = 'BatlabAIBot'	# ID Сессии диалога (нужно, чтобы потом учить бота)
	request.query = message.text # Посылаем запрос к ИИ с сообщением от юзера
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
	if response:
		bot.send_message(message.chat.id, text=response)
	else:
		bot.send_message(message.chat.id, text='Я Вас не совсем понял!')
bot.polling(none_stop=True)
