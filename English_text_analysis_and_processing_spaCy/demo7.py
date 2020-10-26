# 词向量计算

import spacy
from scipy import spatial

nlp = spacy.load('en_core_web_lg')

#  print(nlp.vocab['banana'].vector)

# 余弦相似度计算
cosine_similarity = lambda x,y: 1 - spatial.distance.cosine(x,y)

# 男人、女人、国王、女王的词向量
man = nlp.vocab['man'].vector
woman = nlp.vocab['woman'].vector
queen = nlp.vocab['queen'].vector
king = nlp.vocab['king'].vector

# 我们对向量做一个简单计算 "man" - "woman" + "queen"
maybe_king = man - woman + queen
computed_similiarities = []

# 扫描整个词库的词向量做对比，召回最接近的词向量
for word in nlp.vocab:
    if not word.has_vector:
        continue

    similarity = cosine_similarity(maybe_king,word.vector)
    computed_similiarities.append((word,similarity))

# 排序与最接近结果展示
computed_similiarities = sorted(computed_similiarities,key=lambda item:-item[1])
print([w[0].text for w in computed_similiarities[:10]])
