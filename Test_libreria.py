import unittest
import Libreria

class Test_simulacion(unittest.TestCase):

    def test_programing_drill_3_2_2(self):
        print(Libreria.drill3_2__2(2, 5, [0, '1/2', '1/2', 0, 0, 0, 0, 0],
                               [[0, 0, 0, '1/3', '1/3', '1/3', 0, 0], [0, 0, 0, 0, 0, '1/3', '1/3', '1/3']]))