from textbot import action,router


def test_router():
    assert isinstance(
        router.assignaction(router.tag("send an Email to Parsa.")),action.EmailAction
    )
    assert isinstance(
        router.assignaction(router.tag("send an email to sarah.")),action.EmailAction
    )
