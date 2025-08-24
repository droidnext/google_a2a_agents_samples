# Capitals and Flags Agent Configuration

This folder contains agent configurations for answering questions about country capitals and flags, similar to the multi-agent basic configuration structure.

## Agent Architecture

The system consists of three specialized agents working together:

### 1. **capital_agent** (`capital_agent.yaml`)
- **Purpose**: Provides information about country capitals and capital cities
- **Expertise**: Capital cities, population, location, historical significance
- **Capabilities**:
  - Identify country capitals
  - Provide capital city facts and trivia
  - Compare capitals between countries
  - Answer questions about specific cities

### 2. **flag_agent** (`flag_agent.yaml`)
- **Purpose**: Provides information about country flags and their meanings
- **Expertise**: Flag designs, colors, symbols, historical significance
- **Capabilities**:
  - Describe flag designs and patterns
  - Explain symbolic meanings of flag elements
  - Provide flag history and adoption dates
  - Share cultural significance of flags

### 3. **root_agent** (`root_agent.yaml`)
- **Purpose**: Coordinates and delegates questions to appropriate specialized agents
- **Role**: Question routing and response coordination
- **Workflow**:
  - Analyzes user questions
  - Routes to appropriate agent(s)
  - Combines information for comprehensive answers
  - Presents organized responses

## Question Types and Routing

### **Capital Questions** → `capital_agent`
- "What is the capital of France?"
- "Is Tokyo a capital city?"
- "Tell me about the capital of Brazil"

### **Flag Questions** → `flag_agent`
- "What does the American flag look like?"
- "What do the colors of the French flag mean?"
- "Describe the flag of Japan"

### **Combined Questions** → Both agents
- "Tell me about France - its capital and flag"
- "Compare Germany and Italy - capitals and flags"
- "What are the capitals and flags of Nordic countries?"

## Configuration Files

- **`capital_agent.yaml`** - Capital cities expert agent configuration
- **`flag_agent.yaml`** - Flag expert agent configuration  
- **`root_agent.yaml`** - Main coordination agent configuration
- **`README.md`** - This documentation file

## Usage Examples

### Single Topic Questions
```
User: "What is the capital of Japan?"
Root Agent: Routes to capital_agent
Response: "The capital of Japan is Tokyo, located on the island of Honshu..."
```

### Flag Questions
```
User: "Describe the flag of Canada"
Root Agent: Routes to flag_agent
Response: "The flag of Canada features a red maple leaf centered on a white square..."
```

### Comprehensive Questions
```
User: "Tell me about Italy - capital and flag"
Root Agent: Uses both agents
Response: "Italy's capital is Rome, a historic city known for... [capital info]
         Italy's flag is a tricolor with green, white, and red vertical stripes... [flag info]"
```

## Key Features

✅ **Specialized Expertise** - Each agent focuses on their domain  
✅ **Smart Routing** - Root agent intelligently delegates questions  
✅ **Comprehensive Answers** - Combines information from multiple agents  
✅ **Consistent Format** - Well-organized, informative responses  
✅ **Extensible Design** - Easy to add more specialized agents  

## Benefits

- **Accurate Information** - Domain-specific expertise for each topic
- **Efficient Processing** - Questions routed to appropriate specialists
- **Rich Responses** - Comprehensive answers combining multiple perspectives
- **Scalable Architecture** - Easy to add new specialized agents
- **User Experience** - Single point of interaction for multiple topics

## Next Steps

This configuration can be extended with:
- Additional geographical agents (population, area, climate)
- Historical agents (founding dates, major events)
- Cultural agents (languages, religions, traditions)
- Economic agents (GDP, industries, trade)
