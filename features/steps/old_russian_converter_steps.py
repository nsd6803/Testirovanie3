from behave import given, when, then
from OldRussianConverter import OldRussianConverter


@given('the value is {value} Arshin')
def set_arshin_value(context, value):
    context.value = float(value)


@when('I convert it to Inch')
def convert_to_inch(context):
    context.result = OldRussianConverter.arshin_to_inch(context.value)


@then('the result should be {expected} Inch')
def verify_inch_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Meter')
def convert_to_meter(context):
    context.result = OldRussianConverter.arshin_to_meter(context.value)


@then('the result should be {expected} Meter')
def verify_meter_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Shaku')
def convert_to_shaku(context):
    context.result = OldRussianConverter.arshin_to_shaku(context.value)


@then('the result should be {expected} Shaku')
def verify_shaku_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {value} Vedro')
def set_vedro_value(context, value):
    context.value = float(value)


@when('I convert it to Sho')
def convert_to_sho(context):
    context.result = OldRussianConverter.vedro_to_sho(context.value)


@then('the result should be {expected} Sho')
def verify_sho_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Barrel')
def convert_to_barrel(context):
    context.result = OldRussianConverter.vedro_to_barrel(context.value)


@then('the result should be {expected} Barrel')
def verify_barrel_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Liter')
def convert_to_liter(context):
    context.result = OldRussianConverter.vedro_to_liter(context.value)


@then('the result should be {expected} Liter')
def verify_liter_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {value} Batman')
def set_batman_value(context, value):
    context.value = float(value)


@when('I convert it to Kg')
def convert_to_kg(context):
    context.result = OldRussianConverter.batman_to_kg(context.value)


@then('the result should be {expected} Kg')
def verify_kg_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Kin')
def convert_to_kin(context):
    context.result = OldRussianConverter.batman_to_kin(context.value)


@then('the result should be {expected} Kin')
def verify_kin_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Pound')
def convert_to_pound(context):
    context.result = OldRussianConverter.batman_to_pound(context.value)


@then('the result should be {expected} Pound')
def verify_pound_result(context, expected):
    expected = float(expected)
    assert context.result == expected
