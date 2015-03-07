Feature: Using modsync
  In order to verify that my application works across multiple framework versions
  As a developer
  I should be able to use modsync for such functionality

  Scenario: Invoking modsync
    When I invoke modsync with no parameters
    Then it should pass