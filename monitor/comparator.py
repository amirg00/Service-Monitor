

class comparator:
    def __init__(self, sample_1, sample_2):
        self.sample_1 = sample_1
        self.sample_2 = sample_2

    def compare(self, newest_sample, old_sample):
        print("blabla\n")
        diff_sample = list(set(newest_sample) - set(old_sample))
        print(diff_sample)

        pass

