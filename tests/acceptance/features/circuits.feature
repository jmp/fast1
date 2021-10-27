Feature: Circuits
    An API that provides details about different racing circuits.

    Scenario: Getting the details of a single circuit
        Given I'm a user
        And I have a reference to a circuit
        When I submit a request for the circuit
        Then I should not get an error
        And I should receive the circuit details
