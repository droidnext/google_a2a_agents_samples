# Cruise Booking Agent Configuration

This directory contains Google ADK Agent Config files for a comprehensive cruise booking system with multiple specialized agents.

## Overview

The cruise booking system consists of a root orchestrator agent and four specialized sub-agents that work together to provide a complete booking experience:

- **CruiseBookingOrchestrator**: Root agent that coordinates the entire booking flow
- **IntentUnderstandingAgent**: Welcomes guests and collects structured booking information
- **CruiseSearchAgent**: Searches for cruises, itineraries, cabins, and pricing
- **CruiseBookingAgent**: Finalizes bookings and offers add-ons
- **ExceptionHandlingAgent**: Handles errors and maintains conversational flow

## Files Structure

```
cruise_booking_agent_config/
├── root_agent.yaml                    # Main orchestrator agent
├── intent_understanding_agent.yaml    # Guest welcome and data collection
├── cruise_search_agent.yaml          # Cruise search and recommendations
├── cruise_booking_agent.yaml         # Booking finalization and add-ons
├── exception_handling_agent.yaml     # Error handling and recovery
├── cruise_booking_tools/             # Tool implementations
│   ├── __init__.py
│   ├── date_resolver_tool.py         # Normalizes time expressions
│   ├── preference_extractor_tool.py  # Extracts structured preferences
│   ├── cruise_semantic_search_api.py # Cruise search functionality
│   ├── cruise_package_api.py         # Cabin and pricing details
│   ├── cruise_booking_api.py         # Booking finalization
│   ├── calendar_api.py               # Sailing availability
│   ├── cruise_entitlements_api.py    # Add-ons and services
│   └── error_logger_tool.py          # Error monitoring
├── local.example_env                 # Environment configuration template
└── README.md                        # This file
```

## Setup

1. **Install Google ADK**:
   ```bash
   pip install google-adk
   ```

2. **Configure Environment**:
   ```bash
   cp local.example_env .env
   # Edit .env with your actual API keys and configuration
   ```

3. **Set up Google AI API**:
   - For Google AI Studio: Get an API key from [Google AI Studio](https://aistudio.google.com/)
   - For Vertex AI: Set up a Google Cloud project and enable Vertex AI

4. **Run the Agent**:
   ```bash
   # Web interface
   adk web
   
   # Terminal interface
   adk run
   
   # API server
   adk api_server
   ```

## Agent Workflow

1. **IntentUnderstandingAgent** greets the guest and collects:
   - Travel dates (using DateResolverTool)
   - Party size
   - Preferences (using PreferenceExtractorTool)

2. **CruiseSearchAgent** finds relevant options:
   - Uses CruiseSemanticSearchAPI for itinerary recommendations
   - Uses CruisePackageAPI for detailed cabin and pricing information

3. **CruiseBookingAgent** finalizes the booking:
   - Uses CruiseBookingAPI to create reservations
   - Uses CalendarAPI to confirm sailing dates
   - Uses CruiseEntitlementsAPI to offer add-ons

4. **ExceptionHandlingAgent** manages any errors:
   - Logs errors using ErrorLoggerTool
   - Provides fallback options
   - Maintains conversational flow

## Tools

The system includes comprehensive tools for:

- **Date Resolution**: Converts natural language time expressions to structured dates
- **Preference Extraction**: Extracts structured preferences from conversational input
- **Cruise Search**: Semantic search for relevant cruise options
- **Package Details**: Detailed cabin information and pricing
- **Booking Management**: Reservation creation and confirmation
- **Calendar Integration**: Sailing availability and scheduling
- **Entitlements**: Add-ons, excursions, and value-added services
- **Error Monitoring**: Comprehensive error logging and analysis

## Customization

Each agent can be customized by editing the corresponding YAML file:

- Modify `instruction` fields to change agent behavior
- Add or remove tools in the `tools` section
- Update `description` and `goals` to reflect your specific requirements

## Mock Data

The current implementation uses mock data for demonstration purposes. In a production environment, you would:

1. Replace mock API calls with real cruise booking APIs
2. Implement proper authentication and security
3. Add database integration for persistent storage
4. Set up proper error monitoring and alerting

## Known Limitations

- Currently uses mock data for cruise information
- Limited to Gemini models (as per ADK Agent Config limitations)
- Python-only tool implementations
- No real-time availability checking

## Next Steps

1. Integrate with real cruise booking APIs
2. Add user authentication and session management
3. Implement payment processing
4. Add real-time availability checking
5. Set up comprehensive monitoring and analytics
