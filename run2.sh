#!/bin/bash

set -e

PYTHONPATH=`pwd`/python python3 camera-ssd-threaded-2.py --usb --vid 1 --prototxt models/googlenet_fc/coco/SSD_300x300/deploy.prototxt --model models/googlenet_fc/coco/SSD_300x300/deploy.caffemodel --width 1280 --height 720


echo "** run SSD caffe successfully"
