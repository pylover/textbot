from textbot import EmailAgent, router


def test_router():
    assert router.route('Send an email to Sarah') == EmailAgent

