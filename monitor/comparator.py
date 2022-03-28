import time
from datetime import datetime


class comparator:
    def __init__(self, newest_sample, old_sample):
        # the older sample
        self.old_sample = old_sample
        # the newer sample
        self.newest_sample = newest_sample

    def compare(self):
        """
        ONLINE MODE: Method compares the two given samples to see differences in status of the services,
        then writes it to the 'status_log.txt' file.
        :return: the difference list
        """
        return list(set(self.newest_sample) - set(self.old_sample))

    def compare_offline(self,):
        """
        OFFLINE MODE: Method compares the two given samples to see differences in status of the services,
        then returns it.
        :return: the concat list.
        """
        run_diff_sample = [(name, "running") for name, status in list(set(self.newest_sample) - set(self.old_sample))]
        stop_diff_sample = [(name, "stopped") for name, status in list(set(self.old_sample) - set(self.newest_sample))]
        return run_diff_sample + stop_diff_sample
