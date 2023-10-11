import unittest


class JapaneseConverter:
    def __init__(self):
        super().__init__()

    def syaku_meter(self, unit):
        return 0

    def syaku_duym(self, unit):
        return 0

    def syaku_arshin(self, unit):
        return 0

    def se_liter(self, unit):
        return 0

    def se_vedro(self, unit):
        return 0

    def se_barrel(self, unit):
        return 0

    def kin_kg(self, unit):
        return 0

    def kin_batman(self, unit):
        return 0

    def kin_funt(self, unit):
        return 0


class TestJapanese(unittest.TestCase):
    def test_syaku_meter(self):
        result1 = JapaneseConverter()

        self.assertEqual(result1.syaku_meter(100), 30.3)

    def test_syaku_duym(self):
        result1 = JapaneseConverter()

        self.assertEqual(result1.syaku_duym(100), 1192.913)

    def test_syaku_arshin(self):
        result1 = JapaneseConverter()

        self.assertEqual(result1.syaku_arshin(100), 42.6)

    def test_se_liter(self):
        result1 = JapaneseConverter()

        self.assertEqual(result1.se_liter(100), 1.8039)

    def test_se_vedro(self):
        result1 = JapaneseConverter()

        self.assertEqual(result1.se_vedro(100), 0.15)

    def test_se_barrel(self):
        result1 = JapaneseConverter()

        self.assertEqual(result1.se_barrel(100), 0.011)

    def test_kin_kg(self):
        result1 = JapaneseConverter()

        self.assertEqual(result1.kin_kg(100), 0.6)

    def test_kin_batman(self):
        result1 = JapaneseConverter()

        self.assertEqual(result1.kin_batman(100), 2.46)

    def test_kin_funt(self):
        result1 = JapaneseConverter()
        self.assertEqual(result1.kin_funt(100), 1.322774)
