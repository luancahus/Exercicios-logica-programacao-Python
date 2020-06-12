#Triânulo#

import math
import os
ta = float(input('digite um valor '))
tb = float(input('digite um segundo valor '))
tc = float(input('digite um terceiro valor '))

if ta > (tb-tc) and tb > (ta-tc) and tc > (tb-ta):
if ta < (tb+tc) and tb < (ta+tc) and tc < (ta+tb):
if ta == tb == tc:
print('triângulo equilátero')
 elif ta == tb or tb == tc or ta == tc:
print('triângulo isósceles ')
 else:
print('triângulo escaleno')
 else:
print('não é um triângulo')
