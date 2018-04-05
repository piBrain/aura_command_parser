import json
from pprint import pprint
from snips_nlu import load_resources, SnipsNLUEngine

data = json.load(open('./dataset.json', 'r+'))
load_resources('en')

nlu_engine = SnipsNLUEngine(config=json.load(open('./config_en.json', 'r+')))
nlu_engine.fit(data)

with open('./trained_engine.json', 'w+') as f:
    f.write(json.dumps(nlu_engine.to_dict()))
