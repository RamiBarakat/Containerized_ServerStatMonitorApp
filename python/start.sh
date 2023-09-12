#!/bin/bash

python -m unittest testread.py
python -m unittest testapi.py

python3 apis.py
