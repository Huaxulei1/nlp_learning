import numpy as np
import pandas as pd
import nltk
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#  加载数据
data = pd.read_csv("emotion_data.csv")
#  print(data.shape)

#  print(data.head())

#  打印不同的情感种类
#  print(data.sentiment.unique())

#  以下步骤是在进行数据的预处理
#  1、排除无关项
data = data.drop(data.columns[[0,2]],axis=1)

def preprocessing(text):
    #分词
    token_words = word_tokenize(text)
    #去除停用词
    stop_words = stopwords.words('english')
    fileter_words = [word for word in token_words if word not in stop_words]
    #stemmer
    stemmer = PorterStemmer()
    fileterStem_words = [stemmer.stem(word) for word in fileter_words]
    
    return ' '.join(fileterStem_words) #返回一个字符串  以空格间隔
 
#使用apply对content字段的所有文本进行处理 矢量化编程 避免显式for循环 速度快
data['content'] = data['content'].apply(preprocessing)
print(data['content'][0])#content字段的第一条文本 处理之后

dataset = data.values #将DataFrame转换为矩阵/2维数组
print(dataset.shape)
#提取特征(第2列 处理后的文本)
features = dataset[:,1]
print(features[100])
#提取标签/sentiment(第1列)
target = dataset[:,0]

# 使用LabelEncoder对不同的情感target进行编码 把不同的情感转换为数字
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
print(target)
target_processed = le.fit_transform(target) 
print(target_processed)
print(le.classes_) #anger对应数字0 依次类推

# 对输入的文本进行特征抽取和表示(这里用到的tf-idf特征之后会学习) 
#数字化 把文本表示成特征向量(1*42725维的稀疏向量)
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
X_processed = tfidf.fit_transform(features)
print(X_processed.shape) #特征矩阵 40000条文本  每行代表一个文本的特征向量
print(X_processed[0].shape)
print(X_processed[0]) #稀疏向量

X_train, X_test, y_train, y_test = train_test_split(X_processed, target_processed, test_size=0.25, random_state=42)

#使用简单的逻辑回归模型
lr = LogisticRegression()
lr.fit(X_train, y_train)

lr.score(X_test, y_test)

test_ex = "It is so intersting"
test_ex = preprocessing(test_ex)
text_ex_processed = tfidf.transform([test_ex])
print(lr.predict(text_ex_processed)) #预测的情感索引
print(le.classes_[lr.predict(text_ex_processed)]) #预测的情感