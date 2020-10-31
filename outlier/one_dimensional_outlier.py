import statistics as st


class Outlier(object):
    def __init__(self):
        pass

    class BoxPlot(object):
        def __init__(self, data_vector: list, factor=None):
            self._ds = data_vector
            self._factor = 1.5 if factor is None else factor

        def get_upper_bound_outlier(self) -> list:
            pass

        def get_lower_bound_outlier(self):
            pass

    class Normal(object):
        def __init__(self, data_vector: list, factor=None):
            self._ds = data_vector
            self._mean = st.mean(data)
            self._std = st.stdev(data)
            self._factor = 2.5 if factor is None else factor

        def get_upper_bound_outlier(self):
            return list(filter(lambda x: x > self._mean + self._factor * self._std, self._ds))

        def get_lower_bound_outlier(self):
            return list(filter(lambda x: x < self._mean - self._factor * self._std, self._ds))


if __name__ == '__main__':
    data = [14, 12, 7, 12, 10, 10, 19, 8, 13, 27, 50]
    print(st.mean(data), st.stdev(data))
    vl = Outlier().Normal(data_vector=data).get_upper_bound_outlier()
    print(vl)
