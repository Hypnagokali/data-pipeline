import unittest
from src import distribution_rnd

class TestDistribution(unittest.TestCase):

    def test_bimodal_dist(self):
        bimodal_pdf = distribution_rnd.distribution(7.5, 0.5, 2, 20, 0.5, 4)
        first_max = bimodal_pdf(7.5)
        after_first_max = bimodal_pdf(8)
        low = bimodal_pdf(15)
        second_max = bimodal_pdf(20)

        self.assertTrue(first_max > after_first_max)
        self.assertTrue(after_first_max > low)
        self.assertTrue(second_max > first_max)

    def test_compare_curves(self):
        relaxing = distribution_rnd.distribution(7.5, 1, 1, 20, 1, 1)
        needs_concentration = distribution_rnd.distribution(10, 3, 2, 15, 1, 1)
        relaxing_max = relaxing(10)
        conc_not_max = needs_concentration(10)

        self.assertTrue(conc_not_max > relaxing_max)
        

if __name__ == '__main__':
    unittest.main()