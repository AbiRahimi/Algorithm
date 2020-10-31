import unittest


class Parameter(object):
    def __init__(self):
        self.alternative = list()
        self.attribute = dict()
        self.score = dict()

    def set_attribute_type(self, **kwargs):
        for key in kwargs:
            if key not in self.attribute:
                self.attribute[key] = {'w': 1, 'o': 'max'}

            typ = kwargs.get(key).lower()
            self.attribute[key]['o'] = 'max' if typ.find('min') == -1 else 'min'

        return

    def set_attribute_weight(self, **kwargs):
        for key in kwargs:
            if key not in self.attribute:
                self.attribute[key] = {'w': 1, 'o': 'max'}

            self.attribute[key]['w'] = float(kwargs.get(key))

        return

    def set_alternative_value(self, title: str, **kwargs):
        alt = kwargs
        alt['title'] = title
        self.alternative.append(alt)

        return

    def get_best_alternative(self) -> str:
        max_score = max(list(self.score.values()))
        for alt in self.score:
            if self.score.get(alt) >= max_score:
                return alt

    def get_alternative_score(self, title: str) -> float:
        return self.score.get(title)

    def normalize_score(self, value):
        max_val = sum([self.attribute.get(x).get('w') for x in self.attribute])
        return value / max_val
