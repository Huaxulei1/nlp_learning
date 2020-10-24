# 命名实体识别简称NER ，又称为“专名识别，是指是被文本中具有特定意义的实体，主要包括人名、地名、机构名等。


import nltk
from nltk import ne_chunk,pos_tag,word_tokenize

sentence = "Cordelia studies at Nanjing University of Science and Technology."
print(ne_chunk(pos_tag(word_tokenize(sentence))))