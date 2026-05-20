from langgraph.graph import StateGraph

from app.langgraph.state.agent_state import AgentState

from app.langgraph.agents.extraction_agent import extraction_agent
from app.langgraph.agents.policy_agent import policy_agent
from app.langgraph.agents.validation_agent import validation_agent
from app.langgraph.agents.decision_agent import decision_agent

workflow = StateGraph(AgentState)

workflow.add_node("extract", extraction_agent)

workflow.add_node("policy", policy_agent)

workflow.add_node("validate", validation_agent)

workflow.add_node("decision", decision_agent)

workflow.set_entry_point("extract")

workflow.add_edge("extract", "policy")

workflow.add_edge("policy", "validate")

workflow.add_edge("validate", "decision")

graph = workflow.compile()