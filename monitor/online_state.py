import sys
from threading import Thread
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
    pass

def win_get_sample(time_at_seconds):
    """
    function get sample every time_at_seconds
    and sent it to write into service_list.
    and than, insert it to Queue for logs file.
    """
    pass
    

def main(time_at_seconds):
    
    # check witch type of sample to take
    if WINDOWS in sys.platform:
         thread = Thread(target=win_get_sample, args=(time_at_seconds,))
            thread.start()
    else:
        pass
