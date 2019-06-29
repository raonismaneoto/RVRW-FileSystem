#!/bin/bash
restart=$1

if [ "$restart" == "-r" ]; then
	rm -rf disk
	python setup.py
fi

python user_api.py
