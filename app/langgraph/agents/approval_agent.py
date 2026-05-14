def approval_agent(state):

    if state.get("approved"):
        return "APPROVED"

    return "REVIEW"