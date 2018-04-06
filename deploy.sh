#!/bin/bash
generate-dataset --language en --intent-files ./intents/* --entity-files ./entities/* > dataset.json
python3 snips_trainer.py
mkdir ./deploy
cp ./trained_engine.json ./deploy
cp ./config_en.json ./deploy
cp ./lambda_function.py ./deploy
cp -r $1/* ./deploy
pushd ./deploy
zip -r command_parsing.zip ./*
popd
cp ./deploy/command_parsing.zip .
aws s3 cp command_parsing.zip s3://microservice.files
