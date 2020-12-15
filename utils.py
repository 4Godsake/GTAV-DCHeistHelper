import ctypes
import os
import sys
from ctypes.wintypes import MAX_PATH
from time import sleep


def get_documents_path():
    dll = ctypes.windll.shell32
    buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
    if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
        return buf.value
    else:
        print("Error")
        sys.exit(1)


SETTINGS_PATH = get_documents_path() + '\\Rockstar Games\\GTA V\\settings.xml'


def get_game_resolution():
    if os.path.exists(SETTINGS_PATH):
        settings_file = open(SETTINGS_PATH, 'r')
        contents = settings_file.readlines()
        width = '0'
        height = '0'

        for line in contents:
            if line.__contains__('ScreenWidth value'):
                width = line.split('"')[1]
            elif line.__contains__('ScreenHeight value'):
                height = line.split('"')[1]

        settings_file.close()

        if width != '0' and height != '0':
            print('Detected game resolution: ' + str(width) + 'x' + str(height) + '\n')
            if width != '1920' and height != '1080':
                print('This resolution is not supported!')
            else:
                return int(width), int(height)
    else:
        print('Couldn\'t detect game resolution')

    print('Exiting...')
    sleep(3)
    sys.exit(1)
