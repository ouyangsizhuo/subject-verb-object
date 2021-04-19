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
amod: adjectival modifier形容词
punct: punctuation，标点
dobj : direct object直接宾语
ROOT: root，最重要的词，从它开始，根节点
poss: possession modifier，所有形式，所有格，所属
attr: attributive，定语
relcl：relative clause 关系从句 
compound：复合语
"""
