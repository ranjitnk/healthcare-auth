class FHIRClient:

    def create_patient(self, payload):
        return {
            "resourceType":"Patient",
            "status":"created"
        }