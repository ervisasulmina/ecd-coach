"""
Session Manager

Simple placeholder for:
- Session state (current conversation)
- Long-term memory (stored on disk)
"""

class SessionManager:
    def __init__(self):
        # Later: load from disk / database
        self.state = {}

    def get_child_profile(self) -> dict:
        return self.state.get("child_profile", {})

    def update_child_profile(self, profile: dict) -> None:
        self.state["child_profile"] = profile
