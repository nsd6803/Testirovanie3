import unittest
class SIConverter:
    def __init__(self):
        super().__init__()

# Конвертация си в американскую
    def meters_to_inch(self, unit):
        return 0

    def liters_to_barrel(self, unit):
        return 0

    def kilograms_to_pound(self, unit):
        return 0

# Конвертация си в японскую
    def meters_to_syaku(self, unit):
        return 0

    def liters_to_se(self, unit):
        return 0

    def kilograms_to_kin(self, unit):
        return 0

# Конвертация си в старорусскую
    def meters_to_arshin(self, unit):
        return 0

    def liters_to_bucket(self, unit):
        return 0

    def kilograms_to_batman(self, unit):
        return 0

class TestSIConverter(unittest.TestCase):
    def test_syaku_meter(self):
        result1 = SIConverter()

        self.assertEqual(result1.meters_to_inch(100), 3937)

    def test_syaku_duym(self):
        result1 = SIConverter()

        self.assertEqual(result1.liters_to_barrel("159"), 1)

    def test_syaku_arshin(self):
        result1 = SIConverter()

        self.assertEqual(result1.kilograms_to_pound(100), 220)

    def test_se_liter(self):
        result1 = SIConverter()

        self.assertEqual(result1.meters_to_syaku(100), 330)

    def test_se_vedro(self):
        result1 = SIConverter()

        self.assertEqual(result1.liters_to_se("100"), 180)

    def test_se_barrel(self):
        result1 = SIConverter()

        self.assertEqual(result1.kilograms_to_kin(100), 60)

    def test_kin_kg(self):
        result1 = SIConverter()

        self.assertEqual(result1.meters_to_arshin("100"), 140.6)

    def test_kin_batman(self):
        result1 = SIConverter()

        self.assertEqual(result1.liters_to_bucket(100), 1229.9)

    def test_kin_funt(self):
        result1 = SIConverter()
        self.assertEqual(result1.kilograms_to_batman(100), 409.5)

    def test_syaku_meter_fail(self):
        result1 = SIConverter()

        self.assertEqual(result1.meters_to_inch("Hello1"), "Некорректное значение")

    def test_syaku_duym_fail(self):
        result1 = SIConverter()

        self.assertEqual(result1.liters_to_barrel("O.1"), "Некорректное значение")

    def test_syaku_arshin_fail(self):
        result1 = SIConverter()

        self.assertEqual(result1.kilograms_to_pound("12345ff"), "Некорректное значение")

    def test_se_liter_fail(self):
        result1 = SIConverter()

        self.assertEqual(result1.meters_to_syaku("100_"), "Некорректное значение")

    def test_se_vedro_fail(self):
        result1 = SIConverter()

        self.assertEqual(result1.liters_to_se("?юю"), "Некорректное значение")

    def test_se_barrel_fail(self):
        result1 = SIConverter()

        self.assertEqual(result1.kilograms_to_kin(".100"), "Некорректное значение")

    def test_kin_kg_fail(self):
        result1 = SIConverter()

        self.assertEqual(result1.meters_to_arshin("1OO"), "Некорректное значение")

    def test_kin_batman_fail(self):
        result1 = SIConverter()

        self.assertEqual(result1.liters_to_bucket(100000000000000000000000000000000000000000000000000000000000000000),
                         "Некорректное значение")

    def test_kin_funt_fail(self):
        result1 = SIConverter()
        self.assertEqual(result1.kilograms_to_batman("dfef"), "Некорректное значение")
