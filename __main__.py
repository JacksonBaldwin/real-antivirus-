import os
import random
from datetime import datetime

#safe password
safety = input('start process?(y/n): ').lower()
if safety != 'y':
    print('wrong key, qutting project...')
    quit()

#grab all files from machine
extensions = ['.txt','.docx',]
file_paths = []
for root, dirs, files, in os.walk('c:\\'):
    for file in files:
        file_path, file_ext =  os.path.splitext(root+'\\'+file)
        if file_ext in extensions:
            file_paths.append(root+'\\'+file)

for f in file_paths:
    print(f)

print('you have 3 viruses')
