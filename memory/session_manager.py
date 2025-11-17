"""
Session Manager

Simple placeholder for:
- Session state (current conversation)
- Long-term memory (stored in memory for now)

Later, this can be extended to persist data to disk.
"""

class SessionManager:
    def __init__(self):
        # For now this is just an in-memory dictionary.
        # You could add file-based persistence later for long-term memory.
        self.state = {
            "child_profile": {
                # These can be updated as the agent learns more
                "age_months": None,
                "interests": ["cars", "animals"],
                "last_behavior_description": None,
            }
        }

    def get_child_profile(self) -> dict:
        """
        Returns the current child profile.
        Always returns a dict.
        """
        return self.state.get("child_profile", {})

    def update_child_profile(self, profile: dict) -> None:
        """
        Updates the stored child profile.
        """
        self.state["child_profile"] = profile
