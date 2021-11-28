from chatbot import Chatbot

bot = Chatbot("Clayton Nero")

while True:
	frase = bot.escuta()
	resp = bot.pensa(frase)
	bot.fala(resp)
	
	if resp == 'tchau amigo! volte depois pra prosearmos novamente! ':
		break
	
