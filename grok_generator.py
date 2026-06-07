from groq import Groq
from config import API_KEY
import json

client = Groq(api_key=API_KEY)


def generate_sql_and_data(user_prompt):

    prompt = f"""
You are a Text-to-SQL assistant.

User Request:
{user_prompt}

Generate ONLY valid JSON in the following format:

{{
    "table_name": "employees",
    "sql_query": "SELECT * FROM employees;",
    "data": [
        {{
            "id": 1,
            "name": "John",
            "department": "IT",
            "salary": 60000
        }}
    ]
}}

Rules:
1. Return ONLY JSON.
2. No markdown.
3. No explanation.
4. Generate 10 realistic rows.
5. SQL query must work on the generated dataset.
6. Detect table automatically.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        text = response.choices[0].message.content.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "").strip()

        return json.loads(text)

    except Exception as e:

        return {
            "table_name": "error",
            "sql_query": "Groq API temporarily unavailable",
            "data": [
                {
                    "message": str(e)
                }
            ]
        }