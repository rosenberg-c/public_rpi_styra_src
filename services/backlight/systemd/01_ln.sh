#!/usr/bin/env bash


MPATHProfile="/home/pi/rpi_styra/services/backlight"

# control
sudo ln -s ${MPATHProfile}/systemd/backlight.service /etc/systemd/system

# pir
sudo ln -s ${MPATHProfile}/systemd/pir.service /etc/systemd/system

# sudo rm /etc/systemd/system/