# 基于displacy做可视化的命名实体识别

import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("I just bought 2 shares at 9 a.m. beacuse the stock went up 30% in just 2 days according to the WSJ")

print(displacy.render(doc,style='ent',jupyter=False))