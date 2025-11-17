"""
Safety Response Tool

Provides reusable safe messaging templates for:
- Health concerns
- Red-flag behaviors
"""

class SafetyResponseTool:
    @staticmethod
    def health_disclaimer() -> str:
        return (
            "I cannot provide medical diagnosis or treatment. "
            "If you have concerns about your child's health or development, "
            "please contact a pediatrician or qualified professional as soon as possible."
        )
