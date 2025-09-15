"""
Cruise Booking API Tool for finalizing reservations.
"""
from typing import Dict, Any, List, Optional
import uuid
from datetime import datetime


def cruise_booking_api(
    itinerary_id: str,
    cabin_code: str,
    passenger_details: List[Dict[str, Any]],
    contact_info: Dict[str, str],
    special_requests: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Finalize cruise booking and create reservation.
    
    Args:
        itinerary_id: ID of the cruise itinerary
        cabin_code: Code of the selected cabin
        passenger_details: List of passenger information
        contact_info: Contact information for the booking
        special_requests: List of special requests
    
    Returns:
        Dictionary containing booking confirmation
    """
    # Mock implementation - in real scenario, this would call actual booking APIs
    booking_id = str(uuid.uuid4())
    confirmation_number = f"CRU{booking_id[:8].upper()}"
    
    # Mock pricing calculation
    base_prices = {
        "INT": 899.00,
        "OV": 1099.00,
        "BAL": 1299.00,
        "SUITE": 2199.00
    }
    
    base_price = base_prices.get(cabin_code, 899.00)
    total_passengers = len(passenger_details)
    subtotal = base_price * total_passengers
    
    # Calculate taxes and fees (mock)
    taxes_fees = subtotal * 0.15  # 15% taxes and fees
    gratuities = subtotal * 0.10  # 10% gratuities
    total_amount = subtotal + taxes_fees + gratuities
    
    booking_details = {
        "booking_id": booking_id,
        "confirmation_number": confirmation_number,
        "itinerary_id": itinerary_id,
        "cabin_code": cabin_code,
        "passenger_count": total_passengers,
        "passenger_details": passenger_details,
        "contact_info": contact_info,
        "special_requests": special_requests or [],
        "pricing": {
            "base_price_per_person": base_price,
            "subtotal": subtotal,
            "taxes_and_fees": taxes_fees,
            "gratuities": gratuities,
            "total_amount": total_amount,
            "currency": "USD"
        },
        "booking_status": "Confirmed",
        "booking_date": datetime.now().isoformat(),
        "payment_due_date": "2024-02-15",
        "cancellation_policy": "Full refund if cancelled 90+ days before departure",
        "next_steps": [
            "Complete online check-in 30 days before departure",
            "Download cruise line mobile app",
            "Review excursion options",
            "Consider travel insurance"
        ]
    }
    
    return booking_details


def get_booking_status(confirmation_number: str) -> Dict[str, Any]:
    """
    Get the current status of a booking.
    
    Args:
        confirmation_number: Booking confirmation number
    
    Returns:
        Dictionary containing booking status
    """
    # Mock implementation
    return {
        "confirmation_number": confirmation_number,
        "booking_status": "Confirmed",
        "last_updated": datetime.now().isoformat(),
        "check_in_available": True,
        "excursion_booking_available": True,
        "specialty_dining_available": True
    }
