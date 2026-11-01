from digit_relay.relay_base import run_member

# TODO Anggota 6: ganti kotak placeholder dengan bentuk digit 6, 1, 4
DIGITS = {
    '6': [[(1, 2), (0, 2), (0, 0), (1, 0), (1, 1), (0, 1)]],
    '1': [[(0.2, 1.6), (0.5, 2), (0.5, 0)], [(0.2, 0), (0.8, 0)]],
    '4': [[(0, 2), (0, 1), (1, 1)], [(1, 2), (1, 0)]],
}


def main():
    run_member(6, (0, 255, 255), (7.2, 4.5), DIGITS)
