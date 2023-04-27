#%%
import sys

sys.path.append(Path(__file__).parent)
from pathlib import Path
from utils import Translater

# python -m pip install --upgrade arxiv
import arxiv


class ArxivPaperFetcher:
    def __init__(self, id="2304.13714"):
        self.id = id

    def run(self):
        search = arxiv.Search(id_list=[self.id])
        self.paper = next(search.results())
        self.title = self.paper.title


class PaperAbstracter:
    def __init__(self, paper_obj):
        pass

    def translate(self):
        pass


if __name__ == "__main__":
    arxiv_paper_fetcher = ArxivPaperFetcher()
    arxiv_paper_fetcher.run()
    print(arxiv_paper_fetcher.title)
    translater = Translater(arxiv_paper_fetcher.title)
    translater.run()
    print(translater.translated_text)
