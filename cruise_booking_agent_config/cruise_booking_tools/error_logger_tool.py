"""
Error Logger Tool for logging and monitoring errors.
"""
from typing import Dict, Any, Optional
from datetime import datetime
import json


def error_logger_tool(
    error_type: str,
    error_message: str,
    agent_name: str,
    user_input: Optional[str] = None,
    context: Optional[Dict[str, Any]] = None,
    severity: str = "medium"
) -> Dict[str, Any]:
    """
    Log errors for monitoring and improvement.
    
    Args:
        error_type: Type of error (API_FAILURE, VALIDATION_ERROR, etc.)
        error_message: Detailed error message
        agent_name: Name of the agent that encountered the error
        user_input: User input that caused the error (optional)
        context: Additional context information (optional)
        severity: Error severity (low, medium, high, critical)
    
    Returns:
        Dictionary containing logging confirmation
    """
    # Mock implementation - in real scenario, this would log to actual monitoring system
    error_log = {
        "error_id": f"ERR_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "timestamp": datetime.now().isoformat(),
        "error_type": error_type,
        "error_message": error_message,
        "agent_name": agent_name,
        "user_input": user_input,
        "context": context or {},
        "severity": severity,
        "status": "logged"
    }
    
    # In a real implementation, this would be sent to a logging service
    print(f"ERROR LOGGED: {json.dumps(error_log, indent=2)}")
    
    return {
        "error_id": error_log["error_id"],
        "status": "logged",
        "timestamp": error_log["timestamp"],
        "message": "Error has been logged for monitoring and analysis"
    }


def get_error_summary(
    agent_name: Optional[str] = None,
    error_type: Optional[str] = None,
    hours_back: int = 24
) -> Dict[str, Any]:
    """
    Get a summary of recent errors for monitoring.
    
    Args:
        agent_name: Filter by specific agent (optional)
        error_type: Filter by error type (optional)
        hours_back: Number of hours to look back (default 24)
    
    Returns:
        Dictionary containing error summary
    """
    # Mock implementation - in real scenario, this would query actual logs
    mock_summary = {
        "summary_period": f"Last {hours_back} hours",
        "total_errors": 15,
        "errors_by_agent": {
            "IntentUnderstandingAgent": 3,
            "CruiseSearchAgent": 7,
            "CruiseBookingAgent": 4,
            "ExceptionHandlingAgent": 1
        },
        "errors_by_type": {
            "API_FAILURE": 8,
            "VALIDATION_ERROR": 4,
            "TIMEOUT_ERROR": 2,
            "SYSTEM_ERROR": 1
        },
        "errors_by_severity": {
            "low": 5,
            "medium": 8,
            "high": 2,
            "critical": 0
        },
        "recent_errors": [
            {
                "error_id": "ERR_20240115_103000",
                "timestamp": "2024-01-15T10:30:00Z",
                "agent_name": "CruiseSearchAgent",
                "error_type": "API_FAILURE",
                "error_message": "Cruise search API timeout",
                "severity": "medium"
            },
            {
                "error_id": "ERR_20240115_102500",
                "timestamp": "2024-01-15T10:25:00Z",
                "agent_name": "CruiseBookingAgent",
                "error_type": "VALIDATION_ERROR",
                "error_message": "Invalid passenger information format",
                "severity": "low"
            }
        ],
        "recommendations": [
            "Monitor API response times for CruiseSearchAgent",
            "Improve input validation for passenger information",
            "Consider implementing retry logic for API calls"
        ]
    }
    
    return mock_summary
