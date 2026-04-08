# y=ax+b
# x=y-b/a
# pocitaj a, b pomocou sustav dvoch rovnic
#a2 - b2/a1 - b1 = a
#a2 - a1*(a2-b2/a1-b1) = b
#
# nacitaj suradnice a vytvorenie bieleho pozadia
#
from PIL import Image
pic = Image.new("RGB",(20,20),"white")
pixels = pic.load()
a1 = int(input('zadaj x suradnicu prveho bodu: '))
a2 = int(input('zadaj y suradnicu prveho bodu: '))
b1 = int(input('zadaj x suradnicu druheho bodu: '))
b2 = int(input('zadaj y suradnicu druheho bodu: '))
#
#rozdelenie ci je x rovnake alebo nie
#
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
        for x in range(a1, b1 + 1):
            y = round((a*x)+b)
            pixels[x,y] = (0, 0, 0)        
    else:
        for y in range(a2, b2 + 1):
            x = round((y-b)/a)
            pixels[x,y] = (0, 0, 0)
#
#vykreslenie grafu
#
pic.show()