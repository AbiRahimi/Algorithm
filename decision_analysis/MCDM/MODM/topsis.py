from decision_analysis.MCDM.MODM.simple_additive_weighting import SAW


class TOPSIS(SAW):
    def __init__(self):
        SAW.__init__(self)

    def calc_ranking(self):
        pass

    def get_first_alternative(self) -> str:
        pass

    def get_alternative_score(self, title: str) -> float:
        pass
