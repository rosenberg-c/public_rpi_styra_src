# Energenie

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
Othervise you need to use a 2.4G connection.

---

un mount disk
`diskutil umountDisk /dev/disk2`


## First boot
### ssh
ssh pi@192.168.#.#


### Change password
`passwd`


### set timezone
`timedatectl set-timezone Europe/Stockholm`
### Update Os

---

```
sudo apt-get update -y &&
sudo apt-get upgrade -y &&
sudo apt autoremove -y

```

