from comparator import comparator
from datetime import datetime
from datetime import timedelta


class export_sample_unit:
    def __init__(self, sample_1, sample_2):
        self.sample_1 = sample_1
        self.sample_2 = sample_2
        # Epsilon of time is 5 seconds
        self.delta_time = timedelta(seconds=5)

    def compare_diff_export_samples(self):
        compare = comparator(self.export_sample(self.sample_2), self.export_sample(self.sample_1))
        print(compare.compare_offline())

    def export_sample(self, sample_measure_time):
        with open("service_list.txt", "r") as f:
            lines = f.readlines()
            sample = []
            for index, line in enumerate(lines[::-1]):
                line_lst = line.split(' ')
                format_1 = self.get_date_formatted(sample_measure_time)
                format_2 = self.get_date_formatted(line_lst[0])

                if format_2 <= format_1 and self.compare_time_by_epsilon(format_2, format_1):
                    while lines[::-1][index].split(' ')[0] == line_lst[0]:
                        line_lst = lines[::-1][index].split(' ')
                        service_name = ""
                        for i in range(1, len(line_lst) - 1):
                            service_name += line_lst[i]
                        sample.append((service_name, line_lst[len(line_lst) - 1]))
                        index += 1
                        # loop break condition to avoid out of bounds error.
                        if index >= len(lines[::-1]):
                            break
                    break
        f.close()
        return sample

    def get_date_formatted(self, date: str):
        """
        Method takes a date format as in the logs and converts is to a new date format.
        Afterwards, the method returns it as an 'strptime' object for comparison purposes
        E.g.: 25-03-2022-16:01:32 ->  25-03-2022 16:01:32
        """
        formatted_date = date[:10] + ' ' + date[11:]
        return datetime.strptime(formatted_date, "%d-%m-%Y %H:%M:%S")

    def compare_time_by_epsilon(self, time, time_2):
        return abs(time - time_2) < self.delta_time
