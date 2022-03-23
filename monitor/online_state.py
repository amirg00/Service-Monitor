import sys
import time
import sample_unit

WINDOWS = "win"

Queue = []


def write_to_logs():
    """
    sent the Queue (with 2 samples!)
    to the comparation unit.
    after get the log - insert it to 
    'status_log.txt'
    """
    pass


def write_to_service_list(sample):
    """
    function get sample and insert it
    to the 'service_list.txt'
    """
    with open("service_list.txt", "a") as f:
        for name, status in sample:
            current_time = time.ctime().replace(' ', '-')
            print(f"{current_time} {name} {status}")
            f.write(f"{current_time} {name} {status}\n")


def get_sample(get_sample_by_os, time_at_seconds):
    """
    function get sample every time_at_seconds
    and sent it to write into service_list.
    and than, insert it to Queue for logs file.
    """
    while True:
        sample = get_sample_by_os()
        write_to_service_list(sample)

        # insert sample into Queue for comparation
        if len(Queue) == 2:
            Queue.pop()
        Queue.insert(0, sample)

        write_to_logs()

        time.sleep(time_at_seconds)


def main(time_at_seconds):
    # check witch type of sample to take.
    # for windows
    if WINDOWS in sys.platform:
        get_sample(sample_unit.win_sample, time_at_seconds)

    # for linux
    else:
        get_sample(sample_unit.linux_sample, time_at_seconds)

main(5)
