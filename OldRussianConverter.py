import unittest


class OldRussianConverter:
    pass


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
