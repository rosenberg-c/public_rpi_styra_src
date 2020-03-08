#!/usr/bin/env bash

# ./flip_backlight.sh

B_PATH="/sys/class/backlight/soc:backlight/brightness"

sudo sh -c "echo 1 > ${B_PATH}"
