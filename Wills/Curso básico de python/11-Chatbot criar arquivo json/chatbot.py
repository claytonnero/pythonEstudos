import json
class Chatbot():
	def __init__(self, nome):
		memória = open(nome+".json", "r")
		self.nome = nome
		self.conhecidos = json.load(memória)
		memória.close()
		self.histórico = []
		
	def escuta(self):
		#captura a resposta do usuário e pré-processa a resposta
		frase = input('>: ')
		frase = frase.lower()
		frase = frase.replace('é', 'eh', 1)
		return frase
            
	def pensa(self, frase):
		if frase == "oi":
			self.histórico.append(frase)
			return "Olá qual é o seu nome?"
		if frase == "tchau":
			return "tchau"
		if self.histórico[-1] == "Olá qual é o seu nome?":
			nome = self.pegaNome(frase)
			resp = self.respondeNome(nome)
			return resp
		return "Não Entendí"
     
	def pegaNome(self, nome):
		if "o meu nome eh" in nome:
			nome = nome[14:]
		if "eu me chamo " in nome:
			nome = nome[11:]
		nome = nome.title()	
		return nome

	def respondeNome(self, nome):	
		if nome in self.conhecidos:
			frase = "E Aí "
		else:
			frase = "Muito Prazer "
			self.conhecidos.append(nome)
			memória = open(self.nome+".json", "w")
			json.dump(self.conhecidos, memória)
			memória.close()
			
		return frase+"{}!".format(nome)
            
	def fala(self, frase):
		print(frase)
		self.histórico.append(frase)