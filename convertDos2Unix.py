# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:26:51 2020

@author: phamk
"""



WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

file_path = open(r"E:\AI\Yolo\MiAI_Yolo_2\darknet\train.txt", 'rb')

#with open(file_path, 'rb') as open_file:
content = file_path.read()

content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)


file_path = open(r"E:\AI\Yolo\MiAI_Yolo_2\darknet\train.txt", 'wb')
#with open(file_path, 'wb') as open_file:
file_path.write(content)
#print(content)

"""
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

file_path = r"/darknet/train.txt"

with open(file_path, 'rb') as openn:
openn.read()

content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

with open(file_path, 'wb') as open_file:
open_file.write(content)
"""