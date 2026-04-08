from PIL import Image
#
# tvorba obrazka
#
pic = Image.new("RGB",(200, 300), "white")
pixels = pic.load()
count = 1
#
# tvorba sachovnice
#
for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        if y % 2 == 0:
            if count % 2 == 0:
                pixels[x,y] = (256,256,256)
                count += 1
            else:
                pixels[x,y] = (0,0,0)
                count +=1
        else:
            if count % 2 == 0:
                pixels[x,y] = (0,0,0)
                count += 1
            else:
                pixels[x,y] = (256,256,256)
                count += 1

pic.show()