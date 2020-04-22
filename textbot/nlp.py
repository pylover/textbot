import spacy


def tag(input):
    result = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input)

    for token in doc:
        if token.pos_ == "VERB" or token.pos_ == "NOUN":
            result.append([token.text, token.pos_])

    return result
