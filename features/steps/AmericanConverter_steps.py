from behave import given, when, then
from AmericanConverter import AmericanConverter

@given('the value is {value} Inch_A')
def set_inch_value(context, value):
    context.value = float(value)


@when('I convert it to Arshin_A')
def convert_to_arshin(context):
    context.result = AmericanConverter.inch_to_arshin(context.value)


@then('the result should be {expected} Arshin_A')
def verify_arshin_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Meter_A')
def convert_to_meter(context):
    context.result = AmericanConverter.inch_to_meter(context.value)


@then('the result should be {expected} Meter_A')
def verify_meter_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Syaku_A')
def convert_to_syaku(context):
    context.result = AmericanConverter.inch_to_syaku(context.value)


@then('the result should be {expected} Syaku_A')
def verify_syaku_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {value} Barrel_A')
def set_barrel_value(context, value):
    context.value = float(value)


@when('I convert it to Ce_A')
def convert_to_ce(context):
    context.result = AmericanConverter.barrel_to_ce(context.value)


@then('the result should be {expected} Ce_A')
def verify_ce_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Vedro_A')
def convert_to_vedro(context):
    context.result = AmericanConverter.barrel_to_vedro(context.value)


@then('the result should be {expected} Vedro_A')
def verify_vedro_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Liter_A')
def convert_to_liter(context):
    context.result = AmericanConverter.barrel_to_liter(context.value)


@then('the result should be {expected} Liter_A')
def verify_liter_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {value} Pound_A')
def set_pound_value(context, value):
    context.value = float(value)


@when('I convert it to Kilogram_A')
def convert_to_kilogram(context):
    context.result = AmericanConverter.pound_to_kilogram(context.value)


@then('the result should be {expected} Kilogram_A')
def verify_kilogram_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Kin_A')
def convert_to_kin(context):
    context.result = AmericanConverter.pound_to_kin(context.value)


@then('the result should be {expected} Kin_A')
def verify_kin_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Batman_A')
def convert_to_batman(context):
    context.result = AmericanConverter.pound_to_batman(context.value)


@then('the result should be {expected} Batman_A')
def verify_batman_result(context, expected):
    expected = float(expected)
    assert context.result == expected