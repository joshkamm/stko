"""
EnergyResults
=============

"""

from .results import Results


class EnergyResults(Results):
    """
    Results class containing molecule energy.

    """

    def __init__(self, generator, unit_string):

        self._value = next(generator)
        self._unit_string = unit_string

    def get_energy(self):
        return self._value

    def get_unit_string(self):
        return self._unit_string