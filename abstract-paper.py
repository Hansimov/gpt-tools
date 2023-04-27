import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)
from utils import init_os_envs

init_os_envs()


class ArxivPaperFetcher:
    def __init__(self, paper_id):
        pass

    def translate(self):
        pass


class PaperAbstracter:
    def __init__(self, paper_obj):
        pass

    def translate(self):
        pass
