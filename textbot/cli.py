import easycli



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
        # FIXME: Add an argument to print the list of available languages"
        easycli.Argument(
            'language', default='english', help='Language that you want',
        ),
    ]

    def __call__(self, args):
        from spacy.cli import download
        # FIXME: Print appropriate error message if language not found"
        language = languages[args.language]
        download(language)


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
