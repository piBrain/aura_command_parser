import json
from snips_nlu import load_resources, SnipsNLUEngine
def handler(event, content):
    load_resources('en')
    trained_model = json.loads(open('./trained_engine.json', 'r+'))
    engine = SnipsNLUEngine.from_dict(trained_model)

    return engine.parse(event.get('statement'))

