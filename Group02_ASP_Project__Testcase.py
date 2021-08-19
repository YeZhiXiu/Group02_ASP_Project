import unittest
import Group02_ASP_Project as prog

class Evaluate(unittest.TestCase):
    def test_total(self):
        self.assertEqual(prog.total, 28664611)

    def test_mean(self):
        self.assertEqual(prog.mean, 9554870.34)

if __name__ == '__main__':
    unittest.main()
