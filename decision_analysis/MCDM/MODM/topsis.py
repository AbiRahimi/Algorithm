from decision_analysis.MCDM.MODM.simple_additive_weighting import SAW


class TOPSIS(SAW):
    def __init__(self):
        SAW.__init__(self)

    def calc_topsis_ranking(self):
        nwd = self.calc_saw_ranking()
        print(self.attribute)


if __name__ == '__main__':
    topsis = TOPSIS()
    topsis.set_attribute_type(at1='max', at2='min', at3='min')
    topsis.set_attribute_weight(at3=2.5, at4=1.7)
    topsis.set_alternative_value(title='I', at1=12, at2=4.7, at3=3.1, at4=3.75)
    topsis.set_alternative_value(title='He', at1=7, at2=4.17, at3=5.01, at4=1.25)
    topsis.set_alternative_value(title='She', at1=2, at2=5.7, at3=4.1, at4=0.75)

    topsis.calc_topsis_ranking()

    # h1 = topsis.get_best_alternative()
    # print(h1)

