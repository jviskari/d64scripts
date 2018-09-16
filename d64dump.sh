#!/bin/bash
# Copy from OpenCBM device to disk image

cbmctrl reset
DEVNO=$(cbmctrl detect | cut -c2)


TS=$(date "+%y%m%d%H%M%S")
VOLUME=$(cbmctrl dir $DEVNO | head -1 | cut -d "\"" -f2 | sed -e 's/ /_/g')
FILENAME="$TS"_"$VOLUME.d64"


d64copy -v $DEVNO $FILENAME

