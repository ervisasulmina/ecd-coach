"""
Parent Mentor Agent

Responsible for:
- Responding to parents' emotional concerns
- Providing empathy and gentle, practical guidance
- Optionally using child profile info from memory
"""

from typing import Optional

class ParentMentorAgent:
    def __init__(self, memory: Optional[object] = None):
        self.memory = memory

    def _get_child_age_info(self) -> str:
        """
        Reads child age from memory if available, and formats a short sentence.
        """
        if self.memory is None:
            return ""
        profile = self.memory.get_child_profile()
        age_months = profile.get("age_months")
        if age_months:
            years = age_months // 12
            months = age_months % 12
            if years > 0:
                return f"Your child is around {years} years and {months} months old, which is still a very young age for learning these skills."
            else:
                return f"Your child is around {age_months} months old, which is still a very young age for learning these skills."
        return ""

    def respond(self, concern: str) -> str:
        """
        Generates a supportive, non-judgemental response
        based on the parent's concern text.
        """

        concern_lower = concern.lower()
        age_info = self._get_child_age_info()

        # Very simple pattern-based branching
        if any(word in concern_lower for word in ["guilty", "bad mom", "bad parent"]):
            theme = "guilt"
        elif any(word in concern_lower for word in ["worried", "unsure", "anxious"]):
            theme = "worry"
        elif any(word in concern_lower for word in ["playground", "pushed", "hit", "other child"]):
            theme = "social_conflict"
        else:
            theme = "generic"

        if theme == "guilt":
            message = (
                "First, it makes a lot of sense that you feel this way. Parents who worry about being a 'bad parent' "
                "are usually exactly the ones who care deeply and are trying their best.\n\n"
                f"{age_info}\n\n"
                "A few gentle suggestions:\n"
                "- Notice what you *are* doing for your child each day, even the small things (cuddles, stories, meals).\n"
                "- Try to replace the thought 'I'm a bad parent' with 'I'm a caring parent who is still learning'.\n"
                "- If these feelings show up often, talking to a supportive friend or professional can help you feel less alone."
            )
        elif theme == "worry":
            message = (
                "It's completely normal to feel unsure about your child's development. Every parent compares, wonders, "
                "and sometimes feels a bit lost.\n\n"
                f"{age_info}\n\n"
                "What you can do right now:\n"
                "- Focus on connection: play together, talk, and be present, even for a few minutes at a time.\n"
                "- If a specific behavior worries you, keep a small note of when it happens and what you see.\n"
                "- If your worry stays strong over time, bringing these notes to a pediatrician or child development specialist can provide clarity."
            )
        elif theme == "social_conflict":
            message = (
                "Situations like being pushed or having conflicts with other children can feel very upsetting to watch as a parent. "
                "Your reaction shows how much you care about your child's safety and feelings.\n\n"
                f"{age_info}\n\n"
                "You might try:\n"
                "- Comforting your child first: naming their feeling (e.g., 'You were scared when you were pushed').\n"
                "- Later, talking briefly about what happened in simple words and reassuring them that you are there to protect them.\n"
                "- If this happens often with the same child or environment, speaking calmly with the other adult involved can help set gentler boundaries."
            )
        else:
            message = (
                "Thank you for sharing how you feel. Parenting brings up a lot of emotions—worry, doubt, love, and sometimes frustration—all at the same time.\n\n"
                f"{age_info}\n\n"
                "A few general ideas that can help many parents:\n"
                "- Give yourself permission to be 'good enough', not perfect.\n"
                "- Notice one small moment each day that went well with your child and mentally highlight it.\n"
                "- Reach out to someone you trust and share how you feel; you don’t have to carry everything alone."
            )

        return message
