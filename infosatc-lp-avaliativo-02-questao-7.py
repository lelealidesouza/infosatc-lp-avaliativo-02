listaFilme = ['Vingadores', 'Transformes'] 
print(listaFilme)

listaJogos = ['Zelda', 'Mario'] 
print(listaJogos)

listaLivros = ['Anne Frank', 'Diario De Um Banana'] 
print(listaLivros)

listaEsportes = ['Volei', 'Basquete'] 
print(listaEsportes)

#Letra A da questao 7

listaFilme.append("Gente Grande") 
print(listaFilme)
listaFilme.append("Noiva Cadaver") 
print(listaFilme)

listaJogos.append("LOL") 
print(listaJogos)
listaJogos.append("Valorant") 
print(listaJogos)

listaLivros.append("Dom Quixote") 
print(listaLivros)
listaLivros.append("Cem Anos De Solidao") 
print(listaLivros)

listaEsportes.append("Fórmula 1.") 
print(listaEsportes)
listaEsportes.append("Boxe") 
print(listaEsportes)

#Letra B da questao 7

listaGeral = listaFilme + listaJogos + listaLivros + listaEsportes 
print(listaGeral)

#Letra C da questao 7

MostrarLivros = input("Digite algo da lista de Livros para verificar sua posição: ")
print(listaLivros)
print("A posição de {} é {}".format(MostrarLivros, listaLivros.index(MostrarLivros)))

#Letra D da questao 7 

del listaEsportes[0]
del listaGeral[0]
print(listaEsportes)
print(listaGeral)

#Letra E da questao 7

