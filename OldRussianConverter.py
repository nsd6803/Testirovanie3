import unittest


class OldRussianConverter:
    ARSHIN_TO_INCH = 28.0  # Conversion factor
    ARSHIN_TO_METER = 0.7112
    ARSHIN_TO_SHAKU = 0.71
    VEDRO_TO_SHO = 40.0
    VEDRO_TO_BARREL = 0.36
    VEDRO_TO_LITER = 12.3
    BATMAN_TO_KG = 16.38
    BATMAN_TO_KIN = 1.25
    BATMAN_TO_POUND = 36.11

    @classmethod
    def arshin_to_inch(cls, value):
        return value * cls.ARSHIN_TO_INCH

    @classmethod
    def arshin_to_meter(cls, value):
        return value * cls.ARSHIN_TO_METER

    @classmethod
    def arshin_to_shaku(cls, value):
        return value * cls.ARSHIN_TO_SHAKU

    @classmethod
    def vedro_to_sho(cls, value):
        return value * cls.VEDRO_TO_SHO

    @classmethod
    def vedro_to_barrel(cls, value):
        return value * cls.VEDRO_TO_BARREL

    @classmethod
    def vedro_to_liter(cls, value):
        return value * cls.VEDRO_TO_LITER

    @classmethod
    def batman_to_kg(cls, value):
        return value * cls.BATMAN_TO_KG

    @classmethod
    def batman_to_kin(cls, value):
        return value * cls.BATMAN_TO_KIN

    @classmethod
    def batman_to_pound(cls, value):
        return value * cls.BATMAN_TO_POUND


class TestOldRussianConverter(unittest.TestCase):
    def test_arshin_to_inch(self):
        self.assertEqual(OldRussianConverter.arshin_to_inch(1), 28.0)

    def test_arshin_to_meter(self):
        self.assertAlmostEqual(OldRussianConverter.arshin_to_meter(1), 0.7112, places=4)

    def test_arshin_to_shaku(self):
        self.assertAlmostEqual(OldRussianConverter.arshin_to_shaku(1), 0.71, places=2)

    def test_vedro_to_sho(self):
        self.assertEqual(OldRussianConverter.vedro_to_sho(1), 40.0)

    def test_vedro_to_barrel(self):
        self.assertAlmostEqual(OldRussianConverter.vedro_to_barrel(1), 0.36, places=2)

    def test_vedro_to_liter(self):
        self.assertAlmostEqual(OldRussianConverter.vedro_to_liter(1), 12.3, places=2)

    def test_batman_to_kg(self):
        self.assertAlmostEqual(OldRussianConverter.batman_to_kg(1), 16.38, places=2)

    def test_batman_to_kin(self):
        self.assertAlmostEqual(OldRussianConverter.batman_to_kin(1), 1.25, places=2)

    def test_batman_to_pound(self):
        self.assertAlmostEqual(OldRussianConverter.batman_to_pound(1), 36.11, places=2)
