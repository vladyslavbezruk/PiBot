#!/bin/bash

chmod +x sources/sh/update.sh
chmod +x sources/sh/createSource.sh

cd sources/sh/
./update.sh

cd ../../resources/json/
cp *.json ../../sources/py/

#cp resources/json/*.json sources/py/

cd ../../sources/py/

python3 main.py
