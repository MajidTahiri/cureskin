# Created by majidtahiri at 7/13/23
Feature: Search results filter can be cleared

  @smoke
#Scenario: Clear search results filter
#  Given the search results page is open
#  When user clicks 'More Filters'
#  And select 'Face Wash' filter
#  And click 'Apply' button
#  Then verify filter is set and 'Face Wash' appears under filters
#  When user clicks 'Clear all'
#  Then verify filter is removed



  Scenario: Clear search results filter on mobile devices
    Given the search results page is open
    When user taps 'Filter and Sort'
    And tap 'Product type'
    And navigate to the target page
    When user taps 'Clear all'
    Then verify filter is removed