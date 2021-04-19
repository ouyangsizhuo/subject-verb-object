import spacy
import re
from collections import defaultdict
nlp = spacy.load('en_core_web_sm')
alltext = []
sentext = []
with open('.\\Harry Potter 1.txt','r') as text:
    for lines in text:
        if lines=='\n':
            continue
        else:
            line = lines.strip().split('\n')
        #print(line)
        alltext.append(line)   # 去掉空行后的文本
    #print(alltext)
    for sens in alltext:
        text_sentences = nlp(sens[0])
        #print(text_sentences)
        for sentence in text_sentences.sents:
            sentext.append(sentence)   #分句后的文本
    #print(sentext)
    word_pos_dict = defaultdict(str)
    for sen in sentext:
        H = re.findall(r"\bHarry\b",str(sen))
        if H:
            doc = nlp(str(sen))
        else:
            continue
        #print(doc)
        for token in doc:
            word_pos_dict[token.dep_] = token.text
        print(word_pos_dict['nsubj'],word_pos_dict['ROOT'],word_pos_dict['dobj'])
        word_pos_dict = defaultdict(str)