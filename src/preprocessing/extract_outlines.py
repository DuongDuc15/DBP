from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from rake_nltk import Rake
from nltk.tokenize import sent_tokenize
import os

def sorting(lst):
    # lst2=sorted(lst, key=len)
    lst2 = sorted(lst, key=len)
    return lst2

def trim_body(body):
    paragraphs = body.replace(' <p> ', '\n').split('\n')
    body_new = []
    par_length = 1

    for par in paragraphs:
        _par = par
        if _par.endswith(' <s>.'):
            _par = _par[:-5]
        temp_body = _par.replace(' <s>', ' ').replace('  ', ' ').strip()
        sentences = _par.replace(' <s>', '\n').replace('  ', ' ').strip().split('\n')

        if len(paragraphs) == 1:
            s = 0
            first = True

            while len(sentences[s].split(' ')) < 4 or '::act ' in sentences[s].lower() or ' act:' in sentences[s].lower():
                s+=1
                if s == len(sentences):
                    return None
            body_new.append('<o> ' + sentences[s].replace(' <s> ', ' ').strip())
            s+=1

            while s < len(sentences) and len(body_new)< 5:
                body_new.append('<o>')
                curr_len = 0
                while s < len(sentences) and curr_len + len(sentences[s].split(' ')) < 400:
                    if ':act ' in sentences[s].lower() or 'act: ' in sentences[s].lower() :
                        s+=1
                        break

                    if len(sentences[s]) > 10:
                        curr_len += len(sentences[s].replace(' <s> ', ' ').strip().split(' '))
                        body_new[len(body_new) - 1] += " " + sentences[s].replace(' <s> ', ' ').strip()
                        body_new[len(body_new) - 1] = body_new[len(body_new) - 1].strip()
                    s += 1

        else:
            if par_length >5:
                s = 0
                while s < len(sentences) and len(sentences[s]) > 10 and (len(body_new[len(body_new)-1].split(' ')) + len(sentences[s].split(' '))) < 400:
                    if len(sentences[s]) > 10:
                        body_new[len(body_new) - 1] += " " + sentences[s].replace(' <s> ', ' ').strip()
                        body_new[len(body_new) - 1] = body_new[len(body_new) - 1].strip()
                    s+=1
            else:
                if len(temp_body) > 10 and len(temp_body.split(' ')) <= 400:
                    body_new.append(temp_body.replace(' <s>', ' ').replace('  ', ' ').strip())

                elif len(temp_body.split(' ')) >400:
                    curr_len  = 0
                    newstr = ''
                    for sent in sentences:
                        if len(newstr.split(' ')) + len(sent.split(' ')) <= 400:
                            newstr += (' '+ sent).strip()
                        else:
                            break
                    body_new.append(newstr.replace(' <s>', ' ').replace('  ', ' ').strip())

        par_length+=1

    return body_new