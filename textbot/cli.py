from spacy.cli import downlaod
import plac
import sys
from bddcli import Given, when, stdout, status, stderr, Application, given


def download_language(input):
# Create dictionary for command
    command = {
        "English": "en_core_web_sm",
        "German": "de_core_news_sm",
        "French": "fr_core_news_sm",
        "Spanish": "es_core_news_sm",
        "Multi-language": "xx_ent_wiki_sm",
    }


    language = command[input]

    # Download
    plac.call(download, [language])

if __name__ == '__main__':

    download(["en_core_web_sm"])
