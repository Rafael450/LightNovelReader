from functions import take_pictures, crop_picture, symbol, is_page_picture
from PIL import Image
from manga_ocr import MangaOcr
from classes import *





if __name__ == "__main__":
     

    amount = int(input("Input how many picture will be taken:"))
    take_pictures(amount=amount)

    lines_img = []
    pages = []


    for i in range(amount):
        image = Image.open('.\\snapshots\\{}.png'.format(i))
        if not is_page_picture(image):
            lines_img += crop_picture(image)
        else:
            pages.append(i)

        
        

    
    mocr = MangaOcr()
    
    prev_line = None
    first_line = None
    x = 0
    for img in lines_img:

        if symbol(img) == 'White':
            line = Line(img, ' ', prev_line)
        elif symbol(img) == 'Text':
            text = mocr(img)
            line = Line(img, text, prev_line)
        else:
            line = Line(img, symbol(img).upper(), prev_line)
        
        if prev_line == None:
            first_line = line

        prev_line = line
        
        x+=1
        print(x)
        
    last_line = first_line

    phrases = []
    phrases.append(Phrase(first_line, None))

    while last_line != None:
        phrases.append(Phrase(last_line, phrases[-1]))
        last_line = last_line.find_next_first()
    
    x=0

    with open("text.txt", "w", encoding='utf8') as file:
        for text_line in phrases:
            file.write(text_line.text + "\n")
            print(f'Line {x}')
            x+=1



