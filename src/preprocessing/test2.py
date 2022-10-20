from hashlib import new
import os

f = open(r'src\preprocessing\vi_stopwords.txt', 'r', encoding='"utf-8"')
fout = open(r'src\preprocessing\vi_stopwords_adjusted.txt', 'a', encoding='"utf-8"')

lines = f.readlines()

for line in lines:
    new_line = line.replace(' ', '_')
    fout.write(new_line)

fout.close()