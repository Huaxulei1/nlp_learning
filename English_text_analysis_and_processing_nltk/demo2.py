import nltk
# 导入wordnet语义词典
from nltk.corpus import wordnet as wn

# 输出与dog有关联的单词语义
#  print(wn.synsets('dog'))
# 输出apple的第一种语义
#  print(wn.synsets('apple')[1].definition())

print(wn.synsets('dog'))

# 以dog的名词形式第一种语义来造句

print(wn.synset('dog.n.01').examples())
