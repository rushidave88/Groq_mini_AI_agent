import json
from config import get_client, SYSTEM_EXTRACT_PROMPT


def extract_structured(text):
   
    client = get_client()

    try:
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_EXTRACT_PROMPT},
                {"role": "user",   "content": text}
            ],
            response_format={"type": "json_object"},  
            temperature=1                              # 0 = consistent output
        )

       
        raw = response.choices[0].message.content

        
        parsed = json.loads(raw)

        
        return json.dumps(parsed, indent=2)

    except Exception as e:
        return f"Error during extraction: {e}"
    
