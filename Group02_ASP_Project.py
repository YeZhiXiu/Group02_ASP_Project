import pandas as pdimport numpy as np
import matplotlib.pyplot as plt
import Group02_ASP_Project as prog
import unittest


apple = pd.read_excel('IMVA.xls')
print(apple) #read the file



class EvaluateMarks(unittest.TestCase):
    def test_total(self):
        result = prog.EvaluateMarks.total(Group02_ASP_Project)
        self.assertEqual(result, 9358.6)

    def test_mean(self):
        abc = prog.EvaluateMarks.mean(sum(Group02_ASP_Project), len(Group02_ASP_Project))
        self.assertEqual(abc, 302.89032258064515)

if __name__ == '__main__':
    unittest.main()