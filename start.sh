#!/bin/bash

export PYTHONPATH="$PYTHONPATH:/home/orangepi/PiBot/"

chmod +x sources/sh/createSource.sh

chmod +x sources/sh/removeSource.sh

cd sources/py/

python3.9 main.py

