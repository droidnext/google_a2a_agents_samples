# Roll Dice Agent - Python Implementation

This folder contains a Python implementation of the dice rolling game using the Google ADK Python library with proper tool-based agents and SequentialAgent.

## Architecture

The system consists of three main components:

### 1. **roll_agent** (LlmAgent with Tools)
- **Purpose**: Handles rolling dice of different sizes using the `roll_dice` tool
- **Class**: `LlmAgent` with tools
- **Tool**: `roll_dice(sides: int)` - Returns random number from 1 to sides
- **Model**: gemini-2.0-flash

### 2. **prime_agent** (LlmAgent with Tools)
- **Purpose**: Checks if numbers are prime using the `check_prime` tool
- **Class**: `LlmAgent` with tools
- **Tool**: `check_prime(nums: list[int])` - Returns prime number results
- **Model**: gemini-2.0-flash

### 3. **root_agent** (SequentialAgent)
- **Purpose**: Coordinates the workflow execution
- **Class**: `SequentialAgent`
- **Workflow**: roll_agent → prime_agent (executed in sequence)

## Key Features

✅ **Tool-based Agents**: Uses proper tools for dice rolling and prime checking  
✅ **SequentialAgent Support**: Guaranteed sequential execution of sub-agents  
✅ **Safety Settings**: Configured to avoid false alarms about dice rolling  
✅ **Proper ADK Imports**: Uses correct import paths for the ADK library  
✅ **Apache License**: Properly licensed code  

## How It Works

1. **User Input**: User provides input to the root agent
2. **Sequential Execution**: 
   - First: `roll_agent` executes with dice rolling tools
   - Second: `prime_agent` executes with prime checking tools
3. **Result**: Combined output from both agents

## Tools

### `roll_die(sides: int) -> int`
- Rolls a die with specified number of sides
- Returns random integer from 1 to sides
- Used by roll_agent for dice rolling operations

### `check_prime(nums: list[int]) -> str`
- Checks if numbers in the list are prime
- Returns formatted string with prime number results
- Used by prime_agent for prime number validation

## Usage

### Running the Test

```bash
cd roll_dice_agent
pip install -r requirements.txt
python test_agents.py
```

### Using in Your Code

```python
from roll_dice_agent import root_agent, roll_agent, prime_agent

# Use the sequential agent
result = await root_agent.run("roll a 6-sided die")

# Use individual agents
dice_result = await roll_agent.run("roll a 6-sided die")
prime_result = await prime_agent.run("check if 7 is prime")
```

## Dependencies

- `google-adk-python>=1.12.0` - Google ADK Python library
- `google-genai>=0.3.0` - Google Generative AI library
- `python-dotenv>=1.0.0` - Environment variable loading

## File Structure

```
roll_dice_agent/
├── __init__.py           # Package initialization
├── root_agent.py         # Main agents and SequentialAgent
├── test_agents.py        # Test script
├── requirements.txt      # Dependencies
└── README.md             # This file
```

## Safety Configuration

The agents include safety settings to avoid false alarms about dice rolling:
- `HARM_CATEGORY_DANGEROUS_CONTENT` is set to `OFF`
- This prevents the model from flagging dice rolling as dangerous content

## Next Steps

This implementation provides a solid foundation for:
- Building more complex agent workflows
- Adding additional tools and capabilities
- Integrating with other Google AI services
- Creating production-ready agent systems
