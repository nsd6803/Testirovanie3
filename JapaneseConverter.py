import unittest


class JapaneseConverter:
    SYAKU_TO_METER = 0.303
    SYAKU_TO_DUYM = 11.93
    SYAKU_TO_ARSHIN = 0.427
    SE_TO_LITER = 0.368
    SE_TO_VEDRO = 0.025
    SE_TO_BARREL = 0.0278
    KIN_TO_KG = 0.604
    KIN_TO_BATMAN = 0.8
    KIN_TO_FUNT = 1.33


    @classmethod
    def syaku_meter(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"

        result = float(unit) * cls.SYAKU_TO_METER
        return round(result, 1)

    @classmethod
    def syaku_duym(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"

        result = float(unit) * cls.SYAKU_TO_DUYM
        return round(result, 1)

    @classmethod
    def syaku_arshin(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"

        result = float(unit) * cls.SYAKU_TO_ARSHIN
        return round(result, 1)

    @classmethod
    def se_liter(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"

        result = float(unit) * cls.SE_TO_LITER
        return round(result, 1)

    @classmethod
    def se_vedro(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"

        result = float(unit) * cls.SE_TO_VEDRO
        return round(result, 1)

    @classmethod
    def se_barrel(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"
        result = float(unit) * cls.SE_TO_BARREL
        return round(result, 1)

    @classmethod
    def kin_kg(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"

        result = float(unit) * cls.KIN_TO_KG
        return round(result, 1)

    @classmethod
    def kin_batman(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"

        result = float(unit) * cls.KIN_TO_BATMAN
        return round(result, 1)

    @classmethod
    def kin_funt(cls, unit):
        if not isinstance(unit, (int, float)):
            return "Некорректное значение"

        if not (-1e10 <= unit <= 1e10):
            return "Некорректное значение"

        if isinstance(unit, str):
            try:
                unit_int = int(unit)
                unit_float = float(unit)
            except ValueError:
                return "Некорректное значение"
            else:
                if str(unit) != str(unit_int) or str(unit) != str(unit_float):
                    return "Некорректное значение"

        result = float(unit) * cls.KIN_TO_FUNT
        return round(result, 1)


class TestJapanese(unittest.TestCase):
    def test_syaku_meter(self):
        self.assertEqual(JapaneseConverter.syaku_meter(100), 30.3)

    def test_syaku_duym(self):
        self.assertEqual(JapaneseConverter.syaku_duym(100), 1193.0)

    def test_syaku_arshin(self):
        self.assertEqual(JapaneseConverter.syaku_arshin(100), 42.7)

    def test_se_liter(self):
        self.assertEqual(JapaneseConverter.se_liter(100), 36.8)

    def test_se_vedro(self):
        self.assertEqual(JapaneseConverter.se_vedro(100), 2.5)

    def test_se_barrel(self):
        self.assertEqual(JapaneseConverter.se_barrel(100), 2.8)

    def test_kin_kg(self):
        self.assertEqual(JapaneseConverter.kin_kg(100), 60.4)

    def test_kin_batman(self):
        self.assertEqual(JapaneseConverter.kin_batman(100), 80.0)

    def test_kin_funt(self):
        self.assertEqual(JapaneseConverter.kin_funt(100), 133.0)

    def test_syaku_meter_fail(self):
        self.assertEqual(JapaneseConverter.syaku_meter("Hello1"), "Некорректное значение")

    def test_syaku_duym_fail(self):
        self.assertEqual(JapaneseConverter.syaku_duym("O.1"), "Некорректное значение")

    def test_syaku_arshin_fail(self):
        self.assertEqual(JapaneseConverter.syaku_arshin("12345ff"), "Некорректное значение")

    def test_se_liter_fail(self):
        self.assertEqual(JapaneseConverter.se_liter("100_"), "Некорректное значение")

    def test_se_vedro_fail(self):
        self.assertEqual(JapaneseConverter.se_vedro({"unit": 100}), "Некорректное значение")

    def test_se_barrel_fail(self):
        self.assertEqual(JapaneseConverter.se_barrel([100]), "Некорректное значение")

    def test_kin_kg_fail(self):
        self.assertEqual(JapaneseConverter.kin_kg("1OO"), "Некорректное значение")

    def test_kin_batman_fail(self):
        self.assertEqual(
            JapaneseConverter.kin_batman(100000000000000000000000000000000000000000000000000000000000000000),
            "Некорректное значение")

    def test_kin_funt_fail(self):
        self.assertEqual(JapaneseConverter.kin_funt("dfef"), "Некорректное значение")
