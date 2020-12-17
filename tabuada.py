n = int (input ('digite um número: '))

a1 = n + 1
a2 = n + 2
a3 = n + 3
a4 = n + 4
a5 = n + 5
a6 = n + 6
a7 = n + 7
a8 = n + 8
a9 = n + 9

m1 = n * 1
m2 = n * 2
m3 = n * 3
m4 = n * 4
m5 = n * 5
m6 = n * 6
m7 = n * 7
m8 = n * 8
m9 = n * 9

s1 = n - 1
s2 = n - 2
s3 = n - 3
s4 = n - 4
s5 = n - 5
s6 = n - 6
s7 = n - 7
s8 = n - 8
s9 = n - 9

d1 = n / 1
d2 = n / 2
d3 = n / 3
d4 = n / 4
d5 = n / 5
d6 = n / 6
d7 = n / 7
d8 = n / 8
d9 = n / 9

print (' ADÇÃO ')
print (' {} + 1 = {} \n {} + 2 = {} \n {} + 3 = {} \n {} + 4 = {} \n {} + 5 = {} '
       '\n {} + 6 = {} \n {} + 7 = {} \n {} + 8 = {} \n {} + 9 = {}'
       .format (n , a1 , n , a2 ,n , a3 ,n ,a4 , n , a5 , n ,a6 , n , a7 ,n , a8 , n , a9))


print (' SUBTRAÇÃO')
print (' {} - 1 = {} \n {} - 2 = {} \n {} - 3 = {} \n {} - 4 = {} \n {} - 5 = {} '
       '\n {} - 6 = {} \n {} - 7 = {} \n {} - 8 = {} \n {} - 9 = {}'
       .format (n , s1 , n , s2 ,n , s3 ,n ,s4 , n , s5 , n ,s6 , n , s7 ,n , s8 , n , s9))


print (' MULTIPLICAÇÃO')
print (' {} * 1 = {} \n {} * 2 = {} \n {} * 3 = {} \n {} * 4 = {} \n {} * 5 = {} '
       '\n {} * 6 = {} \n {} * 7 = {} \n {} * 8 = {} \n {} * 9 = {}'
       .format (n , m1 , n , m2 ,n , m3 ,n ,m4 , n , m5 , n ,m6 , n , m7 ,n , m8 , n , m9))

print (' DIVISÃO')
print (' {} / 1 = {:.1f} \n {} / 2 = {:.1f} \n {} / 3 = {:.1f} \n {} / 4 = {:.1f} \n {} / 5 = {:.1f} '
       '\n {} / 6 = {:.1f} \n {} / 7 = {:.1f} \n {} / 8 = {:.1f} \n {} / 9 = {:.1f}'
       .format (n , d1 , n , d2 ,n , d3 ,n ,d4 , n , d5 , n ,d6 , n , d7 ,n , d8 , n , d9))