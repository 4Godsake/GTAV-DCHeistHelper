import os
from time import time

from fingerprint import *
from image import capture_screenshot, check_fingerprint, TEMP_PATH
from keyboard_input import click, keys


def result_message(successful, start, end):
    elapsed = round(end - start, 2)

    if successful:
        print('Hacked in ' + str(elapsed) + ' seconds!')
    else:
        print('you just found a bug...')


def hack():
    screenshot = capture_screenshot()
    found = 0
    number = 1

    for f in FINGERPRINTS:
        result = check_fingerprint(f.x1, f.y1, f.x2, f.y2, screenshot)
        print(str(number) + ': ' + str(result))
        number += 1
        if result:
            found += 1
        if found == 4:
            click(keys.get('tab'))
            return True
        click(f.key_code)

    return False


def start_hacking():
    print('===== start =====')
    start = time()
    successful = hack()
    end = time()
    if os.path.exists(TEMP_PATH):
        os.remove(TEMP_PATH)
    result_message(successful, start, end)
    print('===== end =====\n')
