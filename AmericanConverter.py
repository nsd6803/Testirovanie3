import unittest

class AmericanConverter:
    @classmethod
    def inch_to_arshin(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 2.54 / 71.12
        return round(result, 1)

    @classmethod
    def inch_to_meter(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 0.0254
        return round(result, 1)

    @classmethod
    def inch_to_syaku(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 0.0838201
        return round(result, 1)

    @classmethod
    def barrel_to_liter(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 119.2
        return round(result, 1)

    @classmethod
    def barrel_to_vedro(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 2450.042472
        return round(result, 1)

    @classmethod
    def barrel_to_ce(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 215.02488
        return round(result, 1)

    @classmethod
    def pound_to_kilogram(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 0.453592
        return round(result, 1)

    @classmethod
    def pound_to_kin(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 0.2721552
        return round(result, 1)

    @classmethod
    def pound_to_batman(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Вы ввели некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Вы ввели некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Вы ввели некорректное значение"

        result = float(unit) * 1.85745924
        return round(result, 1)



class TestAmericanConverter(unittest.TestCase):

    def test_inch_to_arshin_with_letter(self):
        result = AmericanConverter.inch_to_arshin('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_arshin_with_array(self):
        result = AmericanConverter.inch_to_arshin([123, 123])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_arshin_with_valid_input(self):
        result = AmericanConverter.inch_to_arshin(100)
        self.assertEqual(result, 3.6)

    def test_inch_to_meter_with_letter(self):
        result = AmericanConverter.inch_to_meter('b')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_meter_with_array(self):
        result = AmericanConverter.inch_to_meter(["qq", 1234])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_meter_with_valid_input(self):
        result = AmericanConverter.inch_to_meter(100)
        self.assertEqual(result, 2.5)

    def test_inch_to_syaku_with_letter(self):
        result = AmericanConverter.inch_to_syaku('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_syaku_with_array(self):
        result = AmericanConverter.inch_to_syaku([123, 321])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_inch_to_syaku_with_valid_input(self):
        result = AmericanConverter.inch_to_syaku(100)
        self.assertEqual(result, 8.4)

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
        self.assertEqual(result, 21502.5)

    def test_barrel_to_vedro_with_letter(self):
        result = AmericanConverter.barrel_to_vedro('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_barrel_to_vedro_with_array(self):
        result = AmericanConverter.barrel_to_vedro([123, 321])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_barrel_to_vedro_with_valid_input(self):
        result = AmericanConverter.barrel_to_vedro(100)
        self.assertEqual(result, 245004.2)

    def test_pound_to_kilogram_with_letter(self):
        result = AmericanConverter.pound_to_kilogram('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_kilogram_with_array(self):
        result = AmericanConverter.pound_to_kilogram([123, 123])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_kilogram_with_valid_input(self):
        result = AmericanConverter.pound_to_kilogram(100)
        self.assertEqual(result, 45.4)

    def test_pound_to_kin_with_letter(self):
        result = AmericanConverter.pound_to_kin('b')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_kin_with_array(self):
        result = AmericanConverter.pound_to_kin(["qq", 1234])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_kin_with_valid_input(self):
        result = AmericanConverter.pound_to_kin(100)
        self.assertEqual(result, 27.2)

    def test_pound_to_batman_with_letter(self):
        result = AmericanConverter.pound_to_batman('a')
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_batman_with_array(self):
        result = AmericanConverter.pound_to_batman([123, 321])
        self.assertEqual(result, "Вы ввели некорректное значение")

    def test_pound_to_batman_with_valid_input(self):
        result = AmericanConverter.pound_to_batman(100)
        self.assertEqual(result, 185.7)

unittest.main()