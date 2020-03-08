import os

from tools_lib.lib.os_platform.os_platform import OSPlatform


def energenie_control(sleep, cmd, socket):
    cmd = f"python3 $HOME/rpi_styra/services/energenie/py/{cmd}-{socket}.py"
    if OSPlatform.is_linux():
        os.system(cmd)
    print(f"cmd: {cmd}")
