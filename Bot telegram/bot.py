import telepot

bot = telepot.Bot("1463037753:AAF1g1u39rwiPnsMtPm70lLa-rCV6pxybEs")

#this will only work if you first go on the telegram and start a conversation and next
print(bot.getUpdates())

"""
[{'update_id': 428150916, 'message': {'message_id': 3, 'from': {'id': 1307273058, 'is_bot': False, 'first_name': 'Clayton Nero', 'username': 'claytonnero', 'language_code': 'pt-br'}, 'chat': {'id': 1307273058, 'first_name': 'Clayton Nero', 'username': 'claytonnero', 'type': 'private'}, 'date': 1609328288, 'text': 'Oi'}}, {'update_id': 428150917, 'message': {'message_id': 4, 'from': {'id': 1307273058, 'is_bot': False, 'first_name': 'Clayton Nero', 'username': 'claytonnero', 'language_code': 'pt-br'}, 'chat': {'id': 1307273058, 'first_name': 'Clayton Nero', 'username': 'claytonnero', 'type': 'private'}, 'date': 1609328295, 'text': 'Bot meu'}}]
"""
bot.sendMessage(1307273058, "")