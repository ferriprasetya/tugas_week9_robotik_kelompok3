from digit_relay.relay_base import run_member

# TODO Anggota 7: ganti kotak placeholder dengan bentuk digit 7, 1, 5
BOX = [[(0, 0), (1, 0), (1, 2), (0, 2), (0, 0)]]
DIGITS = {'7': BOX, '1': BOX, '5': BOX}


def main():
    run_member(7, (255, 0, 255), (2.4, 1.2), DIGITS)
