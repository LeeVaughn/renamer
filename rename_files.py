import os

path = "./files_to_rename"

# rename each file by replacing spaces with underscores
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename),os.path.join(path, filename.replace(' ', '_').replace(',', '').replace('&', 'and').replace("'", "").replace('!', '').replace('+', '_').replace('(', '_').replace('(', '_').replace(')', '_').replace('___', '_').replace('__', '_')))
