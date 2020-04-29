from bddcli import Given, stdout, Application, when, given, status

from textbot import __version__
from textbot import languages

apptextbot = Application('textbot', 'textbot.cli:TextBot.quickstart')


def test_version():
    with Given(apptextbot, '--version'):
        assert stdout.startswith(__version__)


def test_getdb():
    with Given(apptextbot, ' getdb -language '):
        when(given + 'english')
        assert stdout.endswith("('en_core_web_sm')\n")

        when(given + 'spanish')
        assert stdout.endswith("('es_core_news_sm')\n")

        when(given + 'german')
        assert stdout.endswith("('de_core_news_sm')\n")

        when(given + 'french')
        assert stdout.endswith("('fr_core_news_sm')\n")

        when(given + 'multi-language')
        assert stdout.endswith("('xx_ent_wiki_sm')\n")

        when(given + 'foo')
        assert stdout.endswith('We dont find your choice in our database\n')

    with Given(apptextbot, ' getdb -list '):
        assert stdout.endswith((', '.join(list(languages.keys()))) + '\n')
