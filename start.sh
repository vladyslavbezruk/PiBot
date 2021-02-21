#!/bin/bash

chmod +x sources/sh/update.sh
chmod +x sources/sh/createSource.sh

cd sources/sh/
./update.sh

cd ../py/

python3 main.py
