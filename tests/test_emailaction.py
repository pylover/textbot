from textbot import action,router


def test_router():
    assert isinstance(
        router.specifyaction(router.parse("send an Email to Parsa.")),
        action.EmailAction
    )
    assert isinstance(
        router.specifyaction(router.parse("send an email to sarah."))
        ,action.EmailAction
    )
