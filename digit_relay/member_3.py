from digit_relay.relay_base import run_member

# TODO Anggota 3: ganti kotak placeholder dengan bentuk digit 1
BOX = [[(0, 0), (1, 0), (1, 2), (0, 2), (0, 0)]]
DIGITS = {
    '3': [[(0, 2), (1, 2), (1, 0), (0, 0)], [(0.2, 1), (1, 1)]],
    '1': BOX,
}


def main():
    run_member(3, (0, 0, 0), (7.2, 7.8), DIGITS)
