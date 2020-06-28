#!/bin/bash
set -e

CWD=$(cd $(dirname $0);pwd)
cd "${CWD}/../tables"
EXISTING_TABLES=`aws dynamodb list-tables --endpoint-url=http://localhost:8000 | jq -r ".TableNames[]"`
echo $EXISTING_TABLES

for file in `find . -type f -name "*.json" -maxdepth 1 -execdir basename '{}' ';'`; do
  table=`echo $file | sed s/.json//`
  if [[ $EXISTING_TABLES == *${table}* ]]; then
    echo "${table} is already exists."
  else
    aws dynamodb create-table --cli-input-json file://${file}  --endpoint-url http://localhost:8000
  fi
done
