from digit_relay.relay_base import run_member

# TODO Anggota 4: ganti kotak placeholder dengan bentuk digit 4, 1, 2
BOX = [[(0, 0), (1, 0), (1, 2), (0, 2), (0, 0)]]
DIGITS = {'4': BOX, '1': BOX, '2': BOX}


def main():
    run_member(4, (255, 255, 0), (0.8, 4.5), DIGITS)
