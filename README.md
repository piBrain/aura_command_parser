# Aura Intent Parser

Snips-NLU is an recently open sourced library for parsing the intent and values from natural language.

E.g. "I want to walk with Tom", the intent is going for a walk and a value might be tom.

Snips operates on intents and entities as training data.
Intents are the actions that may be taken in a sentence and entities are the values you may want to extract for that.

You can read more about this **[here](http://snips-nlu.readthedocs.io/en/latest/)**

This microservice is a small wrapper for a Snips model trained on custom intents and entities.
You can find intents in /intents and entities in /entities.
Ultimately the model is deployed to an AWS lambda function that is further layered with an API Gateway stage.

The requirements for setting this up are as follows.

### Python
- Python >= 3.6 (Virtual Env Optional)
- aws-cli
- python-pip3 or just pip3
- snips_nlu

### NodeJS
- serverless (global install)
- serverless-python-requirements

## Set-up
I personally recommend creating a python virtualenv to set-up for this project. (and really any python project.) This however is optional.

For the python dependencies you may 'pip install -r requirements.txt' and for the node js dependencies you must first globally install
serverless with either 'npm install -g serverless' or 'yarn global add serverless' followed by 'npm install' or 'yarn install'.

**Any depdencies you add must be added to either the requirements.txt or the package.json**

## Adding Additional Intents or Entities
Both intents and entities are simply txt files with some special syntax. Use your favorite editor of choice and edit away.
The snips documentation for that syntax and intents/entities in general is located **[here.](http://snips-nlu.readthedocs.io/en/latest/data_model.html)**

After editing the intents or entities the dataset.json needs to be regenerated.

This is as simple as:

* generate-dataset --language en --intent-files ./intents/* --entity-files ./entities/* > dataset.json

## Retraining

To retrain the model simply run:

* python snips_trainer.py

## Deploying

Deploying will use serverless and the aws-cli to package and upload the required files to their respective AWS services.
This will result in an upload of the trained_engine.json that training produces to the microservice.files bucket and the
creation or update of whatever stage (i.e. prod, development) you chose.

To deploy run:

* ./deploy.sh (stage) or bash ./deploy.sh (stage)

Stages at the moment include:

- prod
- development

Be careful with this because if you mistype you will wind up deploying a new lambda function that is not attached to an api gateway.
If this happens no big deal, either kill the deployment before it finishes or go to aws and delete the lambda function.


### Have Fun!






