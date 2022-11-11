# from hashlib import new
import re
import os
import regex
import py_vncorenlp

#=============================================
def cleaning_text(text, keep_punct=True):
    """ 
    Removing non-latin chars
    But keeping numbers and punctuations as default
    """
    if keep_punct:
        return regex.sub(u'[^\p{Latin}0-9[:punct:]]+', u' ', text)
    return regex.sub(u'[^\p{Latin}0-9]+', u' ', text)

#=============================================
# Word segmentation
toolkit_path = r"..\preprocessing\toolkit"
model = py_vncorenlp.VnCoreNLP(annotators=['wseg'], save_dir=toolkit_path)

def tokenizing(text):
    """
    This function returns a list of VNese tokens 
    extracted from a full sentence
    """
    new_text = ' '.join(model.word_segment(text))
    return new_text

#=============================================
def lowercasing(text):
    return text.lower()

#=============================================
# Removing VNese accent(?)
from unidecode import unidecode
def removing_accent(text):
    return unidecode(text)

#=============================================
# Preprocessing Function
def preprocessing(text, lowercase=True, keep_punct=True, keep_accent=True):
    fi_text = cleaning_text(text, keep_punct)
    fi_text = tokenizing(fi_text)
    if lowercase == True:
        fi_text = lowercasing(fi_text)
    if keep_accent == False:
        fi_text = removing_accent(fi_text)
    
    return fi_text



infile = r'C:\Users\Admin\Documents\Learning\DBP\code\coding\src\preprocessing\preproccessed\raw_content.txt'
outfile = r'C:\Users\Admin\Documents\Learning\DBP\code\coding\src\preprocessing\preproccessed\content.txt'

f = open(infile, 'r', encoding='"utf-8"')
fout = open(outfile, 'a', encoding='"utf-8"')

assert os.stat(outfile).st_size == 0, str(outfile, " exists!")

lines = f.readlines()

for line in lines: 
    if line.startswith("<EOS>"):
        fout.write('\n<EOS>\n')
    else:       
        if not re.match('^\n$', line):
            text = preprocessing(line).replace('.', '.\n')
            fout.write(text)

f.close()
fout.close()
