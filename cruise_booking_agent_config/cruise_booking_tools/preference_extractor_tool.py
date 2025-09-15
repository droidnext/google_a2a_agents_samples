"""
Preference Extractor Tool for extracting structured preferences from natural language.
"""
import re
from typing import Dict, Any, List, Optional


def preference_extractor_tool(user_input: str) -> Dict[str, Any]:
    """
    Extracts structured preferences from natural language input.
    
    Args:
        user_input: Natural language input from the user
    
    Returns:
        Dictionary containing extracted preferences
    """
    user_input = user_input.lower().strip()
    
    preferences = {
        "cruise_lines": [],
        "cabin_types": [],
        "budget_range": None,
        "activities": [],
        "destinations": [],
        "special_requirements": [],
        "party_size": None,
        "duration_preference": None
    }
    
    # Extract cruise line preferences
    cruise_lines = {
        'royal caribbean': ['royal caribbean', 'rcl', 'royal'],
        'carnival': ['carnival', 'ccl'],
        'norwegian': ['norwegian', 'ncl', 'norwegian cruise line'],
        'princess': ['princess', 'princess cruises'],
        'celebrity': ['celebrity', 'celebrity cruises'],
        'holland america': ['holland america', 'hal'],
        'disney': ['disney', 'disney cruise line', 'dcl'],
        'cunard': ['cunard', 'cunard line'],
        'virgin': ['virgin', 'virgin voyages']
    }
    
    for line, keywords in cruise_lines.items():
        if any(keyword in user_input for keyword in keywords):
            preferences["cruise_lines"].append(line)
    
    # Extract cabin type preferences
    cabin_types = {
        'interior': ['interior', 'inside', 'inside cabin'],
        'oceanview': ['oceanview', 'ocean view', 'outside', 'outside cabin'],
        'balcony': ['balcony', 'verandah', 'veranda'],
        'suite': ['suite', 'penthouse', 'villa'],
        'family': ['family', 'family cabin', 'family stateroom']
    }
    
    for cabin_type, keywords in cabin_types.items():
        if any(keyword in user_input for keyword in keywords):
            preferences["cabin_types"].append(cabin_type)
    
    # Extract budget information
    budget_patterns = [
        r'\$(\d+(?:,\d{3})*(?:\.\d{2})?)\s*(?:per person|pp|per person)',
        r'budget.*?\$(\d+(?:,\d{3})*(?:\.\d{2})?)',
        r'around\s*\$(\d+(?:,\d{3})*(?:\.\d{2})?)',
        r'under\s*\$(\d+(?:,\d{3})*(?:\.\d{2})?)',
        r'less than\s*\$(\d+(?:,\d{3})*(?:\.\d{2})?)',
        r'more than\s*\$(\d+(?:,\d{3})*(?:\.\d{2})?)',
        r'over\s*\$(\d+(?:,\d{3})*(?:\.\d{2})?)'
    ]
    
    for pattern in budget_patterns:
        match = re.search(pattern, user_input)
        if match:
            amount = float(match.group(1).replace(',', ''))
            if 'under' in user_input or 'less than' in user_input:
                preferences["budget_range"] = {"max": amount}
            elif 'over' in user_input or 'more than' in user_input:
                preferences["budget_range"] = {"min": amount}
            else:
                preferences["budget_range"] = {"target": amount}
            break
    
    # Extract activity preferences
    activities = {
        'dining': ['dining', 'food', 'restaurant', 'cuisine', 'chef', 'culinary'],
        'entertainment': ['entertainment', 'shows', 'music', 'comedy', 'theater', 'nightlife'],
        'wellness': ['spa', 'wellness', 'fitness', 'gym', 'yoga', 'massage', 'relaxation'],
        'adventure': ['adventure', 'excursions', 'shores', 'exploration', 'hiking', 'diving'],
        'family': ['family', 'kids', 'children', 'family-friendly', 'activities for kids'],
        'romance': ['romance', 'honeymoon', 'anniversary', 'couples', 'romantic'],
        'gambling': ['casino', 'gambling', 'poker', 'blackjack', 'slots'],
        'shopping': ['shopping', 'boutiques', 'stores', 'retail']
    }
    
    for activity, keywords in activities.items():
        if any(keyword in user_input for keyword in keywords):
            preferences["activities"].append(activity)
    
    # Extract destination preferences
    destinations = {
        'caribbean': ['caribbean', 'bahamas', 'jamaica', 'cozumel', 'st. thomas', 'st. maarten'],
        'mediterranean': ['mediterranean', 'europe', 'italy', 'greece', 'spain', 'france'],
        'alaska': ['alaska', 'alaskan', 'glacier', 'juneau', 'skagway'],
        'northern europe': ['northern europe', 'scandinavia', 'norway', 'iceland', 'baltic'],
        'asia': ['asia', 'japan', 'china', 'singapore', 'thailand', 'vietnam'],
        'australia': ['australia', 'new zealand', 'south pacific', 'tahiti'],
        'transatlantic': ['transatlantic', 'trans-atlantic', 'atlantic crossing'],
        'panama canal': ['panama canal', 'panama', 'canal']
    }
    
    for destination, keywords in destinations.items():
        if any(keyword in user_input for keyword in keywords):
            preferences["destinations"].append(destination)
    
    # Extract party size
    party_patterns = [
        r'(\d+)\s*(?:people|guests|adults|passengers)',
        r'party of\s*(\d+)',
        r'(\d+)\s*(?:couple|couples)',
        r'(\d+)\s*(?:family|families)'
    ]
    
    for pattern in party_patterns:
        match = re.search(pattern, user_input)
        if match:
            preferences["party_size"] = int(match.group(1))
            break
    
    # Extract duration preferences
    duration_patterns = [
        r'(\d+)\s*(?:day|days)',
        r'(\d+)\s*(?:week|weeks)',
        r'(\d+)\s*(?:night|nights)'
    ]
    
    for pattern in duration_patterns:
        match = re.search(pattern, user_input)
        if match:
            duration = int(match.group(1))
            if 'week' in user_input:
                preferences["duration_preference"] = f"{duration} weeks"
            elif 'night' in user_input:
                preferences["duration_preference"] = f"{duration} nights"
            else:
                preferences["duration_preference"] = f"{duration} days"
            break
    
    # Extract special requirements
    special_requirements = {
        'accessibility': ['wheelchair', 'accessible', 'disability', 'mobility'],
        'dietary': ['vegetarian', 'vegan', 'gluten-free', 'kosher', 'halal', 'allergies'],
        'pets': ['pet', 'dog', 'cat', 'animal'],
        'smoking': ['smoking', 'non-smoking', 'cigar'],
        'age_restrictions': ['adults only', '21+', '18+', 'senior', 'senior citizen']
    }
    
    for requirement, keywords in special_requirements.items():
        if any(keyword in user_input for keyword in keywords):
            preferences["special_requirements"].append(requirement)
    
    return preferences
