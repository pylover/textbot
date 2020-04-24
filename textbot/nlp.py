import spacy
from .emailaction import EmailAction


def tag(input):
    result = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input)

    for token in doc:
        if token.pos_ == "NOUN":
            result.append(token.text)
    return result


def assignaction(names):
    for item in names:
        if item.lower() == "email":
            emailinstance = EmailAction()
            return emailinstance
