#!/usr/bin/env bash

export PATH=/export/home/<>/<>/python36/bin/:$PATH

python3 -m venv venv

. venv/bin/activate

pip install --upgrade --index-url=${ARTIFACTORY} pip

pip install --no-cache-dir --index-url=${ARTIFACTORY} -e .


if [ $? -ne 0 ]; then
	echo "FAILED TO PULL REPOS"
	exit 0
fi