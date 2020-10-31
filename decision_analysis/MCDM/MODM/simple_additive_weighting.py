import unittest
from decision_analysis.MCDM.MODM.parameter import Parameter


class SAW(Parameter):
    def __init__(self):
        Parameter.__init__(self)

    def calc_saw_ranking(self):
        wf = self._calc_weight_factor()
        nwm = self._alternative_weighting_and_normalized(weight_factor=wf)
        self._calc_alternative_score(normal_weighted_matrix=nwm)

        return nwm

    def _calc_alternative_score(self, normal_weighted_matrix: list):
        for alt in normal_weighted_matrix:
            title = alt.get('title')
            del(alt['title'])
            self.score[title] = self.normalize_score(value=sum(list(alt.values())))

        return

    def _alternative_weighting_and_normalized(self, weight_factor: dict):
        temp = list()
        for alt in self.alternative:
            inf = alt.copy()
            for att in self.attribute:
                nrm = self._normalize(value=inf.get(att),
                                      objective=self.attribute.get(att).get('o'),
                                      weight_fact=weight_factor.get(att))
                inf[att] = nrm * self.attribute.get(att).get('w')

            temp.append(inf)
        return temp

    def _calc_weight_factor(self):
        temp = dict()
        for att in self.attribute:
            tmp = [x.get(att) for x in self.alternative]
            temp[att] = {'min': min(tmp), 'max': max(tmp)}

        return temp

    @staticmethod
    def _normalize(value: float, objective: str, weight_fact: dict) -> float:
        if objective == 'max':
            return (value - weight_fact.get('min')) / (weight_fact.get('max') - weight_fact.get('min'))

        else:
            return (weight_fact.get('max') - value) / (weight_fact.get('max') - weight_fact.get('min'))


class TestCase(unittest.TestCase):
    def test_simple_additive_weighting(self):
        h0 = 'I'  # am the best

        saw = SAW()
        saw.set_attribute_type(at1='max', at2='min', at3='min')
        saw.set_attribute_weight(at3=2.5, at4=1.7)
        saw.set_alternative_value(title='I', at1=12, at2=4.7, at3=3.1, at4=3.75)
        saw.set_alternative_value(title='He', at1=7, at2=4.17, at3=5.01, at4=1.25)
        saw.set_alternative_value(title='She', at1=2, at2=5.7, at3=4.1, at4=0.75)

        saw.calc_saw_ranking()
        h1 = saw.get_best_alternative()

        self.assertEqual(first=h0, second=h1)
        return


if __name__ == '__main__':
    unittest.main()

