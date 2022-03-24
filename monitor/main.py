import argparse
from online_state import online_state
from offline_state import offline_state

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Monitor')
    parser.add_argument('time_at_seconds', help='render time in seconds')
    parser.add_argument('state', help='state for online/offline')
    args = parser.parse_args()

    if args.state == "online":
        online = online_state()
        online.main(int(args.time_at_seconds))

    elif args.state == "offline":
        sample_time = input("Enter a sample time: ")
        sample_2_time = input("Enter a second sample time: ")
        offline = offline_state()
        offline.main(sample_time, sample_2_time)

    else:
        print("Invalid argument")
