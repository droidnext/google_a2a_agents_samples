"""
Cruise Package API Tool for fetching detailed cabin information and pricing.
"""
from typing import Dict, Any, List, Optional


def cruise_package_api(
    itinerary_id: str,
    cabin_types: Optional[List[str]] = None,
    party_size: Optional[int] = None
) -> Dict[str, Any]:
    """
    Fetch detailed cabin information, pricing, and inclusions for a specific itinerary.
    
    Args:
        itinerary_id: ID of the cruise itinerary
        cabin_types: List of preferred cabin types
        party_size: Number of passengers
    
    Returns:
        Dictionary containing detailed package information
    """
    # Mock implementation - in real scenario, this would call actual cruise APIs
    mock_packages = {
        "CAR001": {
            "itinerary_id": "CAR001",
            "title": "7-Night Eastern Caribbean",
            "cruise_line": "Royal Caribbean",
            "ship": "Symphony of the Seas",
            "departure_date": "2024-06-15",
            "return_date": "2024-06-22",
            "cabin_options": [
                {
                    "cabin_type": "Interior",
                    "cabin_code": "INT",
                    "description": "Cozy interior stateroom with twin beds",
                    "size": "149 sq ft",
                    "occupancy": "Up to 4 guests",
                    "amenities": ["TV", "Phone", "Private bathroom", "Air conditioning"],
                    "price_per_person": 899.00,
                    "total_price": 1798.00,
                    "availability": "Available",
                    "deck": "Deck 3-8"
                },
                {
                    "cabin_type": "Oceanview",
                    "cabin_code": "OV",
                    "description": "Stateroom with ocean view window",
                    "size": "179 sq ft",
                    "occupancy": "Up to 4 guests",
                    "amenities": ["Ocean view window", "TV", "Phone", "Private bathroom", "Air conditioning"],
                    "price_per_person": 1099.00,
                    "total_price": 2198.00,
                    "availability": "Available",
                    "deck": "Deck 2-7"
                },
                {
                    "cabin_type": "Balcony",
                    "cabin_code": "BAL",
                    "description": "Stateroom with private balcony",
                    "size": "182 sq ft + 50 sq ft balcony",
                    "occupancy": "Up to 4 guests",
                    "amenities": ["Private balcony", "Ocean view", "TV", "Phone", "Private bathroom", "Air conditioning"],
                    "price_per_person": 1299.00,
                    "total_price": 2598.00,
                    "availability": "Available",
                    "deck": "Deck 6-14"
                },
                {
                    "cabin_type": "Suite",
                    "cabin_code": "SUITE",
                    "description": "Luxury suite with concierge service",
                    "size": "300 sq ft + 100 sq ft balcony",
                    "occupancy": "Up to 4 guests",
                    "amenities": ["Private balcony", "Concierge service", "Priority boarding", "Complimentary specialty dining", "WiFi", "TV", "Phone", "Private bathroom", "Air conditioning"],
                    "price_per_person": 2199.00,
                    "total_price": 4398.00,
                    "availability": "Available",
                    "deck": "Deck 10-14"
                }
            ],
            "inclusions": [
                "All meals in main dining rooms",
                "Room service (limited hours)",
                "Entertainment shows",
                "Fitness center access",
                "Pool and hot tub access",
                "Kids' programs",
                "Port taxes and fees"
            ],
            "exclusions": [
                "Alcoholic beverages",
                "Specialty dining",
                "Spa services",
                "Shore excursions",
                "WiFi (except suites)",
                "Gratuities"
            ]
        },
        "MED002": {
            "itinerary_id": "MED002",
            "title": "10-Night Mediterranean Explorer",
            "cruise_line": "Celebrity Cruises",
            "ship": "Celebrity Edge",
            "departure_date": "2024-07-20",
            "return_date": "2024-07-30",
            "cabin_options": [
                {
                    "cabin_type": "Interior",
                    "cabin_code": "INT",
                    "description": "Modern interior stateroom",
                    "size": "200 sq ft",
                    "occupancy": "Up to 2 guests",
                    "amenities": ["TV", "Phone", "Private bathroom", "Air conditioning", "WiFi"],
                    "price_per_person": 1299.00,
                    "total_price": 2598.00,
                    "availability": "Available",
                    "deck": "Deck 3-6"
                },
                {
                    "cabin_type": "Oceanview",
                    "cabin_code": "OV",
                    "description": "Stateroom with ocean view window",
                    "size": "200 sq ft",
                    "occupancy": "Up to 2 guests",
                    "amenities": ["Ocean view window", "TV", "Phone", "Private bathroom", "Air conditioning", "WiFi"],
                    "price_per_person": 1499.00,
                    "total_price": 2998.00,
                    "availability": "Available",
                    "deck": "Deck 3-6"
                },
                {
                    "cabin_type": "Balcony",
                    "cabin_code": "BAL",
                    "description": "Infinite veranda stateroom",
                    "size": "200 sq ft + infinite veranda",
                    "occupancy": "Up to 2 guests",
                    "amenities": ["Infinite veranda", "Ocean view", "TV", "Phone", "Private bathroom", "Air conditioning", "WiFi"],
                    "price_per_person": 1799.00,
                    "total_price": 3598.00,
                    "availability": "Available",
                    "deck": "Deck 6-12"
                },
                {
                    "cabin_type": "Suite",
                    "cabin_code": "SUITE",
                    "description": "Luxury suite with butler service",
                    "size": "400 sq ft + 100 sq ft veranda",
                    "occupancy": "Up to 4 guests",
                    "amenities": ["Private veranda", "Butler service", "Priority boarding", "Complimentary specialty dining", "WiFi", "TV", "Phone", "Private bathroom", "Air conditioning", "Mini bar"],
                    "price_per_person": 2999.00,
                    "total_price": 5998.00,
                    "availability": "Available",
                    "deck": "Deck 10-12"
                }
            ],
            "inclusions": [
                "All meals in main dining rooms",
                "Room service",
                "Entertainment shows",
                "Fitness center access",
                "Pool and hot tub access",
                "WiFi",
                "Port taxes and fees"
            ],
            "exclusions": [
                "Alcoholic beverages",
                "Specialty dining",
                "Spa services",
                "Shore excursions",
                "Gratuities"
            ]
        }
    }
    
    if itinerary_id not in mock_packages:
        return {
            "error": "Itinerary not found",
            "itinerary_id": itinerary_id
        }
    
    package = mock_packages[itinerary_id]
    
    # Filter cabin options based on preferences
    if cabin_types:
        filtered_cabins = [
            cabin for cabin in package["cabin_options"]
            if cabin["cabin_type"].lower() in [ct.lower() for ct in cabin_types]
        ]
    else:
        filtered_cabins = package["cabin_options"]
    
    return {
        "itinerary_id": itinerary_id,
        "title": package["title"],
        "cruise_line": package["cruise_line"],
        "ship": package["ship"],
        "departure_date": package["departure_date"],
        "return_date": package["return_date"],
        "cabin_options": filtered_cabins,
        "inclusions": package["inclusions"],
        "exclusions": package["exclusions"],
        "total_cabin_options": len(filtered_cabins),
        "search_timestamp": "2024-01-15T10:30:00Z"
    }
