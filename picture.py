from PIL import Image, ImageGrab
import time, pyautogui

def takePictures(amount, box=(343,105,2557,1315)):
    print("Taking {} screenshots in 5 seconds".format(amount))
    time.sleep(5)
    for i in range(amount):
        print("Picture " + str(i))
        img = ImageGrab.grab(bbox=box)
        save_path = ".\snapshots\\{}.png".format(i)
        img.save(save_path)
        pyautogui.press('left')

def cropPicture(picture, columns=18, newbox=(104,89,2079,1126)):
    fit_img = picture.crop(newbox)
    phrases = []
    width, height = fit_img.size
    box_size = width/columns
    for i in range(columns):
        phrase_new = fit_img.crop((width-(i+1)*box_size, 0, width-(i)*box_size, height))
        phrases.append(phrase_new)
        save_path = ".\phrase_test\\{}.png".format(i)
        phrase_new.save(save_path)
    
    




# takePictures(35)
cropPicture(Image.open('.\\snapshots\\30.png'))


        

