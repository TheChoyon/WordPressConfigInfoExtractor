# -*- coding: utf-8 -*-
# Coded by 3XPL0173R~X3D
# Date : 15.04.18
# Tested on: Windows
# Python : 2.7
# facebook.com/TheChoyon
# WP Config Data Extractor
# Format: database_name_here username_here password_here localhost
import os
host = ''
password = ''
user = ''
db = ''
def extract(fileName):
    if fileName == 'Extracted.txt':
        return
    lines = open(fileName, 'r').read().split('\n')
    try:
        for i in lines:
            if 'DB_NAME' in i:
                j = i.split("'")
                db = j[3]
            if 'DB_USER' in i:
                j = i.split("'")
                user = j[3]
            if 'DB_PASSWORD' in i:
                j = i.split("'")
                password = j[3]
            if 'DB_HOST' in i:
                j = i.split("'")
                host = j[3]
        open('Extracted.txt', 'a+').write(db + ' ' + user + ' ' + password + ' ' + host + '\n')
    except:
        print 'Configuration File Invalid!'
try:
    os.chdir(os.getcwd() + '/conf')
except:
    print 'Create a folder named conf and put your configs there and run again!'
    exit(0)
for i in os.listdir(os.getcwd()):
    if os.path.isfile(i):
        extract(i)
print 'Done with job mate! Check the Extracted.txt file in the same folder!'
