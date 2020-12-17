import math
num = float(input('Digite um numero real: '))

print ('O numero inteiro {} é {} '.format(num, math.trunc(num)))

import math
cat1 = int(input('Digite o comprimento do primeiro cateto: '))
cat2 = int(input('Digite o comprimento do segundo cateto: '))
res = math.hypot(cat1, cat2)
print('A Hipotenusa desse triângulo-retângulo será {:.2f}'.format(res))

an = float(input('Digite um ângulo: '))
s = math.sin (math.radians (an))
c = math.cos (math.radians (an))
t = math.tan (math.radians (an))
print('Sendo assim, o seno é {}, o cosseno é {} e a tangente é {}' .format (s, c, t ))


