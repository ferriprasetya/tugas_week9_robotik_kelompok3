from digit_relay.relay_base import run_member

DIGITS = {
    '1': [[(0.2, 1.6), (0.5, 2), (0.5, 0)], [(0.2, 0), (0.8, 0)]],
    '9': [[(1, 1), (0, 1), (0, 2), (1, 2), (1, 0), (0, 0)]],
}


def main():
    run_member(1, (255, 0, 0), (0.8, 7.8), DIGITS)
