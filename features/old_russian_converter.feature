Feature: Old Russian Converter

  Scenario: Convert Arshin to Inch
    Given the value is 1 Arshin
    When I convert it to Inch
    Then the result should be 28.0 Inch

  Scenario: Convert Arshin to Meter
    Given the value is 1 Arshin
    When I convert it to Meter
    Then the result should be 0.7112 Meter

  Scenario: Convert Arshin to Shaku
    Given the value is 1 Arshin
    When I convert it to Shaku
    Then the result should be 0.71 Shaku

  Scenario: Convert Vedro to Sho
    Given the value is 1 Vedro
    When I convert it to Sho
    Then the result should be 40.0 Sho

  Scenario: Convert Vedro to Barrel
    Given the value is 1 Vedro
    When I convert it to Barrel
    Then the result should be 0.36 Barrel

  Scenario: Convert Vedro to Liter
    Given the value is 1 Vedro
    When I convert it to Liter
    Then the result should be 12.3 Liter

  Scenario: Convert Batman to Kg
    Given the value is 1 Batman
    When I convert it to Kg
    Then the result should be 16.38 Kg

  Scenario: Convert Batman to Kin
    Given the value is 1 Batman
    When I convert it to Kin
    Then the result should be 1.25 Kin

  Scenario: Convert Batman to Pound
    Given the value is 1 Batman
    When I convert it to Pound
    Then the result should be 36.11 Pound