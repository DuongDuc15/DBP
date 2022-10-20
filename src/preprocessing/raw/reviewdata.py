import os
import re

from numpy import str_

infile = r'src\preprocessing\raw\data_text.txt'
outfile_tle = r'src\preprocessing\raw\out_title.txt'
outfile_cnt = r'src\preprocessing\raw\out_content.txt'

f = open(infile, 'r', encoding='"utf-8"')
fout_tle = open(outfile_tle, 'a', encoding='"utf-8"')
fout_cnt = open(outfile_cnt, 'a', encoding='"utf-8"')

lines = f.readlines()

str_titles = []

if os.stat(outfile_tle).st_size != 0:
    print (outfile_tle, " exists!")
else:
    for line in lines:
        if re.findall("^[0-9]+\. .", line):
            fout_tle.write(line.split('. ')[1])
            fout_cnt.write("<EOS>\n")
        else:
            fout_cnt.write(line)

# if os.stat(outfile_cnt).st_size != 0:
#     print (outfile_cnt, " exists!")
# else:
#     for line in lines:
#         if not re.findall("^[0-9]+\. .", line):
#             outfile_cnt.write(line)
#         if re.findall("^[0-9]+\. .", line):
#             outfile_cnt.write("<EOS>")

f.close()
fout_tle.close()
fout_cnt.close()

print (len(str_titles))