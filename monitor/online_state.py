import sys
import os
from datetime import datetime
import sample_unit
from comparator import comparator
import time


class online_state:
    def __init__(self):
        self.queue = []
        self.WINDOWS = "win"
        self.last_modification_time = ''

    def write_to_logs(self):
        """
        Function sends the Queue (with 2 samples!) to the comparison unit.
        Afterwards gets the log - insert it to 'status_log.txt' file.
        """
        compare = comparator(self.queue[0], self.queue[1])
        diff_sample = compare.compare()
        
        with open("status_log.txt", "a") as f:
            current_time = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
            for name, status in diff_sample:
                if status != "running" and status != "stopped":
                    continue
                print(f"{current_time} {name} {status}")
                f.write(f"{current_time} {name} {status}\n")
        

    def write_to_service_list(self, sample, is_first_sample):
        """
        Function gets sample and inserts it to the 'service_list.txt' file
        :return: None
        """
        # security check
        if not is_first_sample:
            try:
                modTimesinceEpoc = os.path.getmtime("service_list.txt")
                modificationTime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(modTimesinceEpoc))
                if self.last_modification_time != modificationTime:
                    print("Warning: file service_list.txt was changed unexpectedly!!!")
                
            except:
                print("Warning: file service_list.txt was deleted!!!")
        
        with open("service_list.txt", "a") as f:
            for name, status in sample:
                current_time = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
                if status == "running":
                    print(f"{current_time} {name} {status}") if is_first_sample else None
                    f.write(f"{current_time} {name} {status}\n")
        
        # update program about the current last modified date
        modTimesinceEpoc = os.path.getmtime("service_list.txt")
        modificationTime = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(modTimesinceEpoc))
        self.last_modification_time = modificationTime

    def get_sample(self, get_sample_by_os, time_at_seconds):
        """
        function get sample every time_at_seconds
        and sent it to write into service_list.
        and then, insert it to Queue for logs file.
        """
        is_first_sample = True
        while True:
            sample = get_sample_by_os()
            self.write_to_service_list(sample, is_first_sample)

            # insert sample into Queue for comparison
            if len(self.queue) == 2:
                self.queue.pop()
                self.queue.insert(0, sample)
                self.write_to_logs()

            elif len(self.queue) == 1 or len(self.queue) == 0:
                self.queue.insert(0, sample)

            time.sleep(time_at_seconds)
            is_first_sample = False

    def main(self, time_at_seconds):
        # check witch type of sample to take.
        # for windows
        if self.WINDOWS in sys.platform:
            self.get_sample(sample_unit.win_sample, time_at_seconds)

        # for linux
        else:
            self.get_sample(sample_unit.linux_sample, time_at_seconds)
