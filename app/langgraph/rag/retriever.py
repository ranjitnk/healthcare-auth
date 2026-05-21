from app.langgraph.rag.vector_store import collection

def retrieve_policy(procedure, diagnosis=""):

    search_query = f"""
    Medical procedure:
    {procedure}

    Diagnosis:
    {diagnosis}

    Prior authorization requirements
    """

    specialty = "general"

    if "knee" in procedure.lower():
        specialty = "orthopedic"

    elif "heart" in procedure.lower():
        specialty = "cardiology"

    results = collection.query(

        query_texts=[search_query],

        n_results=2,

        where={
            "specialty": specialty
        }
    )

    print("CHROMA RESULTS:", results)

    documents = results.get("documents", [[]])

    if documents and documents[0]:

        return "\n".join(documents[0])

    return "No matching policy found."