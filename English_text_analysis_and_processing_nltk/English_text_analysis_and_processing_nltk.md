# 英文文本处理与NLTK

NLTK，全城Natural Language Toolkit，自然语言处理工具包，是NLP研究领域常用的一个Python库，由宾夕法尼亚大学在Python的基础上开发的一个模块，至今已有超过十万行代码。是一个开源项目，包含数据集、Python模块、教程等；NLTK是最常用的英文自然语言处理Python基础库之一。

### 1.英文Tokenization（标记化/分词）

> 文本是不能成段送入模型中进行分析的，我们通常会把文本切成有独立含义的字、词或者短语，这个过程叫做tokenization，这通常是解决自然语言处理问题的第一步。在NLTK中提供了2中不同的tokenization，sentence_tokenization和word_tokenization，前者把文本进行“断句”，后者对文本进行“分词”。

代码见   https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_nltk   中的demo1

### 2.停用词

> 在自然语言处理的很多任务中，我们处理的主体“文本”中有一些功能词经常出现，然而对于最后的任务目标并没有帮助，甚至会对统计方法带来一些干扰，我们把这类词叫做停用词，通常我们会用一个停用词表把它们过滤出来。比如英语当中的定冠词/不定冠词(a,an,the等)。

代码见   https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_nltk   中的demo1

### 3.词性标注

> 词性（part-of-speech）是词汇基本的语法属性，通常也称为词性。
>
> 词性标注（part-of-speech tagging）,又称为词类标注或者简称标注，是指为分词结果中的每个单词标注一个正确的词性的程序，也即确定每个词是名词、动词、形容词或者其他词性的过程。
>
> 词性标注是很多NLP任务的预处理步骤，如句法分析，经过词性标注后的文本会带来很大的便利性，但也不是不可或缺的步骤。 词性标注的最简单做法是选取最高频词性，主流的做法可以分为基于规则和基于统计的方法，包括：
>
> 基于最大熵的词性标注
> 基于统计最大概率输出词性
> 基于HMM的词性标注

代码见   https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_nltk   中的demo1

具体的词性标注编码和含义

![img](https://img2018.cnblogs.com/blog/1152413/201904/1152413-20190410104159044-1813153570.png)

### 4.chunking/组块分析

> 分块是命名实体识别的基础，词性给出来的句子成分的属性，但有时候，更多的信息(比如句子句法结构)可以帮助我们对句子中的模式挖掘更充分。举个例子，”古天乐赞助了很多小学“中的头部古天乐是一个人名(命名实体)
>
> 组块分析是一个非常有用的从文本抽取信息的方法，提取组块需要用到正则表达式：

代码见   https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_nltk   中的demo1

### 5.命名实体识别

> 命名实体识别（Named Entity Recognition，简称NER），又称作“专名识别”，是指识别文本中具有特定意义的实体，主要包括人名、地名、机构名、专有名词等。通常包括两部分：1) 实体边界识别；2) 确定实体类别（人名、地名、机构名或其他）。

代码见  https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_nltk   中的demo3

### 6.Stemming和Lemmatizing

> 很多时候我们需要对英文当中的时态语态等做归一化，这个时候我们就需要stemming和lemmatizing这样的操作了。比如"running"是进行时，但是这个词表征的含义和"run"是一致的，我们在识别语义的时候，希望能消除这种差异化。

代码见  https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_nltk   中的demo4

### 7.WordNet与词义解析

代码见  https://github.com/Huaxulei1/nlp_learning/tree/master/English_text_analysis_and_processing_nltk   中的demo2