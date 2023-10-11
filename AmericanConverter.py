import unittest

class AmericanConverter:
    BATMAN_TO_POUND = 36.11



class TestAmericanConverter(unittest.TestCase):

    def test_inch_to_arshin_with_letter(self):
        result = AmericanConverter.inch_to_arshin('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_arshin_with_array(self):
        result = AmericanConverter.inch_to_arshin([123, 123])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_arshin_with_valid_input(self):
        result = AmericanConverter.inch_to_arshin(100)
        self.assertEqual(result, 3.5714)

    def test_inch_to_meter_with_letter(self):
        result = AmericanConverter.inch_to_meter('b')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_meter_with_array(self):
        result = AmericanConverter.inch_to_meter(["qq", 1234])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_meter_with_valid_input(self):
        result = AmericanConverter.inch_to_meter(100)
        self.assertEqual(result, 2.54)

    def test_inch_to_syaku_with_letter(self):
        result = AmericanConverter.inch_to_syaku('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_syaku_with_array(self):
        result = AmericanConverter.inch_to_syaku([123, 321])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_syaku_with_valid_input(self):
        result = AmericanConverter.inch_to_syaku(100)
        self.assertEqual(result, 8.382)

    def test_barrel_to_liter_with_letter(self):
        result = AmericanConverter.barrel_to_liter('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_barrel_to_liter_with_array(self):
        result = AmericanConverter.barrel_to_liter([123, 123])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_barrel_to_liter_with_valid_input(self):
        result = AmericanConverter.barrel_to_liter(100)
        self.assertEqual(result, 11920)

    def test_barrel_to_ce_with_letter(self):
        result = AmericanConverter.barrel_to_ce('b')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_barrel_to_ce_with_array(self):
        result = AmericanConverter.barrel_to_ce(["qq", 1234])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_barrel_to_ce_with_valid_input(self):
        result = AmericanConverter.barrel_to_ce(100)
        self.assertEqual(result, 21502.488)

    def test_barrel_to_vedro_with_letter(self):
        result = AmericanConverter.barrel_to_vedro('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_barrel_to_vedro_with_array(self):
        result = AmericanConverter.barrel_to_vedro([123, 321])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_barrel_to_vedro_with_valid_input(self):
        result = AmericanConverter.barrel_to_vedro(100)
        self.assertEqual(result, 245004,2472)

    def test_pound_to_kilogram_with_letter(self):
        result = AmericanConverter.pound_to_kilogram('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_kilogram_with_array(self):
        result = AmericanConverter.pound_to_kilogram([123, 123])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_kilogram_with_valid_input(self):
        result = AmericanConverter.pound_to_kilogram(100)
        self.assertEqual(result, 45.3592)

    def test_pound_to_kin_with_letter(self):
        result = AmericanConverter.pound_to_kin('b')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_kin_with_array(self):
        result = AmericanConverter.pound_to_kin(["qq", 1234])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_kin_with_valid_input(self):
        result = AmericanConverter.pound_to_kin(100)
        self.assertEqual(result, 27.21552)

    def test_pound_to_batman_with_letter(self):
        result = AmericanConverter.pound_to_batman('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_batman_with_array(self):
        result = AmericanConverter.pound_to_batman([123, 321])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_batman_with_valid_input(self):
        result = AmericanConverter.pound_to_batman(100)
        self.assertEqual(result, 185.745924)

unittest.main()