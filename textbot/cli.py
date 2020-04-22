from spacy.cli import download
import argparse
import plac

def download_language():
# Create dictionary for command
    command = {
        "English": "en_core_web_sm",
        "German": "de_core_news_sm",
        "French": "fr_core_news_sm",
        "Spanish": "es_core_news_sm",
        "Multi-language": "xx_ent_wiki_sm",
    }

    # Create the parser
    my_parser = argparse.ArgumentParser(
        prog="download dictionary",
        description="Download the dictionary of language that you want",
    )

    # Add the arguments
    my_parser.add_argument(
        "-language",
        metavar="Language",
        type=str,
        help="Language that you want",
        default="English",
        choices=["English", "German", "French", "Spanish", "Multi-language"],
    )

    # Execute the parse_args() method
    args = my_parser.parse_args()
    language = command[args.language]

    # Download
    plac.call(download, [language])
