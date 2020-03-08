from requests.energenie.config.get_request_config import convert_dict_to_class


def validate(_json):
    try:
        _ = convert_dict_to_class(_json)
        return True
    except KeyError:
        print("KeyError")
        return False
