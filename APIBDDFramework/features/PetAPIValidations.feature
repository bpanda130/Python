# Created by Bishnu at 2/23/2021
Feature: Verify all the Pet APIs from PetStore
  # Enter feature description here

  Scenario Outline: Verify Add Pet Functionality
    Given the Pet <petName> and <Status> need to be added to Library
    When we execute the AddPet PostAPI method
    Then verify required pet with <petName> and <Status> is successfully added
    And status code of response should be 200
    Examples:
      | petName | Status     |
      | 'tommy' | 'available'|
      | 'puppy' | 'Pending'  |

    @GETPetByPetID
    Scenario Outline: Verify the GetPet by petID API response
      Given the required petID <petID> pass as argument to url
      When we execute the GetPet get method
      Then verify the required PetDetails <petName> and <Status> appeared in response
      And status code of response should be 200
      Examples:
        | petID | petName | Status     |
        | 606   | petNme  | available  |

      @GETPetByStatus
      Scenario Outline: Verify the GetPet by Status API response
        Given the required status <Status> passed as argument to url
        When we execute the GetPet get method with reqired Parameter
        Then verify all the pets with <Status> appeared
        And status code of response should be 200
        Examples:
          | Status    |
          | available |
          | pending   |
          | sold      |

        @UpdatePet
      Scenario Outline: Update the required Pet Details by Pet Update API
        Given the required <petID>, <petName> and <status> passed as argument to API
        When we execute the Update API with required Parameters
        Then verify the updated <petID>, <petName> and <status> value appeared in response
        And status code of response should be 200
        Examples:
          | petID | petName | status |
          | 606   | tony    | sold   |