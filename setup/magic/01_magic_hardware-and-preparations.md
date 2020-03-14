# Magic
## Get hardware
### Parts
-  Raspberry pi
-  Sd card
-  hdmi cable
-  usb panel power with converter
-  other
-  Wooden box 
-  5" or 7" hdmi

## Install Raspbian with desktop
Time of writing 2020-02-05 kernel 4.19

### dd
diskutil list
diskutil umountDisk /dev/disk#
sudo dd bs=1m if=/path of=/path conv=sync

### Prepare sd

copy `/rpi-files/ssh` to `/boot/ssh` to enable ssh

---

copy `/rpi-files/wpa_supplicant.conf` to `/boot/wpa_supplicant.conf`

Change `SSID` and `PASSWORD` to match your home wifi. 
If you are using a rpi 3 b+ and above then you can use a 5G wifi connection.
Otherwise you need to use a 2.4G connection.

---

Add 
```
hdmi_force_hotplug=1
hdmi_group=2
hdmi_mode=87
hdmi_cvt=800 480 60 6 0 0 0
```
to end of file `/boot/config.txt`

---

Add this to config if you have lines around your screen
`hdmi_drive=1`

---

un mount disk
`diskutil umountDisk /dev/disk2`


## First boot
### ssh
ssh pi@192.168.#.#

### Remove from host file if security warning
ssh-keygen -R 192.168.#.#


### Change password
`passwd`

### Update Os

---

```
sudo apt-get update -y &&
sudo apt-get upgrade -y &&
sudo apt autoremove -y

```

### set timezone
`timedatectl set-timezone Europe/Stockholm`

### disable removable media dialog
if you plug a phone or similar into the usb port a invasive dialog pops up asking about what to do..
This disables that dialog after reboot

sudo nano /etc/xdg/pcmanfm/LXDE-pi/pcmanfm.conf
[volume]
autorun=0

## Disable screen-saver

`sudo nano /etc/lightdm/lightdm.conf`

hit `ctrl + w` 
and write `xserver-command=X` hit enter
change the line `#xserver-command=X` to `xserver-command=X -s 0 -dpms`

---
