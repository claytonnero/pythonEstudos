##aula 2
# feito na aula 1
print('Olá qual é o seu nome?')
nome = input('>: ')

#feito na aula 2
if "o meu nome eh " in nome:
	nome = nome[14:]
	
conhecidos = ["Clayton", "Will", "Nero"]
frase = "Muito prazer "

for conhecido in conhecidos:
	if nome == conhecidos:
		frase = "E Aí "

print(frase+"{}!".format(nome))
	
while True:
	resposta = input(">: ")
	
	if resposta == 'tchau':
		break
		
print("thau, thau!")