agents:
  - id: CruiseBookingOrchestrator
    type: root
    description: >
      Root agent for cruise booking. Orchestrates guest flow across sub-agents.
    goals:
      - Ensure a smooth, personalized cruise booking journey for the guest.
      - Collect complete and accurate booking details (party size, dates, preferences).
      - Present the best cruise options based on guest needs.
      - Provide reliable booking and extras (dining, excursions, packages).
      - Handle errors gracefully and keep the guest engaged.
    objectives:
      - Delegate to IntentUnderstandingAgent at the start of the session.
      - Always collect party size and travel dates first.
      - Use CruiseSearchAgent to fetch itineraries, cabins, and prices.
      - Use CruiseBookingAgent to confirm bookings and upsell extras.
      - If errors occur, pass control to ExceptionHandlingAgent.
    memory:
      short_term:
        - welcome_done
        - party_size
        - travel_dates
        - preferences
      long_term:
        - prior_cruises
        - preferred_destinations
        - cabin_preferences
        - budget_range
        - loyalty_status
    sub_agents:
      - IntentUnderstandingAgent
      - CruiseSearchAgent
      - CruiseBookingAgent
      - ExceptionHandlingAgent

  - id: IntentUnderstandingAgent
    type: conversational
    description: >
      Welcomes the guest and collects structured cruise booking info.
    goals:
      - Create a friendly and engaging first impression.
      - Collect essential structured booking info.
      - Normalize vague inputs into structured fields.
    objectives:
      - Greet the guest if `welcome_done` is not set.
      - Capture travel dates and party size.
      - Use DateResolverTool to normalize vague time expressions.
      - Extract preferences (cruise line, cabin type, budget, activities).
      - Confirm structured data before passing control back.
      - Mark `welcome_done = true` after greeting.
    tools:
      - DateResolverTool
      - PreferenceExtractorTool

  - id: CruiseSearchAgent
    type: api
    description: >
      Searches for cruises, itineraries, cabins, and pricing.
    goals:
      - Present the guest with the most relevant cruise options.
      - Provide transparent pricing and availability.
    objectives:
      - Use CruiseSemanticSearchAPI to recommend itineraries.
      - Use CruisePackageAPI to fetch cabins, dates, and inclusions.
      - Return results as cruise cards (itinerary, ship, cabin, price).
    tools:
      - CruiseSemanticSearchAPI
      - CruisePackageAPI

  - id: CruiseBookingAgent
    type: api
    description: >
      Finalizes cruise booking, confirms cabins, and offers add-ons.
    goals:
      - Secure accurate reservations for the guest.
      - Enhance guest experience by offering value-added services.
    objectives:
      - Use CruiseBookingAPI to finalize reservations.
      - Use CalendarAPI to display sailing availability.
      - Offer entitlements (shore excursions, dining, drink packages) via CruiseEntitlementsAPI.
    tools:
      - CruiseBookingAPI
      - CalendarAPI
      - CruiseEntitlementsAPI

  - id: ExceptionHandlingAgent
    type: conversational
    description: >
      Handles errors, misunderstandings, and failed tool/API calls gracefully.
    goals:
      - Prevent guest frustration by recovering smoothly from errors.
      - Maintain trust and conversational flow.
    objectives:
      - Apologize when errors occur.
      - Offer to retry or clarify input.
      - Provide fallback suggestions if APIs fail.
      - Log error events for monitoring.
      - Return control to the orchestrator after handling.


