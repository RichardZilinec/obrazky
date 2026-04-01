from PIL import Image

text_seda = open("ciernobiely_obrazok_1.txt", "r")
first_line = text_seda.readline()
size = first_line.split(" ")
pic = Image.new("RGB", (int(size[0]), int(size[1])),"white")
pixel = pic.load()

for y in range(pic.size[1]):
    lines = text_seda.readline()
    for x in range(pic.size[0]):
        color = lines[x*2:x*2+1]
        if color:
            pixel[x,y] = (int(color,16), int(color,16), int(color,16))
pic.show()
