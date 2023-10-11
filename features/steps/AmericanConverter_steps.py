from behave import given, when, then


@given('the value is {value} Inch')
def set_inch_value(context, value):
    context.value = float(value)


@when('I convert it to Arshin')
def convert_to_arshin(context):
    context.result = AmericanConverter.inch_to_arshin(context.value)


@then('the result should be {expected} Arshin')
def verify_arshin_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Meter')
def convert_to_meter(context):
    context.result = AmericanConverter.inch_to_meter(context.value)


@then('the result should be {expected} Meter')
def verify_meter_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Syaku')
def convert_to_syaku(context):
    context.result = AmericanConverter.inch_to_syaku(context.value)


@then('the result should be {expected} Syaku')
def verify_syaku_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {value} Barrel')
def set_barrel_value(context, value):
    context.value = float(value)


@when('I convert it to Ce')
def convert_to_ce(context):
    context.result = AmericanConverter.barrel_to_ce(context.value)


@then('the result should be {expected} Ce')
def verify_ce_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Vedro')
def convert_to_vedro(context):
    context.result = AmericanConverter.barrel_to_vedro(context.value)


@then('the result should be {expected} Vedro')
def verify_vedro_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Liter')
def convert_to_liter(context):
    context.result = AmericanConverter.barrel_to_liter(context.value)


@then('the result should be {expected} Liter')
def verify_liter_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@given('the value is {value} Pound')
def set_pound_value(context, value):
    context.value = float(value)


@when('I convert it to Kilogram')
def convert_to_kilogram(context):
    context.result = AmericanConverter.pound_to_kilogram(context.value)


@then('the result should be {expected} Kilogram')
def verify_kilogram_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Kin')
def convert_to_kin(context):
    context.result = AmericanConverter.pound_to_kin(context.value)


@then('the result should be {expected} Kin')
def verify_kin_result(context, expected):
    expected = float(expected)
    assert context.result == expected


@when('I convert it to Batman')
def convert_to_batman(context):
    context.result = AmericanConverter.pound_to_batman(context.value)


@then('the result should be {expected} Batman')
def verify_batman_result(context, expected):
    expected = float(expected)
    assert context.result == expected