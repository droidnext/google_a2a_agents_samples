"""
Cruise Entitlements API Tool for offering add-ons and value-added services.
"""
from typing import Dict, Any, List, Optional


def cruise_entitlements_api(
    itinerary_id: str,
    cabin_type: str,
    passenger_count: int,
    preferences: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Get available entitlements and add-ons for a cruise booking.
    
    Args:
        itinerary_id: ID of the cruise itinerary
        cabin_type: Type of cabin booked
        passenger_count: Number of passengers
        preferences: List of preferred activity types
    
    Returns:
        Dictionary containing available entitlements
    """
    # Mock implementation - in real scenario, this would call actual entitlements APIs
    mock_entitlements = {
        "dining_packages": [
            {
                "package_id": "DINE001",
                "name": "Specialty Dining Package",
                "description": "3-night specialty dining package",
                "price_per_person": 89.00,
                "includes": [
                    "Choice of 3 specialty restaurants",
                    "Priority reservations",
                    "Complimentary wine pairing"
                ],
                "restaurants": ["Chops Grille", "Izumi", "150 Central Park"],
                "availability": "Available"
            },
            {
                "package_id": "DINE002",
                "name": "Ultimate Dining Package",
                "description": "Unlimited specialty dining",
                "price_per_person": 199.00,
                "includes": [
                    "Unlimited specialty dining",
                    "Priority reservations",
                    "Complimentary beverages"
                ],
                "restaurants": ["All specialty restaurants"],
                "availability": "Available"
            }
        ],
        "beverage_packages": [
            {
                "package_id": "BEV001",
                "name": "Classic Beverage Package",
                "description": "Unlimited alcoholic and non-alcoholic beverages",
                "price_per_person": 65.00,
                "includes": [
                    "Unlimited cocktails, wine, beer",
                    "Premium coffee and tea",
                    "Fresh juices and sodas",
                    "Bottled water"
                ],
                "restrictions": "Must be purchased for all adults in cabin",
                "availability": "Available"
            },
            {
                "package_id": "BEV002",
                "name": "Premium Beverage Package",
                "description": "Premium alcoholic and non-alcoholic beverages",
                "price_per_person": 89.00,
                "includes": [
                    "Premium spirits and cocktails",
                    "Premium wines",
                    "Specialty coffee drinks",
                    "Fresh juices and sodas",
                    "Bottled water"
                ],
                "restrictions": "Must be purchased for all adults in cabin",
                "availability": "Available"
            }
        ],
        "excursions": [
            {
                "excursion_id": "EXC001",
                "name": "Nassau City Tour & Beach Break",
                "port": "Nassau, Bahamas",
                "duration": "4 hours",
                "price_per_person": 79.00,
                "description": "Explore historic Nassau and relax at Cable Beach",
                "includes": ["Transportation", "Guide", "Beach access", "Lunch"],
                "difficulty": "Easy",
                "availability": "Available"
            },
            {
                "excursion_id": "EXC002",
                "name": "St. Thomas Island Drive & Shopping",
                "port": "St. Thomas, USVI",
                "duration": "3 hours",
                "price_per_person": 59.00,
                "description": "Scenic island tour with shopping time",
                "includes": ["Transportation", "Guide", "Shopping time"],
                "difficulty": "Easy",
                "availability": "Available"
            },
            {
                "excursion_id": "EXC003",
                "name": "St. Maarten Beach & Snorkeling",
                "port": "St. Maarten",
                "duration": "5 hours",
                "price_per_person": 99.00,
                "description": "Beach day with snorkeling equipment",
                "includes": ["Transportation", "Snorkeling gear", "Beach access", "Lunch"],
                "difficulty": "Moderate",
                "availability": "Available"
            }
        ],
        "spa_services": [
            {
                "service_id": "SPA001",
                "name": "Couples Massage Package",
                "description": "60-minute couples massage",
                "price_per_couple": 299.00,
                "duration": "60 minutes",
                "includes": ["Couples massage", "Champagne", "Chocolates"],
                "availability": "Available"
            },
            {
                "service_id": "SPA002",
                "name": "Spa Day Pass",
                "description": "Full day access to spa facilities",
                "price_per_person": 89.00,
                "duration": "Full day",
                "includes": ["Thermal suite access", "Sauna", "Steam room", "Relaxation area"],
                "availability": "Available"
            }
        ],
        "internet_packages": [
            {
                "package_id": "WIFI001",
                "name": "Basic Internet Package",
                "description": "Basic internet access for email and browsing",
                "price_per_person": 15.00,
                "speed": "Basic",
                "devices": 1,
                "availability": "Available"
            },
            {
                "package_id": "WIFI002",
                "name": "Premium Internet Package",
                "description": "High-speed internet for streaming and video calls",
                "price_per_person": 25.00,
                "speed": "Premium",
                "devices": 2,
                "availability": "Available"
            }
        ],
        "photo_packages": [
            {
                "package_id": "PHOTO001",
                "name": "Digital Photo Package",
                "description": "All digital photos from your cruise",
                "price_per_cabin": 199.00,
                "includes": ["All digital photos", "USB drive", "Online gallery access"],
                "availability": "Available"
            }
        ]
    }
    
    # Filter entitlements based on preferences
    filtered_entitlements = {}
    
    for category, items in mock_entitlements.items():
        if preferences:
            # Simple filtering based on category names
            if any(pref.lower() in category.lower() for pref in preferences):
                filtered_entitlements[category] = items
        else:
            filtered_entitlements[category] = items
    
    # Add cabin-specific recommendations
    cabin_recommendations = {
        "Suite": [
            "Priority reservations for all services",
            "Complimentary specialty dining",
            "Concierge service",
            "Priority boarding and disembarkation"
        ],
        "Balcony": [
            "Private balcony dining",
            "Room service on balcony",
            "Priority excursion booking"
        ],
        "Oceanview": [
            "Window dining experience",
            "Priority spa booking"
        ],
        "Interior": [
            "Public area recommendations",
            "Entertainment package upgrades"
        ]
    }
    
    return {
        "itinerary_id": itinerary_id,
        "cabin_type": cabin_type,
        "passenger_count": passenger_count,
        "entitlements": filtered_entitlements,
        "cabin_recommendations": cabin_recommendations.get(cabin_type, []),
        "total_categories": len(filtered_entitlements),
        "search_timestamp": "2024-01-15T10:30:00Z"
    }


def book_entitlement(
    itinerary_id: str,
    entitlement_id: str,
    passenger_count: int,
    special_requests: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Book a specific entitlement or add-on.
    
    Args:
        itinerary_id: ID of the cruise itinerary
        entitlement_id: ID of the entitlement to book
        passenger_count: Number of passengers
        special_requests: List of special requests
    
    Returns:
        Dictionary containing booking confirmation
    """
    # Mock implementation
    return {
        "booking_id": f"ENT{entitlement_id}",
        "itinerary_id": itinerary_id,
        "entitlement_id": entitlement_id,
        "passenger_count": passenger_count,
        "special_requests": special_requests or [],
        "booking_status": "Confirmed",
        "confirmation_number": f"ENT{entitlement_id}",
        "booking_date": "2024-01-15T10:30:00Z",
        "next_steps": [
            "Confirmation will be sent via email",
            "Entitlement will be added to your cruise account",
            "Present confirmation at service location"
        ]
    }
