import sys
import time
import sample_unit
from comparator import comparator


class online_state:
    def __init__(self):
        self.queue = []
        self.WINDOWS = "win"

    def write_to_logs(self, sample_q1, sample_q2):
        """
        sends the Queue (with 2 samples!)
        to the comparison unit.
        after get the log - insert it to
        'status_log.txt'
        """
        compare = comparator(sample_q1, sample_q2)
        compare.compare(sample_q1, sample_q2)


    def write_to_service_list(self, sample):
        """
        function get sample and insert it
        to the 'service_list.txt'
        """
        with open("service_list.txt", "a") as f:
            for name, status in sample:
                current_time = time.ctime().replace(' ', '-')
                # print(f"{current_time} {name} {status}")
                f.write(f"{current_time} {name} {status}\n")

    def get_sample(self, get_sample_by_os, time_at_seconds):
        """
        function get sample every time_at_seconds
        and sent it to write into service_list.
        and then, insert it to Queue for logs file.
        """
        while True:
            sample = get_sample_by_os()
            self.write_to_service_list(sample)

            # insert sample into Queue for comparison
            if len(self.queue) == 2:
                self.queue.pop()
                self.queue.insert(0, sample)
                self.write_to_logs(self.queue[0], self.queue[1])

            elif len(self.queue) == 1:
                self.queue.insert(0, sample)

            time.sleep(time_at_seconds)

    def main(self, time_at_seconds):
        # check witch type of sample to take.
        # for windows
        if self.WINDOWS in sys.platform:
            self.get_sample(sample_unit.win_sample, time_at_seconds)

        # for linux
        else:
            self.get_sample(sample_unit.linux_sample, time_at_seconds)
