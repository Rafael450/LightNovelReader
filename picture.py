import imaplib
from PIL import ImageOps, ImageGrab, Image
import numpy as np
import time, pyautogui

def take_pictures(amount, box=(343,105,2557,1315)):
    print("Taking {} screenshots in 5 seconds".format(amount))
    time.sleep(5)

    for i in range(amount):
        print("Picture " + str(i))
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
        # save_path = ".\phrase_test\\{}.png".format(i)
        # phrase_new.save(save_path)
    
    return phrases

def is_first_line(phrase, height=84):
    width, _ = phrase.size
    img_top = ImageOps.grayscale(phrase.crop((0,0,width,height)))
    blackness = 255-np.average(img_top)
    print(blackness)
    return True if blackness < 0.5 else False


    
    


for i in range(17):
    print(is_first_line(Image.open('.\\phrase_test\\{}.png'.format(i))))
# takePictures(35)
# cropPicture(Image.open('.\\snapshots\\30.png'))


        

