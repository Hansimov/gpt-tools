import os
import json
from pathlib import Path

# python -m pip install --upgrade openai
import openai


def init_os_envs():
    with open(Path(__file__).parent / "secrets.json", "r") as rf:
        secrets = json.load(rf)
    os.environ["OPENAI_API_KEY"] = secrets["openai_api_key"]

    for proxy_env in ["http_proxy", "https_proxy"]:
        os.environ[proxy_env] = secrets["http_proxy"]


init_os_envs()
openai.api_key = os.environ["OPENAI_API_KEY"]


class Translater:
    def __init__(self) -> None:
        pass

    def run(self):
        MODEL = "gpt-3.5-turbo"
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Knock knock."},
                {"role": "assistant", "content": "Who's there?"},
                {"role": "user", "content": "Orange."},
            ],
            temperature=0,
        )
        print(response)


translater = Translater()
translater.run()
