from digit_relay.relay_base import run_member

# TODO Anggota 8: ganti kotak placeholder dengan bentuk digit 8, 1, 6
BOX = [[(0, 0), (1, 0), (1, 2), (0, 2), (0, 0)]]
DIGITS = {'8': BOX, '1': BOX, '6': BOX}


def main():
    run_member(8, (255, 165, 0), (5.6, 1.2), DIGITS)
