#!/bin/bash

chmod +x update.sh
chmod +x createSource.sh

./update.sh

python3 /sources/py/main.py
