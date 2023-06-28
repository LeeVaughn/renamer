import os
import re

path = "./files_to_rename"

# rename each file by replacing anything that isn't a letter or number with an underscore
for filename in os.listdir(path):
    new_filename = re.sub('[^A-Za-z0-9]+', '_', filename)
    os.rename(os.path.join(path,filename),os.path.join(path, new_filename))
