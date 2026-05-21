import os

from pypdf import PdfReader

from app.langgraph.rag.vector_store import collection

POLICY_FOLDER = "data/policies"

def load_sample_policy():

    existing = collection.get()

    if existing["ids"]:

        print("Policies already loaded")

        return

    policy_files = os.listdir(POLICY_FOLDER)

    counter = 0

    for file_name in policy_files:

        file_path = os.path.join(
            POLICY_FOLDER,
            file_name
        )

        text = ""

        # PDF Handling
        if file_name.endswith(".pdf"):

            try:

                reader = PdfReader(file_path)

                for page in reader.pages:

                    extracted = page.extract_text()

                    if extracted:

                        text += extracted

            except Exception as e:

                print(f"Skipping invalid PDF {file_name}: {e}")

                continue

        # TXT Handling
        elif file_name.endswith(".txt"):

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

        else:
            continue

        specialty = "general"

        if "ortho" in file_name.lower():
            specialty = "orthopedic"

        elif "cardio" in file_name.lower():
            specialty = "cardiology"

        collection.add(

            documents=[text],

            ids=[f"policy_{counter}"],

            metadatas=[{
                "specialty": specialty
            }]
        )

        print(f"Loaded policy: {file_name}")

        counter += 1

    print("All policies loaded into ChromaDB")