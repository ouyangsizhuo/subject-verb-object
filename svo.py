import spacy
import re
from collections import defaultdict
nlp = spacy.load('en_core_web_sm')
word_pos_dict = {}
sent = "A girl who dresses a white T-shirt is my sister."
doc = nlp(sent)
for token in doc:
    word_pos_dict[token.dep_] = token.text
print(word_pos_dict)
print(word_pos_dict['nsubj'],word_pos_dict['ROOT'],word_pos_dict['dobj'])

"""
token.text: 单词
token.i: 单词序号
token.idx: 单词起始位置
token.dep_: 依存关系
"""

"""
det: determiner决定词，如冠词等
nsubj : nominal subject，名词主语

"""
