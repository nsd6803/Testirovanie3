Feature: American Converter

  Scenario: Convert Inch_A to Arshin_A
    Given the value is 10 Inch_A
    When I convert it to Arshin_A
    Then the result should be 0.4 Arshin_A

  Scenario: Convert Inch_A to Meter_A
    Given the value is 100 Inch_A
    When I convert it to Meter_A
    Then the result should be 2.5 Meter_A

  Scenario: Convert Inch_A to Syaku_A
    Given the value is 100 Inch_A
    When I convert it to Syaku_A
    Then the result should be 8.4 Syaku_A

  Scenario: Convert Barrel_A to Ce_A
    Given the value is 100 Barrel_A
    When I convert it to Ce_A
    Then the result should be 21502.5 Ce_A

  Scenario: Convert Barrel_A to Vedro_A
    Given the value is 100 Barrel_A
    When I convert it to Vedro_A
    Then the result should be 245004.2 Vedro_A

  Scenario: Convert Barrel_A to Liter_A
    Given the value is 10 Barrel_A
    When I convert it to Liter_A
    Then the result should be 1192 Liter_A

  Scenario: Convert Pound_A to Kilogram_A
    Given the value is 100 Pound_A
    When I convert it to Kilogram_A
    Then the result should be 45.4 Kilogram_A

  Scenario: Convert Pound_A to Kin_A
    Given the value is 100 Pound_A
    When I convert it to Kin_A
    Then the result should be 27.2 Kin_A

  Scenario: Convert Pound_A to Batman_A
    Given the value is 100 Pound_A
    When I convert it to Batman_A
    Then the result should be 185.7 Batman_A