from groq import Groq
from config.settings import Settings
import logging

class GroqService:

    def __init__(self):

        if not Settings.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found.")

        self.client = Groq(api_key=Settings.GROQ_API_KEY)

    def generate_response(self, messages):

        try:
            response = self.client.chat.completions.create(
                model=Settings.MODEL_NAME,
                messages=messages,
                temperature=0.3,
            )

            return response.choices[0].message.content

        except Exception as e:
            logging.error(f"Groq API Error: {str(e)}")
            return f"⚠️ API Error: {str(e)}"