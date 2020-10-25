import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("Hello World! My name is Cordelia")
for token in doc:
    print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t".format(
        token.text,              # 文本形式
        token.idx,               # 索引
        token.lemma_,            # token对象的标准形式
        token.is_punct,          # 是否为标点符号
        token.is_space,          # 是否为空格
        token.shape_,            # 形式 大写X 小写 x
        token.pos_,              # 词性标注
        token.tag_
    ))
for sent in doc.sents:
    print(sent)