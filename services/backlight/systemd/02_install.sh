#!/usr/bin/env bash

# mkdir -p $HOME/.local/share/systemd/user
# nano $HOME/.local/share/systemd/user/pir.service

sudo systemctl enable pir.service
sudo systemctl start pir.service

sudo systemctl enable backlight.service
sudo systemctl start backlight.service
