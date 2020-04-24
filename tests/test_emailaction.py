from textbot import EmailAction, nlp


def test_router():
    assert isinstance(
        nlp.assignaction(nlp.tag("send an Email to Parsa.")), EmailAction
    )
    assert isinstance(
        nlp.assignaction(nlp.tag("send an email to sarah.")), EmailAction
    )
