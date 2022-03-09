from datasets import Dataset
import json
import gdown

url = 'https://drive.google.com/uc?id=1sAgDtEj-UjJECfTF6xfiWFk7lrTX7yoV'
filename = "articles_1000.json"
gdown.download(url, filename, quiet=False)
with open(filename, 'r') as f:
    data = json.load(f)
dataset = Dataset.from_dict(data)
