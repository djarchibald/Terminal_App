#!/bin/bash
if [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it does not seem to be installed.
    To install Python, check out https://installpython3.com/ and try again.' >&2
  exit 1
else
python3 -m venv .venv
source /venv/bin/activate
from os import system
from datetime import date
import time
python3 main.py 
fi

