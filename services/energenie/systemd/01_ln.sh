#!/usr/bin/env bash


MPATHProfile="/home/pi/rpi_styra/services/energenie"

# control
sudo ln -s ${MPATHProfile}/systemd/energenie.service /etc/systemd/system

# sudo rm /etc/systemd/system/