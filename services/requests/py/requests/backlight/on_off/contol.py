import os

from tools_lib.lib.os_platform.os_platform import OSPlatform


def backlight_control(sleep, cmd):
    # cmd = f"python3 $HOME/rpi_styra/services/main_backlight_on_off.py --{cmd}"
    cmd = f"python3 $HOME/rpi_styra/services/backlight/py/{cmd}.py"
    if OSPlatform.is_linux():
        os.system(cmd)
    print(f"cmd: {cmd}")
