from datetime import datetime
from online_state import online_state
from offline_state import offline_state

ONLINE = "online"
OFFLINE = "offline"

def print_explanation():
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


def get_time_at_seconds():
    """
    function return a integer number of seconds from user
    """
    seconds = ''
    while not seconds.isnumeric():
        seconds = input("Enter number of seconds: ")

    return int(seconds)


def get_str_time(sample_num):
    """
    function ask the user for time,
    and return the time when is valid.
    """
    str_time = ''
    is_valid = False

    while not is_valid:
        str_time = input(f"Please enter sample {sample_num} time (DD-MM-YYYY-hh:mm:ss): ")
        try:
            datetime.strptime(str_time, "%d-%m-%Y-%H:%M:%S")
            is_valid = True
        except:
            print("Invalid date format, please try again.")

    return str_time


def main():
    # print some details
    print_explanation()

    monitor_mode = get_monitor_mode()
    
    # open monitor in ONLINE mode
    if monitor_mode == ONLINE:
        seconds = get_time_at_seconds()
        online = online_state()
        online.main(seconds)

    # open monitor in OFFLINE mode
    else:
        time_1, time_2 = get_two_sample_times()
        offline = offline_state()
        offline.main(time_1, time_2)


if __name__ == '__main__':
    main()
