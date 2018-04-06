#!/bin/bash
aws s3 cp trained_engine.json s3://microservice.files
serverless deploy --stage $1
