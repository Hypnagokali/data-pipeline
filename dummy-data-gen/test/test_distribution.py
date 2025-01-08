import unittest
from src import distribution_rnd

class TestDistribution(unittest.TestCase):

    def test_bimodal_dist(self):
        first_max = distribution_rnd.bimodal_pdf(7.5)
        after_first_max = distribution_rnd.bimodal_pdf(8)
        low = distribution_rnd.bimodal_pdf(15)
        second_max = distribution_rnd.bimodal_pdf(20)

        self.assertTrue(first_max > after_first_max)
        self.assertTrue(after_first_max > low)
        self.assertTrue(second_max > first_max)
        

if __name__ == '__main__':
    unittest.main()