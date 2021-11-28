def resposta():
	#captura a resposta do usuário e pré-processa a resposta
	resp = input('>: ')
	resp = resp.lower()
	resp = resp.replace('é', 'eh', 1)
	return resp
	
def pegaNome(nome):
	#funçao que pega o nome do usuário
	if "o meu nome eh " in nome:
		nome = nome[14:]
	if "eu me chamo " in nome:
		nome = nome[11:]
	nome = nome.title()	
	return nome

def respondeNome(nome):	
	conhecidos = ["Clayton", "Will", "Nero"]
	if nome in conhecidos:
		frase = "E Aí "
	else:
		frase = "Muito Prazer "
	return frase+"{}!".format(nome)