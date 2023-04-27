#%%
import sys

sys.path.append(Path(__file__).parent)
from datetime import datetime
from pathlib import Path
from utils import Translater

# python -m pip install --upgrade arxiv
import arxiv


class ArxivPaper:
    def __init__(self, id):
        self.id = id
        self.run()

    def run(self):
        search = arxiv.Search(id_list=[self.id])
        res = next(search.results())

        self.title = res.title

        self.publish_date = res.published
        self.update_date = res.updated

        # self.arxiv_url = res.entry_id
        # self.pdf_url = res.pdf_url
        self.arxiv_url = f"https://arxiv.org/abs/{self.id}"
        self.pdf_url = f"https://arxiv.org/pdf/{self.id}"
        self.web_url = f"https://www.arxiv-vanity.com/papers/{self.id}"

        self.abstract = res.summary


class PaperAbstracter:
    def __init__(self, paper_id):
        self.id = paper_id

    def translate(self, original_text):
        translater = Translater(original_text)
        print(f"> Translating characters num: {len(original_text)}")
        translater.run()
        return translater.translated_text

    def run(self):
        paper = ArxivPaper(self.id)
        paper.run()

        title_zh = self.translate(paper.title).replace("。", "")
        abstract_zh = self.translate(paper.abstract)

        publish_date_str = str(paper.publish_date)[:10]
        update_date_str = str(paper.update_date)[:10]
        publish_update_str = f"{publish_date_str}提交"
        if paper.publish_date != paper.update_date:
            publish_update_str += f"，{update_date_str}更新"
        today_str = str(datetime.now())[:10]

        sharing_text = (
            f"\n"
            f"【论文分享】{title_zh}\n"
            f"{paper.title}\n"
            f"\n"
            f"* [{self.id}]: {publish_update_str}，{today_str}分享\n"
            f"* arXiv: {paper.arxiv_url}\n"
            f"* PDF: {paper.pdf_url}\n"
            f"* Web: {paper.web_url}\n"
            f"\n"
            f"【摘要】\n{abstract_zh}\n"
            f"\n"
        )
        print(sharing_text)


if __name__ == "__main__":
    paper_id = "2206.10305"
    paper_id = "2304.13712"
    paper_abstracter = PaperAbstracter(paper_id)
    paper_abstracter.run()
