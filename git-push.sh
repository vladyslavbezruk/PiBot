#!/bin/bash

cd ../../

git add *.sh 
git add *.py 
git add *.log 
git add *.json
git commit -m "Updated"
git push

cd sources/py/
