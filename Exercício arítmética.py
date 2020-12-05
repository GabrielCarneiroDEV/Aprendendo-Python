n1 = int (input ('Diga um número: '))
s = int (n1 + 1)
a = int (n1 - 1)


print ('O sucessor de n1 é: ' , s )
print (' O antecessor de n1 é: ' , a )


n2 = int(input ('Diga um número: '))
d = n2 * 2
t = n2 * 3
rq = n2 ** 1/2

print ('o dobro de n2 é {} o triplo é {}  e a raiz quadrada é {}' .format (d, t, rq))


n = input ('Nome do aluno: ')
n1 = int (input ('primeira nota: '))
n2 = int (input ('segunda nota: '))
print ('{} teve como média no seu boletim escolar {}'.format (n , (n1+n2)/2))

medida = float(input('uma medida em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100  
mm = medida * 1000

print ('a medida tem {:.1f} metros \n {:.3f} Km \n {:.2f}Hm \n {:.0f} Dam \n {:.0f} dm \n {:.0f}cm \n {:.0f}mm' .format (medida, km, hm, dam, dm, cm, mm))

