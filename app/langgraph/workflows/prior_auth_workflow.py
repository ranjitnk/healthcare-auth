from app.langgraph.agents.approval_agent import approval_agent

def execute_workflow(payload):

    result = approval_agent(payload)

    return {
        "workflow_result": result
    }