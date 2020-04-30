from textbot import EmailAgent


def test_emailagent(smtpserver):
    host=smtpserver.addr[0]
    port=smtpserver.addr[1]
    username = 'foo@example.com'
    password = 'foo'
    agent = EmailAgent(host, port, username, password)
    agent.send(
        username,
        'bar@example.com',
        'Just for test',
        'Hi baby',
    )
    assert len(smtpserver.outbox) == 1
