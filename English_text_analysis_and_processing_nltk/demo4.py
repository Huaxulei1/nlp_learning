# 很多时候我们需要对英文当中的时态语态等进行归一化，这个时候我们就需要stemming和emmatizing的操作了
# 比如running表示进行时，但是这个词表征的含义与“run”一致，我们在识别语义的时候，希望消除这种差异化。

import nltk 
from nltk.stem import PorterStemmer

# stemmer = PorterStemmer()
# print(stemmer.stem("makes"))


# 这样写也可以
from nltk.stem import SnowballStemmer
stemmer2 = SnowballStemmer("english")
#  print(stemmer2.stem("makes"))


# Lemmatization和Stemmer很类似，不同的地方在于它还考虑了词义关联等信息
# Stemmer的速度更快，但是它通常只是一系列的规则
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("read"))