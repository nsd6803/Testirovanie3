Feature: SI Converter

  Scenario: Convert Meter to Inch
    Given the value is 1 Meter
    When I convert it to Inch
    Then the result should be 39.37 Inch

  Scenario: Convert Liter to Barrel
    Given the value is 159 Liter
    When I convert it to Barrel
    Then the result should be 1 Barrel

  Scenario: Convert Kilogram to Pound
    Given the value is 1 Kilogram
    When I convert it to Pound
    Then the result should be 2.2 Pound

  Scenario: Convert Meter to Syaku
    Given the value is 1 Meter
    When I convert it to Syaku
    Then the result should be 3.3 Syaku

  Scenario: Convert Liter to Se
    Given the value is 1 Liter
    When I convert it to Se
    Then the result should be 1.8 Se

  Scenario: Convert Kilogram to Kin
    Given the value is 1 Kilogram
    When I convert it to Kin
    Then the result should be 0.6 Kin

  Scenario: Convert Meter to Arshin
    Given the value is 1 Meter
    When I convert it to Arshin
    Then the result should be 1.406 Arshin

  Scenario: Convert Liter to Bucket
    Given the value is 1 Liter
    When I convert it to Bucket
    Then the result should be 12.299 Bucket

  Scenario: Convert Kilogram to Batman
    Given the value is 1 Kilogram
    When I convert it to Batman
    Then the result should be 4.095 Batman
