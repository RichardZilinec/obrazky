from PIL import Image
#
# nacitanie hodnot zo suboru
#
text_seda = open("ciernobiely_obrazok_1.txt", "r")
first_line = text_seda.readline()
size = first_line.split(" ")

#
# vytvorenie obr.
#
pic = Image.new("L", (int(size[0]), int(size[1])),"white")
pixel = pic.load()

#
#
#
for y in range(pic.size[1]):
    lines = text_seda.readline()
    #print(y)
    for x in range(pic.size[0]):
        color = lines[x*2:x*2+2]
        print(color)
        pixel[x,y] = (int(color,16))

pic.show()