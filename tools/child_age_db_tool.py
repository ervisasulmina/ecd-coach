"""
Child Age DB Tool

Very simple placeholder:
- Later, this will load milestone ranges from a JSON file
- For now, it returns a dummy range and description
"""

from dataclasses import dataclass

@dataclass
class MilestoneInfo:
    age_range: str
    summary: str

class ChildAgeDBTool:
    def __init__(self):
        # TODO: Load real data from JSON or another source
        pass

    def get_milestones_for_age(self, age_months: int) -> MilestoneInfo:
        # Placeholder logic
        return MilestoneInfo(
            age_range=f"{age_months-2}–{age_months+2} months (approx.)",
            summary="Placeholder milestone info. Real developmental data will go here."
        )
