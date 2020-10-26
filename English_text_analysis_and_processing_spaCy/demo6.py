import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp('Wall Street Journal just published an interesting piece on crypto currencies')

for token in doc:
    print("{0}/{1} <--{2}-- {3}/{4}".format(
        token.text,token.tag_,token.dep_,token.head.text,token.head.tag_
    ))