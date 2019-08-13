#!/bin/bash

set -e

PYTHONPATH=`pwd`/python python3 camera-ssd-threaded.py --usb --vid 1 --prototxt models/bvlc_googlenet/deploy.prototxt --model models/bvlc_googlenet/bvlc_googlenet.caffemodel --width 1280 --height 720


echo "** run SSD caffe successfully"
