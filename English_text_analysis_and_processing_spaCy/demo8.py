# 词汇与文本相似度
import spacy
from scipy import spatial

nlp = spacy.load('en_core_web_lg')

banana = nlp.vocab['banana']
dog = nlp.vocab['dog']
fruit = nlp.vocab['fruit']
animal = nlp.vocab['animal']

#  print(dog.similarity(animal),dog.similarity(fruit))
#  print(banana.similarity(animal),banana.similarity(fruit))

target = nlp("Cats are beautiful animals.")

doc1 = nlp("Dogs are awesome.")
doc2 = nlp("Some gorgeous creatures are felines.")
doc3 = nlp("Dolphins are swimming mammals.")

print(target.similarity(doc1))
print(target.similarity(doc2))
print(target.similarity(doc3))