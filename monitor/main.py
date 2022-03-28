import argparse
from online_state import online_state
from offline_state import offline_state

ONLINE = "online"
OFFLINE = "offline"

def print_explantion():
    """
    function prints some details about the monitor
    """
    explanation = """
    Hello User,
    You have two modes for operating the monitor: online and offline.
    In online mode:
        You enter a fixed number of seconds,
        Then non-stop for the same number of seconds the system will
        sample services on your computer, and save the samples and
        the changes that occur between samples in log files.
    In offline mode:
        Enter into the system two hours in which a sample has been sampled in the past,
        And you will be presented with an output describing a log between the two samples.

    So, what mode would you like to activate?
    Good luck!
    """
    print(explanation)
    
def get_monitor_mode():
    """
    function ask the user for monitor state and return the chosen state
    """
    monitor_state = None
    while monitor_state != ONLINE and monitor_state != OFFLINE:
        monitor_state = input("Enter the desired mode (online / offline): ").lower()
    return monitor_state


def main():
    # print some details
    print_explanation()

    monitor_mode = get_monitor_mode()
    




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
