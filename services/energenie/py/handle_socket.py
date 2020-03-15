

class HandleSocket:
    def __init__(self, on=None, off=None):
        self.on = on
        self.off = off

    def handle_socket(self, auto_on: bool, auto_off: bool):
        if auto_on:
            self.on(1)
        if auto_off:
            self.off(1)
