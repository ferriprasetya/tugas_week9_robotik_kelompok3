from digit_relay.relay_base import run_member

# TODO Anggota 6: ganti kotak placeholder dengan bentuk digit 6, 1, 4
BOX = [[(0, 0), (1, 0), (1, 2), (0, 2), (0, 0)]]
DIGITS = {'6': BOX, '1': BOX, '4': BOX}


def main():
    run_member(6, (0, 255, 255), (7.2, 4.5), DIGITS)
