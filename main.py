import os
import telebot


bot = telebot.TeleBot("1958240247:AAGbmYdNKyjNhvknZWQ_VRmnR8fvWH3a1Jo")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Panda Baby Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCKOLacpK4mv1uh3DhCM8XRg")



bot.polling()
