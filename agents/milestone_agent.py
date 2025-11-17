"""
Milestone Analyst Agent

Responsible for:
- Taking child age and behavior/drawing description as input
- Comparing with age-appropriate milestones (via tools)
- Returning clear, non-diagnostic feedback for parents
"""

from typing import Optional
from tools.child_age_db_tool import ChildAgeDBTool, MilestoneInfo

class MilestoneAnalystAgent:
    def __init__(self, tools: Optional[dict] = None, memory=None):
        self.tools = tools or {}
        self.memory = memory

    def analyze(self, age_months: int, description: str) -> str:
        """
        Uses the ChildAgeDBTool to fetch rough milestone info,
        and returns a friendly, non-medical explanation.
        """
        age_db: ChildAgeDBTool = self.tools.get("age_db")  # type: ignore

        if age_db is None:
            # Fallback if tool is missing
            return (
                f"[MilestoneAnalystAgent] For a child of {age_months} months: "
                f"I received the description: '{description}'.\n"
                "Milestone database tool is not available yet, "
                "but this will be enhanced with developmental ranges."
            )

        milestone_info: MilestoneInfo = age_db.get_milestones_for_age(age_months)

        # Optionally store something in memory (very simple example)
        if self.memory is not None:
            profile = self.memory.get_child_profile()
            profile["age_months"] = age_months
            profile["last_behavior_description"] = description
            self.memory.update_child_profile(profile)

        response = (
            f"For a child around **{milestone_info.age_range}** (your child: {age_months} months):\n\n"
            f"- Based on your description: _\"{description}\"_\n"
            f"- Typical abilities in this range:\n"
            f"  {milestone_info.summary}\n\n"
            f"Important:\n"
            f"- Children develop at different speeds.\n"
            f"- This is **not** a diagnosis and not a replacement for a pediatric assessment.\n"
            f"- If you have strong worries, contacting a pediatrician or child development specialist is always a good idea.\n\n"
            f"Extra note: {milestone_info.notes}"
        )

        return response
