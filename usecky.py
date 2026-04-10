# y=ax+b
# x=y-b/a
# pocitaj a, b pomocou sustav dvoch rovnic
#a2 - b2/a1 - b1 = a
#a2 - a1*(a2-b2/a1-b1) = b
#
# nacitaj suradnice a vytvorenie bieleho pozadia
#
from PIL import Image
import sys
canvas = 1000
pic = Image.new("RGB",(canvas, canvas),"white")
pixels = pic.load()

def vstup(suradnica,poradie,limit):
    temp_input = int(input('Zadaj '+suradnica+' suradnicu '+poradie+' bodu: '))
    if temp_input > limit:
        print('Hodnota moze byt medz 0..',limit)
        sys.exit()
    else:
        return temp_input

a1 = vstup('x','prveho',canvas)
a2 = vstup('y','prveho',canvas)
b1 = vstup('x','druheho',canvas)
b2 = vstup('y','druheho',canvas)
#
#rozdelenie ci je x rovnake alebo nie
#
if a1 > b1:
     a1,b1 = b1,a1
     a2,b2 = b2,a2
if a1 != b1:
#
# vypocet a, b
#
    a = (a2 - b2)/(a1 - b1)
    b = a2 - a1*((a2-b2)/(a1-b1))
    #print(a,b)
#
#rozhodnutie ci idem cez x alebo cez y
#
    if abs(a1 - b1) > abs(a2 - b2) or abs(a1 - b1) == abs(a2 - b2):
#
#vypocitanie x, y + vykreslenie
#
        #print(a1,b1,a,b)
        for x in range(a1, b1 + 1):
            y = round((a*x)+b)
            #print(y)
            pixels[x,y] = (0, 0, 0)        
    else:
        for y in range(a2, b2 + 1):
            x = round((y-b)/a)
            pixels[x,y] = (0, 0, 0)
else:
    a = 1
    x = a1
    if b2 < a2:
         a2,b2 = b2,a2
    for y in range(a2, b2+1):
            pixels[x,y] = (0, 0, 0)        
    
#
#vykreslenie grafu
#
pic.show()
