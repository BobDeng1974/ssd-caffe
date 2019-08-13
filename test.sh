#!/bin/bash

set -e

# NOTE: runtest fails on Jetson Nano due to out of memory
# make runtest

./build/tools/caffe time --gpu 0 --model ./models/bvlc_alexnet/deploy.prototxt

PYTHONPATH=`pwd`/python python3 -c "import caffe; print('caffe version: %s' % caffe.__version__)"

echo "** Build and test SSD caffe successfully"
