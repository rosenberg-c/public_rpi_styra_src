#!/usr/bin/env bash

MPATHProfile="/home/pi/rpi_styra/services/requests"

sudo ln -s ${MPATHProfile}/systemd/request.service /etc/systemd/system

# sudo rm /etc/systemd/system/