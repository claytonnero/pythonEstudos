##aula 2
# feito na aula 1
print('Olá qual é o seu nome?')
nome = input('>: ')
nome = nome.lower()
nome = nome.replace('é', 'eh', 1)

#feito na aula 2
if "o meu nome eh " in nome:
	nome = nome[14:]
if "eu me chamo " in nome:
	nome = nome[11:]
	
nome = nome.title()	
conhecidos = ["Clayton", "Will", "Nero"]

if nome in conhecidos:
	frase = "E Aí "
else:
	frase = "Muito Prazer "
print(frase+"{}!".format(nome))
	
while True:
	resposta = input(">: ")
	
	if resposta == 'tchau':
		break
		
print("thau, thau!")