from PIL import Image
def picture_unshreder(pic):
    obr = Image.open(pic)
    pixels = obr.load()
    bin_message = ""
    vysledny_text = ""
    index = 0
    
    while True:
        x = index % obr.size[0]
        y = index // obr.size[0]

        blue_val = pixels[x, y][2]
        posledny_bit = bin(blue_val)[-1]
        bin_message += posledny_bit

        if len(bin_message) == 7:
            znak = chr(int(bin_message, 2))

            if znak == '#':
                break
                
            vysledny_text += znak
            bin_message = ""
            
        index += 1

        if index >= obr.size[0] * obr.size[1]:
            break
            
    return vysledny_text


obr_out = 'final_pic17.png'

print(picture_unshreder(obr_out))
