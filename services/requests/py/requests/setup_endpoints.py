from requests.backlight.config.backlight_config_get import endpoint_backlight_config_get
from requests.backlight.config.backlight_config_post import endpoint_backlight_config_post
from requests.backlight.config.backlight_config_restart import endpoint_backlight_restart_service
from requests.backlight.on_off.backlight_off import endpoint_backlight_off
from requests.backlight.on_off.backlight_on import endpoint_backlight_on
from requests.device_control.device_control_reboot import endpoint_reboot
from requests.device_control.device_control_shutdown import endpoint_shutdown

from flask import Flask

from requests.energenie.config.energenie_config_get import endpoint_energenie_config_get
from requests.energenie.config.energenie_config_post import endpoint_energenie_config_post
from requests.energenie.config.energenie_config_restart import endpoint_energenie_restart_service
from requests.energenie.on_off.energenie_off import endpoint_energenie_off
from requests.energenie.on_off.energenie_on import endpoint_energenie_on
from requests.utils.online.utils_online import endpoint_online
from requests.utils.ram.utils_ram import endpoint_ram
from requests.utils.temp.utils_temp import endpoint_temp
from requests.utils.uptime.utils_uptime import endpoint_upptime


def setup_enpoints(app: Flask, config_dir):
    endpoint_online(app)

    # other
    endpoint_upptime(app)
    endpoint_ram(app)
    endpoint_temp(app)

    # backlight
    endpoint_backlight_config_get(app, config_dir)
    endpoint_backlight_config_post(app, config_dir)
    endpoint_backlight_restart_service(app)

    endpoint_backlight_on(app)
    endpoint_backlight_off(app)

    # backlight
    endpoint_energenie_config_get(app, config_dir)
    endpoint_energenie_config_post(app, config_dir)
    endpoint_energenie_restart_service(app)

    endpoint_energenie_on(app)
    endpoint_energenie_off(app)

    # Device Control
    endpoint_reboot(app)
    endpoint_shutdown(app)
