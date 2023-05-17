#%%
import sys
from pathlib import Path

sys.path.append(Path(__file__).parent)
from datetime import datetime
from utils import Translater, date_duration

# python -m pip install --upgrade arxiv
import arxiv
import argparse


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

        title_zh = self.translate(paper.title)
        for ch in ["。", "《", "》"]:
            title_zh = title_zh.replace(ch, "")
        abstract_zh = self.translate(paper.abstract).replace("。", "。\n")

        publish_date_str = str(paper.publish_date)[:10]
        update_date_str = str(paper.update_date)[:10]

        today_str = str(datetime.now())[:10]
        publish_duration_str = date_duration(publish_date_str)[1]
        update_duration_str = date_duration(update_date_str)[1]

        publish_update_str = f"提交于{publish_date_str}（{publish_duration_str}）"
        if paper.publish_date != paper.update_date:
            publish_update_str += f"，更新于{update_date_str}（{update_duration_str}）"

        sharing_text = (
            f"\n"
            f"【论文分享】{title_zh}\n"
            f"\n"
            f"{paper.title}\n"
            f"* [{self.id}]: {publish_update_str}\n"
            f"\n"
            f"【摘要】\n{abstract_zh}\n"
            f"* arXiv: {paper.arxiv_url}\n"
            f"* PDF: {paper.pdf_url}\n"
            f"* Web: {paper.web_url}\n"
            f"* Hots: \n"
            f"\n"
        )
        print(sharing_text)


class ArgParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        super(ArgParser, self).__init__(*args, **kwargs)
        self.add_argument("-i", "--paper-id", type=str, help="arXiv paper ID")
        self.args = self.parse_args(sys.argv[1:])


if __name__ == "__main__":
    arg_parser = ArgParser()
    args = arg_parser.args
    paper_id = "2304.12210" if args.paper_id is None else args.paper_id
    paper_abstracter = PaperAbstracter(paper_id)
    paper_abstracter.run()
