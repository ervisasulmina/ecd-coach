"""
Safety Agent

Responsible for:
- Inspecting outputs from other agents
- Detecting medical / safety-related content
- Redirecting to safe messaging when needed
"""

class SafetyAgent:
    def __init__(self):
        pass

    def review(self, user_input: str, agent_output: str) -> str:
        """
        Placeholder: later, we will implement safety checks and rules.
        For now, just returns the agent_output unchanged.
        """
        # TODO: Add pattern checks, categories, and escalation logic.
        return agent_output
