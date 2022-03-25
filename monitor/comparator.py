import time
from datetime import datetime


class comparator:
    def __init__(self, sample_1, sample_2):
        self.sample_1 = sample_1
        self.sample_2 = sample_2

    def compare(self, newest_sample, old_sample):
        """
        Method compares the two given samples to see differences in status of the services,
        then writes it to the 'status_log.txt' file.
        :param newest_sample: the new sample
        :param old_sample: the old sample
        :return: None
        """
        diff_sample = list(set(newest_sample) - set(old_sample))
        print(diff_sample)
        with open("status_log.txt", "a") as f:
            for name, status in diff_sample:
                print(status)
                if status != "running" and status != "stopped":
                    continue
                current_time = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
                f.write(f"{current_time} {name} {status}\n")

            dead_serves = self.dead_services(old_sample, newest_sample)
            for service_name in dead_serves:
                f.write(f"{current_time} {service_name} killed")

    def dead_services(self, old_sample: list, new_sample: list):
        """
        The method finds the dead services, services which could be found in the old
        sample but are no longer in the new sample.
        :param old_sample: the old sample
        :param new_sample: the new sample
        :return: the dead services
        """
        dead_services = []
        for name, status in old_sample:
            flag = False
            for name_2, status_2 in new_sample:
                if name == name_2:
                    flag = True
            if not flag:
                dead_services.append(name)
        return dead_services
