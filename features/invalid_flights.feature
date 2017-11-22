Feature: Handling Invalid Flight Inputs

Scenario: Book an invalid flight

    Given I go to Expedia website
    When "1" adult wants to fly on "22/12/2017" from "LHR" to "LHR"
    Then I shall see an error telling me that origin and destination are the same