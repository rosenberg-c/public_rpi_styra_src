from requests.utils.temp.commands import Commands
from tools_lib.lib.user_sys.sub_com import sub_com


class Temperature:

    def __init__(self):
        pass

    def return_temp(self) -> str:
        raw_temp = sub_com(command=Commands.get_hardware_temp)

        if raw_temp is None:
            return "none"

        return str(int(raw_temp) / 1000)
