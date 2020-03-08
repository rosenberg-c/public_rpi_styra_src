#!/usr/bin/env bash
# sudo sh -c 'echo 1 > /sys/class/backlight/soc\:backlight/brightness'

B_PATH="/sys/class/backlight/soc:backlight/brightness"
B_STATUS=$(cat ${B_PATH})

if [[ ${B_STATUS} = "0" ]]; then
   echo "TURN BACKLIGHT ON"
   sudo sh -c "echo 1 > ${B_PATH}"
else
   echo "TURN BACKLIGHT OFF"
   sudo sh -c "echo 0 > ${B_PATH}"
fi
