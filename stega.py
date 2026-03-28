from PIL import Image

def sprava_to_bin(message):
    message += '#'
    output = ''
    for char in message:
        temp = bin(ord(char))[2::]
        if len(temp) < 7:
            pocet = 7 - len(temp)
            temp = '0'*pocet + temp
        output += temp
    return output

def picture_shreder(bin_message,pic,pic2):
    obr = Image.open(pic)
    pixels = obr.load()
    for i in range (len(bin_message)):
        x = i % obr.size[0]
        y = i// obr.size[0]
        blue_bin = bin(pixels[x,y][2])[2:-1:]
        blue_bin = blue_bin + bin_message[i]
        new_blue = int(blue_bin, 2)
        pixels[x,y] = (pixels[x,y][0], pixels[x,y][1], new_blue)
    obr.save(pic2)

def picture_unshreder(pic):
    obr = Image.open(pic)
    pixels = obr.load()
    
    bin_message = ""
    vysledny_text = ""
    index = 0
    
    while True:
        # 1. Získame súradnice x, y rovnako ako pri šifrovaní
        x = index % obr.size[0]
        y = index // obr.size[0]
        
        # 2. Vytiahneme posledný bit z modrej zložky (index 2)
        blue_val = pixels[x, y][2]
        posledny_bit = bin(blue_val)[-1]
        bin_message += posledny_bit
        
        # 3. Každých 7 bitov skúsime previesť na znak
        if len(bin_message) == 7:
            znak = chr(int(bin_message, 2))
            
            # Ak narazíme na zarážku '#', končíme
            if znak == '#':
                break
                
            vysledny_text += znak
            bin_message = "" # Vynulujeme zásobník pre ďalší znak
            
        index += 1
        
        # Bezpečnostná poistka pre prípad, že by sme prešli celý obrázok
        if index >= obr.size[0] * obr.size[1]:
            break
            
    return vysledny_text

# Použitie:
# print("Dekódovaná správa:", picture_unshreder('sprava_pre_priatela.png'))

obr_in = "Nature_celebrating_India.png"
obr_out = 'sprava_pre_priatela.png'
sprava = input("zadaj mi spravu :")

bin_message = sprava_to_bin(sprava)
picture_shreder(bin_message, obr_in, obr_out)
print(picture_unshreder(obr_out))

#print(bin_message)