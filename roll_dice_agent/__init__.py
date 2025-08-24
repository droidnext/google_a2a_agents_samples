"""
Roll Dice Agent Package

A dice rolling game that finds prime numbers through sequential execution of specialized agents.
"""

from .root_agent import root_agent, roll_agent, prime_agent

__all__ = [
    'root_agent',
    'roll_agent', 
    'prime_agent'
]

__version__ = "1.0.0"
