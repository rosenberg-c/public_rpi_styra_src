import platform


class OSPlatform:
    @staticmethod
    def is_windows():
        if platform.system().lower() == "windows":
            return True
        return False

    @staticmethod
    def is_mac():
        if platform.system().lower() == "darwin":
            return True
        return False

    @staticmethod
    def is_linux():
        if platform.system().lower() == "linux":
            return True
        return False
