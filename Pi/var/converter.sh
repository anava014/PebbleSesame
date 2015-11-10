#!/bin/bash

echo "Converting Image...";
convert currentPicture.jpg \
  -adaptive-resize '144x168>' \
  -fill '#FFFFFF00' -opaque none \
  -type Grayscale -colorspace Gray \
  -colors 2 -depth 1 \
  -define png:compression-level=9 -define png:compression-strategy=0 \
  -define png:exclude-chunk=all \
  currentPicture.png
