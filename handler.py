try:
  import unzip_requirements
except ImportError:
  pass
import json
import boto3
import os
from snips_nlu import load_resources, SnipsNLUEngine
def parse(event, content):
    s3 = boto3.resource('s3')
    obj = s3.Object(os.environ.get('RESOURCE_BUCKET'), 'trained_engine.json')
    load_resources('en')
    trained_model = json.load(obj.get().get('Body'))
    engine = SnipsNLUEngine.from_dict(trained_model)

    return engine.parse(event.get('statement'))
if(__name__=='__main__'):
    handler('','')
