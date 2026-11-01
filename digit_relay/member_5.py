from digit_relay.relay_base import run_member

# TODO Anggota 5: ganti kotak placeholder dengan bentuk digit 5, 1, 3
BOX = [[(0, 0), (1, 0), (1, 2), (0, 2), (0, 0)]]
DIGITS = {'5': BOX, '1': BOX, '3': BOX}


def main():
    run_member(5, (255, 255, 255), (4.0, 4.5), DIGITS)
