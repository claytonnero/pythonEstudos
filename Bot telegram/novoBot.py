import telepot

bot = telepot.Bot("1463037753:AAF1g1u39rwiPnsMtPm70lLa-rCV6pxybEs")

def getMessage(msg):
    print(msg['text'])

bot.message_loop(getMessage)

while True:
    pass