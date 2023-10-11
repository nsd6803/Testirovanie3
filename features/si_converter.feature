Feature: SI Converter

  Scenario: Convert Meter_S to Inch_S
    Given the value is 1 Meter_S
    When I convert it to Inch_S
    Then the result should be 39.37 Inch_S

  Scenario: Convert Liter_S to Barrel_S
    Given the value is 159 Liter_S
    When I convert it to Barrel_S
    Then the result should be 1 Barrel_S

  Scenario: Convert Kilogram_S to Pound_S
    Given the value is 1 Kilogram_S
    When I convert it to Pound_S
    Then the result should be 2.2 Pound_S

  Scenario: Convert Meter_S to Syaku_S
    Given the value is 1 Meter_S
    When I convert it to Syaku_S
    Then the result should be 3.3 Syaku_S

  Scenario: Convert Liter_S to Se_S
    Given the value is 1 Liter_S
    When I convert it to Se_S
    Then the result should be 1.8 Se_S

  Scenario: Convert Kilogram_S to Kin_S
    Given the value is 1 Kilogram_S
    When I convert it to Kin_S
    Then the result should be 0.6 Kin_S

  Scenario: Convert Meter_S to Arshin_S
    Given the value is 1 Meter_S
    When I convert it to Arshin_S
    Then the result should be 1.406 Arshin_S

  Scenario: Convert Liter_S to Bucket_S
    Given the value is 1 Liter_S
    When I convert it to Bucket_S
    Then the result should be 12.299 Bucket_S

  Scenario: Convert Kilogram_S to Batman_S
    Given the value is 1 Kilogram_S
    When I convert it to Batman_S
    Then the result should be 4.095 Batman_S
