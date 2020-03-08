from lib.energenie import cleanup_socket, setup_energenie, \
    socket_one_on, socket_one_off, socket_two_on, socket_two_off, socket_three_on, socket_four_on, socket_three_off, \
    socket_four_off


def run_on_script(socket):
    setup_energenie()

    if socket == 1:
        socket_one_on()

    if socket == 2:
        socket_two_on()

    if socket == 3:
        socket_three_on()

    if socket == 4:
        socket_four_on()

    cleanup_socket()


def run_off_script(socket):
    setup_energenie()

    if socket == 1:
        socket_one_off()

    if socket == 2:
        socket_two_off()

    if socket == 3:
        socket_three_off()

    if socket == 4:
        socket_four_off()

    cleanup_socket()
