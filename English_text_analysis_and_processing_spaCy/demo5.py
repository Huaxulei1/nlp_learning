import spacy
import nltk
from nltk.chunk import conlltags2tree
nlp = spacy.load('en_core_web_sm')

doc = nlp("Next week I'll be in Shanghai.")
#  词性标准
print([(token.text,token.tag_) for token in doc] )

# 命名实体识别
iob_tagged = [
    (
        token.text,
        token.tag_,
        "{0}-{1}".format(token.ent_iob_,token.ent_type_) if token.ent_iob_ != 'O' else token.ent_iob_
    ) for token in doc

]

print(iob_tagged)

print(conlltags2tree(iob_tagged))


