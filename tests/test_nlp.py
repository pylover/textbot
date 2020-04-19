from textbot import speechtag


def test_sendemail():
    assert speechtag("Send an email to sarah.") == [
        ["Send", "VERB"],
        ["email", "NOUN"],
    ]
    assert speechtag("Send an email to oscar about last meating.") == [
        ["Send", "VERB"],
        ["email", "NOUN"],
        ["meating", "NOUN"],
    ]
