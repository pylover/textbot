import easycli
from bddcli import stdout


languages = {
    'english': 'en_core_web_sm',
    'german': 'de_core_news_sm',
    'french': 'fr_core_news_sm',
    'spanish': 'es_core_news_sm',
    'multi-language': 'xx_ent_wiki_sm',
}


class DownloadSpacyDatabase(easycli.SubCommand):
    __command__ = 'getdb'
    __arguments__ = [
        easycli.Argument('-language', help='Language that you want',),
        easycli.Argument(
            '-list',
            action='store_true',
            help='List of language that you can choose',
        ),
    ]

    def __call__(self, args):
        from spacy.cli import download

        if args.language:
            try:
                download(languages[args.language])
            except:
                print('We dont find your choice in our database')

        if args.list:
            print('You can choose the language that is in list')
            print(', '.join(list(languages.keys())))


class TextBot(easycli.Root):
    __completion__ = True
    __help__ = 'A simple text assistant'
    __arguments__ = [
        easycli.Argument(
            '-v', '--version', action='store_true', help='Show version'
        ),
        DownloadSpacyDatabase,
    ]

    def __call__(self, args):
        if args.version:
            from textbot import __version__

            print(__version__)
            return

        return super().__call__(args)
