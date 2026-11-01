from digit_relay.relay_base import run_member

# TODO Anggota 2: ganti kotak placeholder dengan bentuk digit 2, 1, 0
BOX = [[(0, 0), (1, 0), (1, 2), (0, 2), (0, 0)]]
DIGITS = {'2': BOX, '1': BOX, '0': BOX}


def main():
    run_member(2, (0, 255, 0), (4.0, 7.8), DIGITS)
