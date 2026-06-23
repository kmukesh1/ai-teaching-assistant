from app.services.llm_service import LLMService

class TeachingService:
    def __init__(self):
        self.llm = LLMService()
    def explain_concept(self, concept, level="intermediate"):
        return self.llm.get_response(f"Explain {concept} at {level} level")