from bddcli import Given, stdout, Application

from textbot import __version__


app = Application('textbot', 'textbot.cli:TextBot.quickstart')



def test_version():
    with Given(app, '--version'):
        assert stdout.startswith(__version__)

