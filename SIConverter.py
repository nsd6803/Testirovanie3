import unittest
class SIConverter:
    METERS_TO_INCH = 39.37  # Conversion factor
    LITERS_TO_BARREL = 159
    KILOGRAMS_TO_POUND = 2.2
    METERS_TO_SYAKU = 3.3
    LITERS_TO_SE = 1.8
    KILOGRAMS_TO_KIN = 0.6
    METERS_TO_ARSHIN = 1.406
    LITERS_TO_BUCKET = 12.299
    KILOGRAMS_TO_BATMAN = 4.095

# Конвертация си в американскую
    @classmethod
    def meters_to_inch(cls, unit):
        return unit * cls.METERS_TO_INCH

    @classmethod
    def liters_to_barrel(cls, unit):
        return unit / cls.LITERS_TO_BARREL

    @classmethod
    def kilograms_to_pound(cls, unit):
        return unit * cls.KILOGRAMS_TO_POUND

# Конвертация си в японскую
    @classmethod
    def meters_to_syaku(cls, unit):
        return unit * cls.METERS_TO_SYAKU

    @classmethod
    def liters_to_se(cls, unit):
        return unit * cls.LITERS_TO_SE

    @classmethod
    def kilograms_to_kin(cls, unit):
        return unit * cls.KILOGRAMS_TO_KIN

# Конвертация си в старорусскую
    @classmethod
    def meters_to_arshin(cls, unit):
        return unit * cls.METERS_TO_ARSHIN

    @classmethod
    def liters_to_bucket(cls, unit):
        return unit * cls.LITERS_TO_BUCKET

    @classmethod
    def kilograms_to_batman(cls, unit):
        return unit * cls.KILOGRAMS_TO_BATMAN

class TestSIConverter(unittest.TestCase):
    def test_meters_to_inch(self):
        self.assertAlmostEqual(SIConverter.meters_to_inch(1), 39.37, places=2)

    def test_liters_to_barrel(self):
        self.assertAlmostEqual(SIConverter.liters_to_barrel(159), 1, places=2)

    def test_kilograms_to_pound(self):
        self.assertAlmostEqual(SIConverter.kilograms_to_pound(1), 2.2, places=2)

    def test_meters_to_syaku(self):
        self.assertAlmostEqual(SIConverter.meters_to_syaku(1), 3.3, places=2)

    def test_liters_to_se(self):
        self.assertAlmostEqual(SIConverter.liters_to_se(1), 1.8, places=2)

    def test_kilograms_to_kin(self):
        self.assertAlmostEqual(SIConverter.kilograms_to_kin(1), 0.6, places=2)

    def test_meters_to_arshin(self):
        self.assertAlmostEqual(SIConverter.meters_to_arshin(1), 1.406, places=3)

    def test_liters_to_bucket(self):
        self.assertAlmostEqual(SIConverter.liters_to_bucket(1), 12.299, places=3)

    def test_kilograms_to_batman(self):
        self.assertAlmostEqual(SIConverter.kilograms_to_batman(1), 4.095, places=3)
