"""
main.py

Minimal functional version of the ECD-Coach agent system.

This file demonstrates:
- Multi-agent workflow (milestone → planner → mentor → safety)
- Use of tools + memory placeholders
- Clear architecture for future Gemini integration
"""

from agents.milestone_agent import MilestoneAnalystAgent
from agents.activity_planner_agent import ActivityPlannerAgent
from agents.mentor_agent import ParentMentorAgent
from agents.safety_agent import SafetyAgent

from tools.child_age_db_tool import ChildAgeDBTool
from tools.safety_response_tool import SafetyResponseTool

from memory.session_manager import SessionManager


def run_demo():
    """
    Runs a small demonstration to show multi-agent collaboration.
    """
    print("=== ECD-Coach Multi-Agent Demo ===\n")

    # Initialize tools
    age_db_tool = ChildAgeDBTool()
    safety_tool = SafetyResponseTool()

    # Initialize memory
    session = SessionManager()

    # Initialize agents
    milestone_agent = MilestoneAnalystAgent(
        tools={"age_db": age_db_tool},
        memory=session
    )
    planner_agent = ActivityPlannerAgent(
        tools={},
        memory=session
    )
    mentor_agent = ParentMentorAgent(memory=session)
    safety_agent = SafetyAgent()

    # DEMO INPUTS
    age_months = 33
    behavior_desc = "He drew a car with wheels and rode a two-wheel bike today."
    parent_concern = "I feel unsure if this is advanced or normal."

    print("Input child age:", age_months)
    print("Input behavior:", behavior_desc)
    print("Input concern:", parent_concern)
    print("\n---\n")

    # 1️⃣ Milestone analysis
    milestone_output = milestone_agent.analyze(age_months, behavior_desc)
    milestone_output = safety_agent.review(behavior_desc, milestone_output)
    print("Milestone Analyst Output:\n", milestone_output, "\n")

    # 2️⃣ Activity planning
    activity_output = planner_agent.plan_activities(age_months)
    activity_output_str = "\n".join(activity_output)
    activity_output_str = safety_agent.review("", activity_output_str)
    print("Activity Planner Output:\n", activity_output_str, "\n")

    # 3️⃣ Mentor response
    mentor_output = mentor_agent.respond(parent_concern)
    mentor_output = safety_agent.review(parent_concern, mentor_output)
    print("Parent Mentor Output:\n", mentor_output, "\n")

    print("=== End of Demo ===")


if __name__ == "__main__":
    run_demo()
