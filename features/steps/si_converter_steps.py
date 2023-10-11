from behave import given, when, then
from SIConverter import SIConverter


@given('the value is {unit} Meter_S')
def set_meter_value(context, unit):
    context.value = float(unit)


@when('I convert it to Inch_S')
def convert_to_inch(context):
    context.result = SIConverter.meters_to_inch(context.value)


@then('the result should be {expected} Inch_S')
def verify_inch_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Syaku_S')
def convert_to_syaku(context):
    context.result = SIConverter.meters_to_syaku(context.value)


@then('the result should be {expected} Syaku_S')
def verify_syaku_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Arshin_S')
def convert_to_arshin(context):
    context.result = SIConverter.meters_to_arshin(context.value)


@then('the result should be {expected} Arshin_S')
def verify_arshin_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {unit} Liter_S')
def set_liter_value(context, unit):
    context.value = float(unit)


@when('I convert it to Se_S')
def convert_to_se(context):
    context.result = SIConverter.liters_to_se(context.value)


@then('the result should be {expected} Se_S')
def verify_se_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Barrel_S')
def convert_to_barrel(context):
    context.result = SIConverter.liters_to_barrel(context.value)


@then('the result should be {expected} Barrel_S')
def verify_barrel_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Bucket_S')
def convert_to_bucket(context):
    context.result = SIConverter.liters_to_bucket(context.value)


@then('the result should be {expected} Bucket_S')
def verify_bucket_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {unit} Kilogram_S')
def set_kilogram_value(context, unit):
    context.value = float(unit)


@when('I convert it to Pound_S')
def convert_to_pound(context):
    context.result = SIConverter.kilograms_to_pound(context.value)


@then('the result should be {expected} Pound_S')
def verify_pound_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Kin_S')
def convert_to_kin(context):
    context.result = SIConverter.kilograms_to_kin(context.value)


@then('the result should be {expected} Kin_S')
def verify_kin_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Batman_S')
def convert_to_batman(context):
    context.result = SIConverter.kilograms_to_batman(context.value)


@then('the result should be {expected} Batman_S')
def verify_batman_result(context, expected):
    expected = float(expected)
    assert context.result == expected
    
