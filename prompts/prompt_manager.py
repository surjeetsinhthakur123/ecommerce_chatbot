class PromptManager:

    SYSTEM_PROMPT = """
You are a professional E-commerce AI Assistant.

ROLE:
- Help users discover products
- Compare products
- Suggest alternatives
- Answer return/refund/shipping questions

CONSTRAINTS:
- Only respond to e-commerce related queries
- If unrelated question, politely refuse
- Use bullet points for product lists
- Keep answers concise and structured
"""

    @staticmethod
    def build_messages(chat_history, user_query):

        messages = [
            {"role": "system", "content": PromptManager.SYSTEM_PROMPT}
        ]

        for msg in chat_history:
            messages.append({
                "role": msg["role"].lower(),
                "content": msg["content"]
            })

        messages.append({
            "role": "user",
            "content": user_query
        })

        return messages