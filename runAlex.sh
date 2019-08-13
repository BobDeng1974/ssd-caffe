#!/bin/bash

set -e

PYTHONPATH=`pwd`/python python3 camera-ssd-threaded.py --usb --vid 1 --prototxt models/bvlc_alexnet/deploy.prototxt --model models/bvlc_alexnet/bvlc_alexnet.caffemodel --width 1280 --height 720


echo "** run SSD caffe successfully"
