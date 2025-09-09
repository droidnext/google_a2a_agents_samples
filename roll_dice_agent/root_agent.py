# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.genai import types


# --- Roll Die Sub-Agent ---
def roll_dice() -> int:
  """Roll a die and return the rolled result."""
  return random.randint(1, 6)


roll_agent = LlmAgent(
    name="roll_agent",
    description="A dice rolling agent that finds prime numbers through parallel execution of specialized sub-agents.",
    model="gemini-2.0-flash",
    instruction="""
  You are a dice rolling game coordinator. When the user types "roll":
  1. Call dice_agent to get a number
  2. Call check_prime_agent with that number
  3. If prime, show "The number [number] is prime!"
  4. If not prime, show "The number [number] is not prime. Roll again!"
  
  You have access to dice_agent and check_prime_agent. Use them.

    """,
    tools=[roll_dice],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  # avoid false alarm about rolling dice.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)


def check_prime(num: int) -> str:
  """Check if a given number is prime."""
  number = int(num)
  if number <= 1:
    return f"The number {number} is not prime."
  
  is_prime = True
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      is_prime = False
      break
  
  if is_prime:
    return f"The number {number} is prime!"
  else:
    return f"The number {number} is not prime. Roll again!"


prime_agent = LlmAgent(
    name="prime_agent",
    description="A specialized agent that determines whether a given number is prime.",
    model="gemini-2.0-flash",
    instruction="""
You are a prime number checking agent that determines if a given number is prime.
    """,
    tools=[check_prime],
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(  # avoid false alarm about rolling dice.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)

root_agent = SequentialAgent(
    name="simple_sequential_agent",
    sub_agents=[roll_agent, prime_agent],
    # The agents will run in the order provided: roll_agent -> prime_agent
)
