from digit_relay.relay_base import run_member

DIGITS = {
    '3': [[(0, 2), (1, 2), (1, 0), (0, 0)], [(0.2, 1), (1, 1)]],
    '1': [[(0.2, 1.6), (0.5, 2), (0.5, 0)], [(0.2, 0), (0.8, 0)]],
}


def main():
    run_member(3, (0, 0, 0), (7.2, 7.8), DIGITS)
