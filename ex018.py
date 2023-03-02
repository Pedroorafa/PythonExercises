from math import cos, sin, tan,radians
a = int(input('Digite o valor do angulo: '))
r = radians(a)
s = sin(r)
c = cos(r)
t = tan(r)
print('O valor do seno é {:.2f}, do cosseno {:.2f} e da tangente {:.2f}'.format(s, c, t))

