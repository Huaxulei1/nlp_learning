import spacy

nlp = spacy.load('en_core_web_sm')
doc  = nlp('Hello World! My name is Cordelia')
for token in doc:
    print('"' + token.text + '"')