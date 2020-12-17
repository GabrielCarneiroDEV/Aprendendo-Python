import random

a1 = input ('Nome do primeiro aluno: ')
a2 = input ('nome do segundo aluno: ')
a3 = input (' nome do terceiro aluno: ')
a4 = input (' nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
print ('Alunos: \n {} \n {} \n {} \n {} \n' .format(a1,a2,a3,a4))
escolhido = random.choice (lista)
print (' O aluno sorteado foi {}' .format(escolhido))

random.shuffle (lista)


print ('a ordem de apresentação dos alunos será :')
print (lista)


