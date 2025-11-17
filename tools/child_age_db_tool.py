"""
Child Age DB Tool

Simple, hard-coded developmental milestone info for demo purposes.

NOTE:
- This is NOT medical advice.
- These are rough, illustrative examples only, not diagnostic criteria.
"""

from dataclasses import dataclass

@dataclass
class MilestoneInfo:
    age_range: str
    summary: str
    notes: str

class ChildAgeDBTool:
    def __init__(self):
        # Very small "database" just for the demo
        self._db = {
            # Approx 30–36 months
            "30-36": MilestoneInfo(
                age_range="30–36 months",
                summary=(
                    "Around this age, many children can draw simple shapes, "
                    "start representing objects (like a 'car' or 'person') in their drawings, "
                    "and show improving balance and coordination."
                ),
                notes=(
                    "There is a wide normal range. Some children focus more on gross motor skills "
                    "like running or biking, others on fine motor or language."
                ),
            ),
        }

    def _get_bucket_key(self, age_months: int) -> str:
        """
        Very simple bucketing: we only support 30–36 months for now.
        
        """
        if 30 <= age_months <= 36:
            return "30-36"
        # default fall-back
        return "30-36"

    def get_milestones_for_age(self, age_months: int) -> MilestoneInfo:
        bucket = self._get_bucket_key(age_months)
        return self._db[bucket]
