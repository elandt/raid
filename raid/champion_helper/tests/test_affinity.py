from django.test import TestCase

from models import Affinity


def create_affinity(name, strength, weakness):
    """
    Create an affinity with the given 'name', 'strength', and 'weakness'.
    'strength' and 'weakness can be null'
    """

    return Affinity.objects.create(
        name=name,
        strength=strength,
        weakness=weakness)


class AffinityModelTests(TestCase):

    def test_affinity_with_null_strength_and_weakness(self):
        """
        Create an affinity with where both the 'strength' and 'weakness' are null.
        This is the case for the Void affinity as of 5/16/2020
        """
        aff = create_affinity(name="void")
        self.assertIsNone(aff.strength)
        self.assertIsNone(aff.weakness)
