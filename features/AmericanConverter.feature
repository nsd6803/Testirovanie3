Feature: American Converter

  Scenario: Convert Inch to Arshin
    Given the value is 10 Inch
    When I convert it to Arshin
    Then the result should be 0.4 Arshin

  Scenario: Convert Inch to Meter
    Given the value is 100 Inch
    When I convert it to Meter
    Then the result should be 2.5 Meter

  Scenario: Convert Inch to Syaku
    Given the value is 100 Inch
    When I convert it to Syaku
    Then the result should be 8.4 Shaku

  Scenario: Convert Barrel to Ce
    Given the value is 100 Barrel
    When I convert it to Ce
    Then the result should be 21502.5 Ce

  Scenario: Convert Barrel to Vedro
    Given the value is 100 Barrel
    When I convert it to Vedro
    Then the result should be 245003.2 Veddro

  Scenario: Convert Barrel to Liter
    Given the value is 10 Barrel
    When I convert it to Liter
    Then the result should be 1192 Liter

  Scenario: Convert Pound to Kilogram
    Given the value is 100 Pound
    When I convert it to Kilogram
    Then the result should be 45.4 Kilogram

  Scenario: Convert Pound to Kin
    Given the value is 100 Pound
    When I convert it to Kin
    Then the result should be 27.2 Kin

  Scenario: Convert Pound to Batman
    Given the value is 100 Pound
    When I convert it to Batman
    Then the result should be 185.7 Pound