import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp("Wall Street Journal just published an intersting piece on crypto currencies")
for chunk in doc.noun_chunks:
    print(chunk.text,chunk.label_,chunk.root.text)