#!/usr/bin/env bash

export PATH=$PATH:$(pwd)
rm -rf ./venv
pip3 install --upgrade pip
python3 -m venv venv
source ./venv/bin/activate
pip3 install .