import nltk
#nltk.download('punkt')
# 导入内置分词器和分句器
from nltk import word_tokenize,sent_tokenize
# 导入内置停用词
from nltk.corpus import stopwords
# 导入词性标注工具
from nltk import pos_tag
# 导入正则表达式分块器
from nltk.chunk import RegexpParser
import matplotlib
matplotlib.use('Agg')

# 读入数据
corpus = open('1.txt','r').read()
# 查看数据类型
# print("corpus的数据类型是",type(corpus))


# 断句
sentences =sent_tokenize(corpus)
#  print(sentences)

# 分词
words = word_tokenize(corpus)
#  print(word[:20])

# 输出开头10个停用词
stop_words = stopwords.words('english')
#  print(stop_words[0:10])


# 使用列表推导式去掉停用词
filtered_corpus = [w for w in words if not w in stop_words]
#  print(filtered_corpus[:20])

# 查看停用词总量
#  print("语料词数量为：",len(words))
# 查看使用的停用词总量
#  print("停用词数量为：",len(filtered_corpus))
# 查看总共剔除的停用词数量
#  print("我们总共剔除的停用词数量为：",len(words)-len(filtered_corpus))

tags = pos_tag(filtered_corpus)
#  print(tags[:20])

# 写一个匹配名词的正则表达式
pattern = """NP: {<JJ>*<NN>+}"""

# 定义组块分析器
chunk = RegexpParser(pattern)

# 对一段文本进行分句
tokenized_sentence = nltk.sent_tokenize(corpus)

# 对一段文本进行分词
tokenized_words = [word_tokenize(sentence) for sentence in tokenized_sentence]

# 对一段文本进行词性标注
tagged_words = [nltk.pos_tag(word) for word in tokenized_words]

# 识别NP模块
word_tree = [chunk.parse(word) for word in tagged_words]


word_tree[0].draw()