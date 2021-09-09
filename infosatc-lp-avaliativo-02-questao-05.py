lista = ['BANANA', 'MAÇA', 'LARANJA', 'MORANGO'] 
print(lista)

per = input("digite para conferir se esta na lista: ")

if per in lista:
    print("Sim, está na lista!")
else:
    print("Não está na lista")