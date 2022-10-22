import unittest

class Converter:

    def DToMm(self, d):
        if d > 0:
            return d * 25.4
        return "Error!"

    def D2ToSm2(self, d2):
        if d2 > 0:
            return d2*6.45
        return "Error!"

    def D3ToSm3(self, d3):
        if d3 > 0:
            return d3*16.39
        return 'Error!'

    def UToL(self, u):
        if u > 0:
            return u*0.029
        return 'Error!'


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.obj = Converter()

    def test_1(self):
        self.assertEqual(self.obj.DToMm(12), 304.79999999999995)

    def test_2(self):
        self.assertEqual(self.obj.D2ToSm2(23), 148.35)

    def test_3(self):
        self.assertEqual(self.obj.D2ToSm2(245), 1580.25)

    def test_4(self):
        self.assertEqual(self.obj.D3ToSm3(25), 409.75)

    def test_5(self):
        self.assertEqual(self.obj.UToL(23), 0.667)

    def test_6(self):
        self.assertEqual(self.obj.DToMm(-2), 'Error!')

    def test_7(self):
        self.assertEqual(self.obj.D2ToSm2(-2), 'Error!')

    def test_8(self):
        self.assertEqual(self.obj.D3ToSm3(-2), 'Error!')

    def test_9(self):
        self.assertEqual(self.obj.UToL(-2), 'Error!')


if __name__ == "__main__":
    unittest.main()
