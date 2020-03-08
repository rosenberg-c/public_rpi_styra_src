from typing import Optional

from tools_lib.lib.user_sys.sub_com import sub_com


class GetRamStatusRpi:
    def __init__(self):
        pass

    def ret_info(self) -> dict:
        raw_info = self._get_raw_info()
        calc_info = self._calc_ram_memory(raw_info)

        return {
            "ram_total": calc_info[0],
            "ram_used": calc_info[1],
            "ram_free": calc_info[2],
            "ram_shared": calc_info[3],
            "ram_buff": calc_info[4],
            "ram_available": calc_info[5],
        }

    def _get_raw_info(self) -> Optional[str]:  # pragma: no cover
        input_sub = sub_com(command='free')
        response = sub_com(command='grep -i Mem', input_pipe=input_sub)
        return response

    def _calc_ram_memory(self, response) -> (str, str, str):
        """command = 'free | grep -i Mem'"""
        # total, used, free, shared, buff/cache, available
        zero_return = '0', '0', '0', '0', '0', '0'
        if response is False:
            return zero_return

        try:
            response = response.replace('\n', '').split()
            r_tot, r_used, r_free, r_shared, r_buff, r_available = response[1], response[2], response[3], response[4], \
                                                                   response[5], response[6]
        except (IndexError, AttributeError):  # pragma: no cover
            return zero_return
        r_tot = int(r_tot) / 1000
        r_used = int(r_used) / 1000
        r_free = int(r_free) / 1000
        r_shared = int(r_shared) / 1000
        r_buff = int(r_buff) / 1000
        r_available = int(r_available) / 1000

        ram_total = str(r_tot) + ' MB'
        ram_used = str(r_used) + ' MB'
        ram_free = str(r_free) + ' MB'
        ram_shared = str(r_shared) + ' MB'
        ram_buff = str(r_buff) + ' MB'
        ram_available = str(r_available) + ' MB'

        return ram_total, ram_used, ram_free, ram_shared, ram_buff, ram_available
