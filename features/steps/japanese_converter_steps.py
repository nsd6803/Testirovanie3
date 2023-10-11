from behave import given, when, then
from JapaneseConverter import JapaneseConverter


@given('the value is {value} Syaku_J')
def set_arshin_value(context, value):
    context.value = float(value)


@when('I convert it to Duym_J')
def convert_to_inch(context):
    context.result = JapaneseConverter.syaku_duym(context.value)


@then('the result should be {expected} Duym_J')
def verify_inch_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Meter_J')
def convert_to_meter(context):
    context.result = JapaneseConverter.syaku_meter(context.value)


@then('the result should be {expected} Meter_J')
def verify_meter_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Arshin_J')
def convert_to_shaku(context):
    context.result = JapaneseConverter.syaku_arshin(context.value)


@then('the result should be {expected} Arshin_J')
def verify_shaku_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {value} Se_J')
def set_vedro_value(context, value):
    context.value = float(value)


@when('I convert it to Liter_J')
def convert_to_sho(context):
    context.result = JapaneseConverter.se_liter(context.value)


@then('the result should be {expected} Liter_J')
def verify_sho_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Vedro_J')
def convert_to_barrel(context):
    context.result = JapaneseConverter.se_vedro(context.value)


@then('the result should be {expected} Vedro_J')
def verify_barrel_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Barrel_J')
def convert_to_liter(context):
    context.result = JapaneseConverter.se_barrel(context.value)


@then('the result should be {expected} Barrel_J')
def verify_liter_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {value} Kin_J')
def set_batman_value(context, value):
    context.value = float(value)


@when('I convert it to Kg_J')
def convert_to_kg(context):
    context.result = JapaneseConverter.kin_kg(context.value)


@then('the result should be {expected} Kg_J')
def verify_kg_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Batman_J')
def convert_to_kin(context):
    context.result = JapaneseConverter.kin_batman(context.value)


@then('the result should be {expected} Batman_J')
def verify_kin_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Funt_J')
def convert_to_pound(context):
    context.result = JapaneseConverter.kin_funt(context.value)


@then('the result should be {expected} Funt_J')
def verify_pound_result(context, expected):
    expected = float(expected)
    assert context.result == expected
