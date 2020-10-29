# 英文文本处理与spaCy

[spaCy](https://spacy.io/)是Python和Cython中的高级自然语言处理库，它建立在最新的研究基础之上，从一开始就设计用于实际产品。spaCy 带有预先训练的统计模型和单词向量，目前支持 20 多种语言的标记。它具有世界上速度最快的句法分析器，用于标签的卷积神经网络模型，解析和命名实体识别以及与深度学习整合。

#### 0.英文Tokenization(标记化/分词)

> 文本是不能成段送入模型中进行分析的，我们通常会把文本切成有独立含义的字、词或者短语，这个过程叫做tokenization，这通常是大家解决自然语言处理问题的第一步。在spaCY中同样可以很方便地完成Tokenization。

代码：https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_spaCy   /demo1和demo2



#### 1.词性标注

> 词性（part-of-speech）是词汇基本的语法属性，通常也称为词性。

> 词性标注（part-of-speech tagging）,又称为词类标注或者简称标注，是指为分词结果中的每个单词标注一个正确的词性的程序，也即确定每个词是名词、动词、形容词或者其他词性的过程。

> 词性标注是很多NLP任务的预处理步骤，如句法分析，经过词性标注后的文本会带来很大的便利性，但也不是不可或缺的步骤。 词性标注的最简单做法是选取最高频词性，主流的做法可以分为基于规则和基于统计的方法，包括：

- 基于最大熵的词性标注
- 基于统计最大概率输出词性
- 基于HMM的词性标注

代码：https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_spaCy   /demo5



#### 2.命名实体识别

> 命名实体识别（Named Entity Recognition，简称NER），又称作“专名识别”，是指识别文本中具有特定意义的实体，主要包括人名、地名、机构名、专有名词等。通常包括两部分：1) 实体边界识别；2) 确定实体类别（人名、地名、机构名或其他）。

代码：https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_spaCy   /demo5



#### 3.chunking/组块分析

> spaCy可以自动检测名词短语，并输出根(root)词，比如下面的"Journal","piece","currencies"

代码：https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_spaCy   /demo4



#### 4.句法依存解析

> spaCy有着非常强大的句法依存解析功能，可以试试对句子进行解析。

代码：https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_spaCy   /demo6



#### 5.词向量使用

> NLP中有一个非常强大的文本表示学习方法叫做word2vec，通过词的上下文学习到词语的稠密向量化表示，同时在这个表示形态下，语义相关的词在向量空间中会比较接近。也有类似`v(爷爷)-v(奶奶) ≈ v(男人)-v(女人)`的关系。

> 如果大家要使用英文的词向量，需要先下载预先训练好的结果。

> 命令：!python3 -m spacy download en_core_web_lg

代码：https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_spaCy   /demo7



#### 6.词汇与文本相似度

在词向量的基础上，spaCy提供了从词到文档的相似度计算的方法，下面的例子是它的使用方法。

代码：https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_spaCy   /demo8

