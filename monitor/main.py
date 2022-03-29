from datetime import datetime
from online_state import online_state
from offline_state import offline_state

ONLINE = "online"
OFFLINE = "offline"

def print_explanation():
    """
    Function prints some details about the monitor.
    """
    explanation = """
*********************************************************************************************
*   Hello User,                                                                             * 
*   Welcome to our service monitor!                                                         *
*                                                                                           *
*   You have two modes for operating the monitor: ONLINE & OFFLINE.                         *
*   In ONLINE mode:                                                                         *
*       You will be asked to enter a fixed number of seconds (X),                           *
*       then for every X seconds the system will sample services on your computer,          *
*       and store the samples in service_list.txt file. Additionally, the changes that      *
*       occur between samples in log files would be presented                               *
*       by our software, and will be stored in status_log.txt file as well.                 *
*                                                                                           *
*   In OFFLINE mode:                                                                        *
*       Enter two hours in which a sample has been sampled in the past,                     *
*       And you will be presented with an output describing a log between the two samples.  *
*                                                                                           *
*    So, what mode would you rather to activate?                                            *
*    Good luck!                                                                             *
********************************************************************************************* 
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


def get_two_sample_times():
    """
    function return two times from user
    for the offline monitor state
    """
    time_1 = get_str_time(1)
    time_2 = get_str_time(2)
    return time_1, time_2


def main():
    # print some details
    print_explanation()
    while True:
        monitor_mode = get_monitor_mode()

        # open monitor in ONLINE mode
        if monitor_mode == ONLINE:
            seconds = get_time_at_seconds()
            online = online_state()
            try:
                online.main(seconds)
            except:
                pass

        # open monitor in OFFLINE mode
        else:
            time_1, time_2 = get_two_sample_times()
            offline = offline_state()
            offline.main(time_1, time_2)

        exit = input("Press E to exit, or any other key to continue\n").upper()
        if exit == 'E':
            break


if __name__ == '__main__':
    main()
