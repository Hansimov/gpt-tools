#%%
import os

os.environ["OPENAI_API_KEY"] = "<OPENAI_API_KEY>"
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

data_filename = "./what_i_worked_on.txt"
index_filename = "./index_what_i_worked_on.json"
documents = SimpleDirectoryReader("data").load_data()

# Modify paths of `vocab_bpe` and `encoder_json` in following location:
#   [C:\Python39\lib\site-packages\tiktoken_ext\openai_public.py]: Line 12-13
if not os.path.exists(index_filename):
    index = GPTSimpleVectorIndex.from_documents(documents)
    index.save_to_disk(index_filename)
else:
    index = GPTSimpleVectorIndex.load_from_disk(index_filename)

response = index.query("What did the author do growing up?")
print(response)
