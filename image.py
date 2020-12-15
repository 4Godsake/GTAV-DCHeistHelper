import os

from PIL import ImageGrab, Image
from python_imagesearch.imagesearch import imagesearcharea, region_grabber

from keyboard_input import click, keys
from utils import get_game_resolution

print("========== GTAV DC Heist Helper ==========")
print("=          Author: 4Godsake              =")
print("=          E-mail:1025744898@qq.com      =")
print("==========================================")
w, h = get_game_resolution()
TEMP_PATH = os.getenv('LOCALAPPDATA') + '\\Temp\\fingertip.png'


def check_fingerprint(x1, y1, x2, y2, image):
    fingertip = region_grabber((x1, y1, x2, y2))
    fingertip.save(TEMP_PATH)
    if imagesearcharea(TEMP_PATH, w * 0.495, h * 0.125, w * 0.7, h * 0.625, 0.425, image) != [-1, -1]:
        click(keys.get('enter'))
        return True
    return False


def capture_screenshot():
    multiplier = 0.8
    screenshot = ImageGrab.grab()
    screenshot.thumbnail((screenshot.size[0] * multiplier, screenshot.size[1] * multiplier), Image.ANTIALIAS)
    return screenshot
