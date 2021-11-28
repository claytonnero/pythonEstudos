class Chatbot():
	def __init__(self, nome):
		self.nome = nome
		
	def fala(self, nome):
		print("Oi meu nome é "+self.nome)

b1 = Chatbot("Clayton")
b1.fala()

b2 = Chatbot("Tatiane")
b2.fala()
