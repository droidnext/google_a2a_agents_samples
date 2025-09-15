"""
Cruise Semantic Search API Tool for finding relevant cruise itineraries.
"""
from typing import Dict, Any, List, Optional
import json


def cruise_semantic_search_api(
    destinations: Optional[List[str]] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    party_size: Optional[int] = None,
    budget_range: Optional[Dict[str, float]] = None,
    cruise_lines: Optional[List[str]] = None,
    activities: Optional[List[str]] = None,
    duration_preference: Optional[str] = None
) -> Dict[str, Any]:
    """
    Search for cruise itineraries based on semantic criteria.
    
    Args:
        destinations: List of preferred destinations
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        party_size: Number of passengers
        budget_range: Budget constraints (min, max, target)
        cruise_lines: Preferred cruise lines
        activities: Preferred activities
        duration_preference: Preferred cruise duration
    
    Returns:
        Dictionary containing search results
    """
    # Mock implementation - in real scenario, this would call actual cruise APIs
    mock_results = [
        {
            "itinerary_id": "CAR001",
            "title": "7-Night Eastern Caribbean",
            "cruise_line": "Royal Caribbean",
            "ship": "Symphony of the Seas",
            "departure_port": "Miami, Florida",
            "ports": ["Nassau, Bahamas", "St. Thomas, USVI", "St. Maarten"],
            "duration": "7 nights",
            "departure_date": "2024-06-15",
            "return_date": "2024-06-22",
            "starting_price": 899.00,
            "currency": "USD",
            "availability": "Available",
            "highlights": ["Largest cruise ship", "Broadway shows", "Water slides", "Fine dining"],
            "amenities": ["WiFi", "Gym", "Spa", "Casino", "Multiple restaurants"],
            "cabin_types": ["Interior", "Oceanview", "Balcony", "Suite"]
        },
        {
            "itinerary_id": "MED002",
            "title": "10-Night Mediterranean Explorer",
            "cruise_line": "Celebrity Cruises",
            "ship": "Celebrity Edge",
            "departure_port": "Barcelona, Spain",
            "ports": ["Rome, Italy", "Santorini, Greece", "Mykonos, Greece", "Naples, Italy"],
            "duration": "10 nights",
            "departure_date": "2024-07-20",
            "return_date": "2024-07-30",
            "starting_price": 1299.00,
            "currency": "USD",
            "availability": "Available",
            "highlights": ["Modern luxury", "Michelin-starred dining", "Art collection", "Rooftop garden"],
            "amenities": ["WiFi", "Spa", "Fine dining", "Art gallery", "Rooftop terrace"],
            "cabin_types": ["Interior", "Oceanview", "Balcony", "Suite"]
        },
        {
            "itinerary_id": "ALASKA003",
            "title": "7-Night Alaska Glacier Discovery",
            "cruise_line": "Princess Cruises",
            "ship": "Royal Princess",
            "departure_port": "Seattle, Washington",
            "ports": ["Juneau, Alaska", "Skagway, Alaska", "Glacier Bay", "Ketchikan, Alaska"],
            "duration": "7 nights",
            "departure_date": "2024-08-10",
            "return_date": "2024-08-17",
            "starting_price": 1099.00,
            "currency": "USD",
            "availability": "Available",
            "highlights": ["Glacier viewing", "Wildlife spotting", "Scenic cruising", "Alaska culture"],
            "amenities": ["WiFi", "Naturalist talks", "Observation deck", "Alaska cuisine"],
            "cabin_types": ["Interior", "Oceanview", "Balcony", "Suite"]
        }
    ]
    
    # Filter results based on criteria
    filtered_results = []
    
    for result in mock_results:
        include_result = True
        
        # Filter by destinations
        if destinations:
            result_destinations = [port.split(',')[1].strip() for port in result["ports"]]
            if not any(dest.lower() in [d.lower() for d in destinations] for dest in result_destinations):
                include_result = False
        
        # Filter by cruise lines
        if cruise_lines:
            if not any(line.lower() in result["cruise_line"].lower() for line in cruise_lines):
                include_result = False
        
        # Filter by budget
        if budget_range:
            price = result["starting_price"]
            if "min" in budget_range and price < budget_range["min"]:
                include_result = False
            if "max" in budget_range and price > budget_range["max"]:
                include_result = False
            if "target" in budget_range and abs(price - budget_range["target"]) > budget_range["target"] * 0.2:
                include_result = False
        
        # Filter by duration
        if duration_preference:
            if "week" in duration_preference:
                weeks = int(duration_preference.split()[0])
                if result["duration"] != f"{weeks * 7} nights":
                    include_result = False
        
        if include_result:
            filtered_results.append(result)
    
    return {
        "search_criteria": {
            "destinations": destinations,
            "start_date": start_date,
            "end_date": end_date,
            "party_size": party_size,
            "budget_range": budget_range,
            "cruise_lines": cruise_lines,
            "activities": activities,
            "duration_preference": duration_preference
        },
        "results": filtered_results,
        "total_results": len(filtered_results),
        "search_timestamp": "2024-01-15T10:30:00Z"
    }
