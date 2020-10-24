# 很多时候我们需要对英文当中的时态语态等进行归一化，这个时候我们就需要stemming和emmatizing的操作了
# 比如running表示进行时，但是这个词表征的含义与“run”一致，我们在识别语义的时候，希望消除这种差异化。


import nltk 
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("makes"))