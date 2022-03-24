from export_sample_unit import export_sample_unit


class offline_state:

    def main(self, sample_time, sample_2_time):
        export = export_sample_unit(sample_time, sample_2_time)
        export.compare_diff_export_samples()
