from app.langgraph.rag.vector_store import collection

def load_sample_policy():

    policy_text = """
    MRI procedures require:
    - valid insurance
    - diagnosis documentation
    - physician notes
    """

    collection.add(
        documents=[policy_text],
        ids=["policy_1"]
    )

    print("Policy loaded into ChromaDB")