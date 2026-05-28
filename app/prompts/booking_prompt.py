BOOKING_PROMPT = """
Extract booking information from the user message below.

IMPORTANT: Return ONLY a valid JSON object with these exact fields. If a field is missing, use null.

{{
  "name": "the person's name or null",
  "email": "the person's email or null",
  "date": "the date or null",
  "time": "the time or null"
}}

User message:
{message}

Return ONLY the JSON object, nothing else."""