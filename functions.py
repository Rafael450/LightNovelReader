from PIL import ImageOps, ImageGrab
import numpy as np
import time, pyautogui

def take_pictures(amount, box=(343,105,2557,1315)):
    print("Taking {} screenshots in 5 seconds".format(amount))
    time.sleep(5)

    for i in range(amount):
        print("Picture {}".format(i))
        img = ImageGrab.grab(bbox=box)
        save_path = ".\snapshots\\{}.png".format(i)
        img.save(save_path)
        pyautogui.press('left')

def crop_picture(picture, columns=18, newbox=(104,89,2079,1126)):
    fit_img = picture.crop(newbox)
    phrases = []
    width, height = fit_img.size
    box_size = width/columns

    for i in range(columns):
        phrase_new = fit_img.crop((width-(i+1)*box_size, 0, width-(i)*box_size, height))
        phrases.append(phrase_new)

        save_path = ".\phrase_test\\{}.png".format(i)
        phrase_new.save(save_path)
    
    return phrases

def is_page_picture(page):
    blackness = 255-np.average(ImageOps.grayscale(page))
    return True if blackness > 11 else False

def symbol(phrase):
    blackness = 255-np.average(ImageOps.grayscale(phrase))
    width, height = phrase.size

    fit_img = phrase.crop((0,0,width,height*0.4))
    blackness_fit = 255-np.average(ImageOps.grayscale(fit_img))
    
    if blackness < 0.00001:
        return 'White'
    elif blackness_fit > 0.00001:
        return 'Text'
    elif 1.05 > blackness > 0.85:
        return 'Fire'
    elif 3.75 > blackness > 3.55:
        return 'Chest'
    elif 2.05 > blackness > 1.85:
        return 'Devil'
    
    return 'ERRORRRRRR'
        

def is_top_white(phrase, height=84):
    width, _ = phrase.size
    img_top = ImageOps.grayscale(phrase.crop((0,0,width,height)))
    blackness = 255-np.average(img_top)
    return True if blackness < 0.00001 else False

def line_concat(first_line):
    text = first_line.text
    if first_line.next_line != None:
        if not first_line.next_line.is_line_start:
            text += line_concat(first_line.next_line)

    return text
