class Commands:
    hdmi_keep_on = 'echo -e ' + '\'\\033[9;0]\'' + ' >> /dev/tty1'
    switch_to_tty3 = 'chvt 3'
    clear = 'clear'

    screen_on_off = 'tvservice -o'

    get_hardware_temp = 'cat /sys/class/thermal/thermal_zone0/temp'

    wlan_signal = 'iwconfig wlan0'
    grep_wlan_signal = 'grep -i signal'
