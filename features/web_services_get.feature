Feature: Get weather on Pune

  Scenario: Get weather on Pune
     Given that user  have a web services API for weather
      When user sends a request to get weather details
      Then system return a success code and weather information