import os
import re

path = "./files_to_rename"

# rename each file by replacing anything that isn't a letter or number with an underscore
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename),os.path.join(path, filename.replace(' ', '_').replace(',', '').replace('：', '').replace('&', 'and').replace("'", "").replace('!', '').replace('+', '_').replace('(', '_').replace(')', '_').replace('[', '_').replace(']', '_').replace('|', '_').replace('⧸', '_').replace('｜', '_').replace('__', '_').replace('___', '_').replace('____', '_')))
