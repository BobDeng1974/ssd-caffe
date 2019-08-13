#!/bin/bash

set -e

PYTHONPATH=`pwd`/python python3 camera-ssd-threaded.py --usb --vid 1 --prototxt models/VGGNet/VOC0712/SSD_300x300/deploy.prototxt --model models/VGGNet/VOC0712/SSD_300x300/VGG_VOC0712_SSD_300x300_iter_120000.caffemodel --width 1280 --height 720
#PYTHONPATH=`pwd`/python python3 ./examples/ssd/ssd_pascal_webcam.py 

echo "** run SSD caffe successfully"
