Feature: Handling Invalid Flight Inputs

Scenario: Book a flight where origin = destination

    Given I go to Expedia website
    When 1 adult wants to fly on 22/12/2017 from LHR to LHR
    Then I shall see an error telling me that origin and destination are the same

Scenario: Book a flight in the past
    Given I go to Expedia website
    When 2 adult wants to fly on 22/12/2016 from LHR to HAM
    Then I shall see an error telling me that the date is in the past