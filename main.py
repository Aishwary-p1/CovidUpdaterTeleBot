import telebot
from data import *


bot = telebot.TeleBot(YOUR_BOT_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to Covid Tracker Bot, the data you are receiving is from www.mohfw.gov.in. \n\n\nThe list of commands are \n\n/ACTIVE for total active cases \n\n\n/RECOVERED for total recovered cases \n\n\n/DEATHS for total deaths.")


@bot.message_handler(commands=['ACTIVE'])
def send_active(message):
	active = get_active()
	bot.reply_to(message, "Total active cases are {} and the new cases are {}.".format(active[0], active[1]))

	
@bot.message_handler(commands=['RECOVERED'])
def send_recovered(message):
	recovered = get_recovered()
	bot.reply_to(message, "Total recovered cases are {} and the newly recovered are {}.".format(recovered[0], recovered[1]))


@bot.message_handler(commands=['DEATHS'])
def send_deaths(message):
	deaths = get_deaths()
	bot.reply_to(message, "Total deaths are {} and new deaths are {}.".format(deaths[0], deaths[1]))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, "Wrong Command")

bot.polling()
