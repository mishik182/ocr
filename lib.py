import os
import re
import cv2 as cv
import pytesseract

alpha = 0.5
beta = 0

# with open('eng_dict.txt') as eng_dict:
#     valid_eng_words = set(eng_dict.read().split())
#
# with open('rus_dict.txt') as rus_dict:
#     valid_rus_words = set(rus_dict.read().split())


def read_write_image(path):
    global alpha
    alpha += 0.2
    image = cv.imread(path)
    if alpha > 1.5:
        return
    convert_image = cv.convertScaleAbs(image, alpha=alpha, beta=0)
    cv.imwrite(path, convert_image)


def get_text(path, lang):
    global alpha
    alpha = 0.5
    return {'data': get_image_text(path, lang)}


def get_image_text(path, lang):
    for item in pytesseract.image_to_string(path, lang=lang).split():
        read_write_image(path)
    return pytesseract.image_to_string(path, lang=lang)
