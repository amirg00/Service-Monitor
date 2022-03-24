from comparator import comparator


class export_sample_unit:
    def __init__(self, sample_1, sample_2):
        self.sample_1 = sample_1
        self.sample_2 = sample_2

    def compare_diff_export_samples(self):
        compare = comparator(self.sample_1, self.sample_2)
        compare.compare(self.export_sample(self.sample_1), self.export_sample(self.sample_2))

    # TODO: NEED TO ADD ROUNDING A LOG TIME IF IT ISN'T COMPATIBLE TO A CERTAIN SAMPLE TIME
    def export_sample(self, sample_measure_time):
        with open("service_list.txt", "r") as f:
            lines = f.readlines()
            sample = []
            for line in lines:
                line_lst = line.split(' ')
                # print(line_lst)
                if sample_measure_time == line_lst[0]:
                    # print(line_lst[0])
                    service_name = ""
                    for i in range(1, len(line_lst) - 1):
                        service_name += line_lst[i]
                    sample.append((service_name, line_lst[len(line_lst) - 1]))
        # print(sample)
        return sample
