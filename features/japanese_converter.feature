Feature: Japanese Converter

  Scenario: Convert Syaku_J to Meter_J
    Given the value is 100 Syaku_J
    When I convert it to Meter_J
    Then the result should be 30.3 Meter_J

  Scenario: Convert Syaku_J to Duym_J
    Given the value is 100 Syaku_J
    When I convert it to Duym_J
    Then the result should be 1193.0 Duym_J

  Scenario: Convert Syaku_J to Arshin_J
    Given the value is 100 Syaku_J
    When I convert it to Arshin_J
    Then the result should be 42.7 Arshin_J

  Scenario: Convert Se_J to Liter_J
    Given the value is 100 Se_J
    When I convert it to Liter_J
    Then the result should be 36.8 Liter_J

  Scenario: Convert Se_J to Vedro_J
    Given the value is 100 Se_J
    When I convert it to Vedro_J
    Then the result should be 2.5 Vedro_J

  Scenario: Convert Se_J to Barrel_J
    Given the value is 100 Se_J
    When I convert it to Barrel_J
    Then the result should be 2.8 Barrel_J

  Scenario: Convert Kin_J to Kg_J
    Given the value is 100 Kin_J
    When I convert it to Kg_J
    Then the result should be 60.4 Kg_J

  Scenario: Convert Kin_J to Batman_J
    Given the value is 100 Kin_J
    When I convert it to Batman_J
    Then the result should be 80.0 Batman_J

  Scenario: Convert Kin_J to Funt_J
    Given the value is 100 Kin_J
    When I convert it to Funt_J
    Then the result should be 133.0 Funt_J