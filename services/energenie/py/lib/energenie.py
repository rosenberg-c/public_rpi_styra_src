# import the required modules
import time

import RPi.GPIO as GPIO


def send_socket():
    # let it settle, encoder requires this
    time.sleep(0.1)
    # Enable the modulator
    GPIO.output(22, True)
    # keep enabled for a period
    #time.sleep(0.25)
    time.sleep(0.85)
    # Disable the modulator
    GPIO.output(22, False)


def socket_all_on():
    print("sending code 1011 ALL on")
    GPIO.output(11, True)  # D0
    GPIO.output(15, True)  # D1
    GPIO.output(16, False)  # D2
    GPIO.output(13, True)  # D3
    send_socket()


def socket_all_off():
    print("sending code 1011 ALL on")
    GPIO.output(11, True)  # D0
    GPIO.output(15, True)  # D1
    GPIO.output(16, False)  # D2
    GPIO.output(13, False)  # D3
    send_socket()


def socket_one_on():
    print("sending code 1111 socket 1 on")
    GPIO.output(11, True)  # D0
    GPIO.output(15, True)  # D1
    GPIO.output(16, True)  # D2
    GPIO.output(13, True)  # D3
    send_socket()


def socket_one_off():
    print("sending code 0111 Socket 1 off")
    GPIO.output(11, True)  # D0
    GPIO.output(15, True)  # D1
    GPIO.output(16, True)  # D2
    GPIO.output(13, False)  # D3
    send_socket()


def socket_two_on():
    print("sending code 1110 socket 2 on")
    GPIO.output(11, False)  # D0
    GPIO.output(15, True)  # D1
    GPIO.output(16, True)  # D2
    GPIO.output(13, True)  # D3
    send_socket()


def socket_two_off():
    print("sending code 0110 socket 2 off")
    GPIO.output(11, False)  # D0
    GPIO.output(15, True)  # D1
    GPIO.output(16, True)  # D2
    GPIO.output(13, False)  # D3
    send_socket()


def socket_three_on():
    print("sending code 1110 socket 2 on")
    GPIO.output(11, True)  # D0
    GPIO.output(15, False)  # D1
    GPIO.output(16, True)  # D2
    GPIO.output(13, True)  # D3
    send_socket()


def socket_three_off():
    print("sending code 0110 socket 2 off")
    GPIO.output(11, True)  # D0
    GPIO.output(15, False)  # D1
    GPIO.output(16, True)  # D2
    GPIO.output(13, False)  # D3
    send_socket()


def socket_four_on():
    print("sending code 1110 socket 2 on")
    GPIO.output(11, False)  # D0
    GPIO.output(15, False)  # D1
    GPIO.output(16, True)  # D2
    GPIO.output(13, True)  # D3
    send_socket()


def socket_four_off():
    print("sending code 0110 socket 2 off")
    GPIO.output(11, False)  # D0
    GPIO.output(15, False)  # D1
    GPIO.output(16, True)  # D2
    GPIO.output(13, False)  # D3
    send_socket()


def setup_energenie():
    # set the pins numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    # Select the signal to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)

    # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)

    # Disable the modulator by setting CE pin lo
    GPIO.output(22, False)

    # Set the modulator to ASK for On Off Keying
    # by setting MODSEL pin lo
    GPIO.output(18, False)

    # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(16, False)
    GPIO.output(13, False)

    # The On/Off code pairs correspond to the hand controller codes.
    # True = '1', False ='0'


def cleanup_socket():
    GPIO.cleanup()
