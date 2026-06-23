class LLMService:
    def __init__(self, provider="gemini"):
        self.provider = provider
    def get_response(self, prompt, system_prompt=None):
        return f"[Demo] AI response to: {prompt[:100]}... (Add your GEMINI_API_KEY in secrets for real answers)"