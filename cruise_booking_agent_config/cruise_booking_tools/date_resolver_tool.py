"""
Date Resolver Tool for normalizing vague time expressions into structured dates.
"""
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import re


def date_resolver_tool(time_expression: str, reference_date: Optional[str] = None) -> Dict[str, Any]:
    """
    Resolves vague time expressions into structured date information.
    
    Args:
        time_expression: Natural language time expression (e.g., "next summer", "in 3 months")
        reference_date: Reference date in YYYY-MM-DD format (defaults to today)
    
    Returns:
        Dictionary containing structured date information
    """
    if reference_date:
        ref_date = datetime.strptime(reference_date, "%Y-%m-%d")
    else:
        ref_date = datetime.now()
    
    time_expression = time_expression.lower().strip()
    
    # Handle "next" expressions
    if "next summer" in time_expression:
        # Find next summer (June-August)
        current_year = ref_date.year
        if ref_date.month >= 6:
            current_year += 1
        return {
            "start_date": f"{current_year}-06-01",
            "end_date": f"{current_year}-08-31",
            "season": "summer",
            "confidence": 0.9
        }
    
    elif "next winter" in time_expression:
        # Find next winter (December-February)
        current_year = ref_date.year
        if ref_date.month >= 12:
            current_year += 1
        return {
            "start_date": f"{current_year}-12-01",
            "end_date": f"{current_year + 1}-02-28",
            "season": "winter",
            "confidence": 0.9
        }
    
    elif "next spring" in time_expression:
        # Find next spring (March-May)
        current_year = ref_date.year
        if ref_date.month >= 3:
            current_year += 1
        return {
            "start_date": f"{current_year}-03-01",
            "end_date": f"{current_year}-05-31",
            "season": "spring",
            "confidence": 0.9
        }
    
    elif "next fall" in time_expression or "next autumn" in time_expression:
        # Find next fall (September-November)
        current_year = ref_date.year
        if ref_date.month >= 9:
            current_year += 1
        return {
            "start_date": f"{current_year}-09-01",
            "end_date": f"{current_year}-11-30",
            "season": "fall",
            "confidence": 0.9
        }
    
    # Handle "in X months" expressions
    months_match = re.search(r'in (\d+) months?', time_expression)
    if months_match:
        months = int(months_match.group(1))
        target_date = ref_date + timedelta(days=months * 30)  # Approximate
        return {
            "start_date": target_date.strftime("%Y-%m-%d"),
            "end_date": (target_date + timedelta(days=30)).strftime("%Y-%m-%d"),
            "months_ahead": months,
            "confidence": 0.8
        }
    
    # Handle "in X weeks" expressions
    weeks_match = re.search(r'in (\d+) weeks?', time_expression)
    if weeks_match:
        weeks = int(weeks_match.group(1))
        target_date = ref_date + timedelta(weeks=weeks)
        return {
            "start_date": target_date.strftime("%Y-%m-%d"),
            "end_date": (target_date + timedelta(days=7)).strftime("%Y-%m-%d"),
            "weeks_ahead": weeks,
            "confidence": 0.8
        }
    
    # Handle specific month mentions
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    
    for month_name, month_num in months.items():
        if month_name in time_expression:
            current_year = ref_date.year
            if ref_date.month > month_num:
                current_year += 1
            
            # Get the last day of the month
            if month_num == 12:
                next_month = 1
                next_year = current_year + 1
            else:
                next_month = month_num + 1
                next_year = current_year
            
            last_day = (datetime(next_year, next_month, 1) - timedelta(days=1)).day
            
            return {
                "start_date": f"{current_year}-{month_num:02d}-01",
                "end_date": f"{current_year}-{month_num:02d}-{last_day}",
                "month": month_name,
                "confidence": 0.7
            }
    
    # Default fallback
    return {
        "start_date": ref_date.strftime("%Y-%m-%d"),
        "end_date": (ref_date + timedelta(days=30)).strftime("%Y-%m-%d"),
        "confidence": 0.3,
        "note": "Could not parse specific date, using approximate range"
    }
