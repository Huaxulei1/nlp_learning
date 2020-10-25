import spacy
import nltk
from nltk.chunk import conlltags2tree
nlp = spacy.load('en_core_web_sm')

doc = nlp("Next")


