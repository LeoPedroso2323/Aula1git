import time

#Criando uma lista dentro de outra lista usando o For
lista = [[x for x in range(4)] for i in range(5)]

print(lista)

lista2 = [12, 17, 22, 45, 32]

print(lista2)

lista2.sort()

print(lista2)

print(lista2[3])

lista.reverse()

print(lista2)

lista_1 = [1,2]
lista_2 = lista_1
lista_1 [0] = 2
lista_1 [1] = 3
print(lista_2)
print(len(lista_2))

time.sleep(3)