import sys
from datetime import datetime
import sample_unit
from comparator import comparator
import time


class online_state:
    def __init__(self):
        self.queue = []
        self.WINDOWS = "win"

    def write_to_logs(self):
        """
        Function sends the Queue (with 2 samples!) to the comparison unit.
        Afterwards gets the log - insert it to 'status_log.txt' file.
        """
        compare = comparator(self.queue[0], self.queue[1])
        diff_sample = compare.compare()
        with open("status_log.txt", "a") as f:
            for name, status in diff_sample:
                if status != "running" and status != "stopped":
                    continue
                current_time = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
                print(f"{current_time} {name} {status}\n")
                f.write(f"{current_time} {name} {status}\n")

    def write_to_service_list(self, sample):
        """
        Function gets sample and inserts it to the 'service_list.txt' file
        :return: None
        """
        with open("service_list.txt", "a") as f:
            for name, status in sample:
                current_time = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
                # print(f"{current_time} {name} {status}")
                if status == "running":
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
            print(len(self.queue))

            # insert sample into Queue for comparison
            if len(self.queue) == 2:
                self.queue.pop()
                self.queue.insert(0, sample)
                print("vlalala")
                self.write_to_logs()

            elif len(self.queue) == 1 or len(self.queue) == 0:
                self.queue.insert(0, sample)
                print("dididid")

            time.sleep(time_at_seconds)

    def main(self, time_at_seconds):
        # check witch type of sample to take.
        # for windows
        if self.WINDOWS in sys.platform:
            self.get_sample(sample_unit.win_sample, time_at_seconds)

        # for linux
        else:
            self.get_sample(sample_unit.linux_sample, time_at_seconds)
