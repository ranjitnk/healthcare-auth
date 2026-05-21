from fastapi import APIRouter

from app.langgraph.orchestrator.workflow import graph
from app.langgraph.rag.policy_loader import load_sample_policy
from app.langgraph.utils.response_formatter import build_triage_report
from app.services.database.triage_service import save_triage_result

router = APIRouter(
    prefix="/agentic",
    tags=["Agentic AI"]
)

@router.post("/prior-auth")
def process_agentic_prior_auth(payload: dict):

    # Load policy into vector DB
    load_sample_policy()

    initial_state = {

        "claim_text": payload["claim_text"],

        "extracted_entities": {},

        "retrieved_policy": "",

        "validation_result": {},

        "final_decision": {},

        "reasoning_logs": []
    }

    # Run LangGraph workflow
    result = graph.invoke(initial_state)

    report = build_triage_report(result)
    save_triage_result(result)

    return report