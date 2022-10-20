from hashlib import new
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
# Tokenizing
toolkit_path = r"C:\Users\Admin\Documents\Learning\DBP\code\coding\src\preprocessing\toolkit"
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



infile = r'C:\Users\Admin\Documents\Learning\DBP\code\coding\src\preprocessing\raw\out_content.txt'
outfile = r'C:\Users\Admin\Documents\Learning\DBP\code\coding\src\preprocessing\preproccessed\data_content.txt'

f = open(infile, 'r', encoding='"utf-8"')
fout = open(outfile, 'a', encoding='"utf-8"')

text = f.read()
data = preprocessing(text)

fout.write(data)

f.close()
fout.close()