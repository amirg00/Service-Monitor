import argparse
from online_state import online_state

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Monitor')
    parser.add_argument('time_at_seconds', help='render time in seconds')
    args = parser.parse_args()
    online = online_state()
    online.main(int(args.time_at_seconds))
