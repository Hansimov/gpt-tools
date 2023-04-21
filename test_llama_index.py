#%%
"""
* llama_index/examples/paul_graham_essay
  * https://github.com/jerryjliu/llama_index/tree/main/examples/paul_graham_essay
"""
import os
import json
from pathlib import Path
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

with open(Path(__file__).parent / "secrets.json", "r") as rf:
    secrets = json.load(rf)
os.environ["OPENAI_API_KEY"] = secrets["openai_api_key"]

for proxy_env in ["http_proxy", "https_proxy"]:
    os.environ[proxy_env] = secrets["http_proxy"]

# data_filename = "./what_i_worked_on.txt"
index_filename = Path(__file__).parent / "index" / "what_i_worked_on_index.json"
documents = SimpleDirectoryReader("data").load_data()

overwrite_index = False
if not os.path.exists(index_filename) or overwrite_index:
    index = GPTSimpleVectorIndex.from_documents(documents)
    index.save_to_disk(index_filename)

new_index = GPTSimpleVectorIndex.load_from_disk(index_filename)

response = new_index.query("What did the author do growing up? 请用中文回答。")
print(response)
