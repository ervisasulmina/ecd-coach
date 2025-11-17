"""
Activity Planner Agent

Responsible for:
- Generating daily/weekly activity ideas
- Using child age, interests and simple constraints (indoor/outdoor)
- This version is rule-based (no LLM yet), but already meaningful for parents.
"""

from typing import Optional

class ActivityPlannerAgent:
    def __init__(self, tools: Optional[dict] = None, memory=None):
        self.tools = tools or {}
        self.memory = memory

    def _get_child_interests(self) -> list[str]:
        """
        Reads interests from memory if available.
        """
        if self.memory is None:
            return []
        profile = self.memory.get_child_profile()
        return profile.get("interests", [])

    def plan_activities(self, age_months: int, constraints: Optional[dict] = None) -> list[str]:
        """
        Returns a small list of suggested activities.

        constraints example:
        {
            "setting": "indoor" or "outdoor"
        }
        """
        constraints = constraints or {}
        setting = constraints.get("setting", "indoor")
        interests = self._get_child_interests()

        activities: list[str] = []

        # Very basic age bucket; later you can expand to other ranges
        if 30 <= age_months <= 36:
            # Fine motor activity
            activities.append(
                "- **Fine motor (indoor)**: Offer crayons and paper and invite your child to draw their favorite object. "
                "You can sit together and talk about what they are drawing."
            )

            # Gross motor activity
            if setting == "indoor":
                activities.append(
                    "- **Gross motor (indoor)**: Create a simple obstacle course with pillows to climb over and a line on the floor to balance-walk on."
                )
            else:
                activities.append(
                    "- **Gross motor (outdoor)**: Go outside and practice riding the bike or running to 'catch' bubbles."
                )

            # Language / storytelling
            activities.append(
                "- **Language**: Look at a picture book together and ask open questions like "
                "\"What do you think will happen next?\" or \"Where is the car/animal?\""
            )

            # Pretend play
            activities.append(
                "- **Pretend play**: Use toy animals or cars to act out a tiny story together. "
                "Let your child decide what happens next."
            )

            # Personalization based on interest
            if "cars" in [i.lower() for i in interests]:
                activities.append(
                    "- **Interest-based**: Draw a simple road on paper and play with small cars on it. "
                    "You can add a 'garage', 'bridge', or 'tunnel' and let your child decide where each car goes."
                )

        else:
            # Generic fallback
            activities.append(
                "- Offer simple play that matches your child's interests (blocks, drawing, pretend play). "
                "This planner will be extended with more age ranges."
            )

        return activities
