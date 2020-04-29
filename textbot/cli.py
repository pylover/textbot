import easycli
import plac

from spacy.cli import download


_version__ = "0.1.0"


def foo():  # pragma: no cover
    print(" ".join(sys.argv))


languages = {
    "English": "en_core_web_sm",
    "German": "de_core_news_sm",
    "French": "fr_core_news_sm",
    "Spanish": "es_core_news_sm",
    "Multi-language": "xx_ent_wiki_sm",
}


class Download(easycli.SubCommand):
    __command__ = "download"
    __arguments__ = [
        easycli.Argument(
            "language", default="English", help="Language that you want",
        ),
    ]

    def __call__(args):
        language = languages[args.language]
        plac.call(download, [language])


class Textbot(easycli.Root):
    __completion__ = True
    __help__ = "A simple text assistant"
    __arguments__ = [
        easycli.Argument(
            "-v", "--version", action="store_true", help="Show version"
        ),
        Download,
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        return super().__call__(args)
