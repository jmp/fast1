Feature: Circuits
    An API that provides details about different racing circuits.

    Scenario: Getting the details of a single circuit
        Given I'm an API client
        And I have a reference to a circuit
        When I submit a request for the circuit
        Then I should receive the circuit details
